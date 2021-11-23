import db

def main():
    db.connect()

    print(db.getTeamStandings())

    db.close()

if __name__ == "__main__":
    main()