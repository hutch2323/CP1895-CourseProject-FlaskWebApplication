import sqlite3
from contextlib import closing
import os
from flask import Flask, render_template, redirect, request, abort
import imghdr
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_PATH"] = "static/images"
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.png', '.jfif', '.jpeg']

conn = sqlite3.connect("images.db", check_same_thread=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/photos")
def photos():
    with closing(conn.cursor()) as c:
        query = '''Select  * From Images'''
        c.execute(query)
        results = c.fetchall()
        images = []
        for result in results:
            images.append((result[1], result[2])) #index 1 is the file name

    return render_template("photos.html", images=images)

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/update", methods = ['POST'])
def getFormData():
    uploaded_file = request.files["file"]
    caption = request.values["caption"]
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]: # or file_ext != validate_image(uploaded_file.stream): --> Taken out (can't get it to work)
            abort(400)
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))

        with closing(conn.cursor()) as c:
            query = '''Insert into Images(Filename, Caption)
                        Values(?, ?)'''
            c.execute(query, (uploaded_file.filename, caption))
            conn.commit()

    return redirect("photos")

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')