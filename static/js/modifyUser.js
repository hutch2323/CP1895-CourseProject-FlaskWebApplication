"use strict";
$(document).ready( () => {
    // set focus to the team name text box
    $("#teamName").focus();

    $("#password1Container").hide();
    $("#password2Container").hide();
    $("#updatePassword").change( () => {
      if($("#updatePassword").prop("checked") == true) {
        console.log("checked");
        $("#password1Container").show();
        $("#password2Container").show();
      } else {
        $("#password1Container").hide();
        $("#password2Container").hide();
      }
    });

	// the handler for the click event of the submit button
    $("#submit").click( evt => {
        let isValid = true;
        let alerts = [];

        if ($("#alert").length > 0){
            $("#alertBanner").html("");
        }

        // validate username
        const usernamePattern = /\b[A-Za-z0-9]{6,30}\b/;
        const username =  $("#username").val().trim();
		if (username == "") {
            // $("#teamName").next().text("Team logo is required.");
            alerts[alerts.length] = "Username is required!";
            isValid = false;
        } else if ((username.length < 4) || (username.length > 25)) {
            alerts[alerts.length] = "Username must be between 4 and 25 characters";
            isValid = false;
        } else if ( !usernamePattern.test(username) ) {
            // $("#email").next().text("Must be a valid email address.");
            alerts[alerts.length] = "Username must only contain alphanumeric characters [A-Z, a-z, or 0-9]."
            isValid = false;
        }
        $("#username").val(username);

        // validate the email entry with a regular expression
        const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
        const email = $("#email").val().trim();
        if (email == "") {
            // $("#email").next().text("This field is required.");
            alerts[alerts.length] = "Email Address field is required."
            isValid = false;
        } else if ( !emailPattern.test(email) ) {
            // $("#email").next().text("Must be a valid email address.");
            alerts[alerts.length] = "Must be a valid email address."
            isValid = false;
        } else if ((email.length <= 5) || (email.length > 50)) {
            alerts[alerts.length] = "Email address must be between 5 and 50 characters.";
            isValid = false;
        }
        $("#email").val(email);

		// validate the first name
        const firstName = $("#firstName").val().trim();
		if (firstName == "") {
            // $("#teamName").next().text("Team Name field is required.");
            alerts[alerts.length] = "First Name field is required!";
            isValid = false;
		} else if ((firstName.length <= 1) || (firstName.length > 30)){
            alerts[alerts.length] = "First name must be between 1 and 30 characters.";
            isValid = false;
        }
        $("#firstName").val(firstName);

        // validate the last name
        const lastName = $("#lastName").val().trim();
		if (lastName == "") {
            // $("#teamName").next().text("Team Name field is required.");
            alerts[alerts.length] = "Last Name field is required!";
            isValid = false;
		} else if ((lastName.length <= 1) || (lastName.length > 30)){
            alerts[alerts.length] = "Last name must be between 1 and 30 characters.";
            isValid = false;
        }
        $("#lastName").val(lastName);

        if($("#currentPassword").length){
            const currentPassword = $("#currentPassword").val().trim();
            if (currentPassword == "") {
            // $("#teamName").next().text("Team Name field is required.");
                alerts[alerts.length] = "Password field is required!";
                isValid = false;
		    } else if ((currentPassword.length <= 7) || (currentPassword.length > 30)) {
                alerts[alerts.length] = "Password must be be between 7 and 30 characters.";
                isValid = false;
            }
        }

        if($("#updatePassword").prop("checked") == true) {
            // validate the teamName
            const password1 = $("#password1").val().trim();
            if (password1 == "") {
                alerts[alerts.length] = "Password field is required!";
                isValid = false;
            } else if ((password1 <= 7) || (password1 > 30)){
                alerts[alerts.length] = "Password must be be between 7 and 30 characters.";
                isValid = false;
            } else if (password1 != $("#password2").val().trim()){
                alerts[alerts.length] = "Passswords don't match.";
                isValid = false;
            }
            $("#password1").val(password1);
        }

        if (!isValid) {
            evt.preventDefault();
            let alertString = ""
            for (let alert of alerts) {
                $("#alertBanner").append(`<div id="alert" class="alert alert-danger d-flex align-items-center" role="alert">
                          <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                          <div>
                            ${alert}
                          </div>
                    </div>`);
            }
            window.scrollTo(0, 335);
        }
    });
});