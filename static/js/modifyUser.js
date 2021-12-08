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
            $("#alert span").click();
        }

        // validate username
        const user =  $("#userName").val();
		if (user == "") {
            // $("#teamName").next().text("Team logo is required.");
            alerts[alerts.length] = "Username is required!";
            isValid = false;
        } else if (user.length < 4) {
            alerts[alerts.length] = "Username must be greater than 4 characters";
            isValid = false;
        }
        $("#userName").val(user);

        // validate the email entry with a regular expression
        const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
        console.log($("#email").val().trim());
        const email = $("#email").val().trim();
        if (email == "") {
            // $("#email").next().text("This field is required.");
            alerts[alerts.length] = "Email Address field is required."
            isValid = false;
        } else if ( !emailPattern.test(email) ) {
            // $("#email").next().text("Must be a valid email address.");
            alerts[alerts.length] = "Must be a valid email address."
            isValid = false;
        }
        // else {
        //     $("#email").next().text("*");
        // }
        $("#email").val(email);

		// validate the first name
        const firstName = $("#firstName").val().trim();
		if (firstName == "") {
            // $("#teamName").next().text("Team Name field is required.");
            alerts[alerts.length] = "First Name field is required!";
            isValid = false;
		} else if (firstName <= 1) {
            alerts[alerts.length] = "First name must be greater than 1 character.";
            isValid = false;
        }
        // else {
		// 	// $("#teamName").next().text("*");
		// }
        $("#firstName").val(firstName);

        // validate the teamName
        const lastName = $("#lastName").val().trim();
		if (lastName == "") {
            // $("#teamName").next().text("Team Name field is required.");
            alerts[alerts.length] = "Last Name field is required!";
            isValid = false;
		} else if (lastName <= 1) {
            alerts[alerts.length] = "Last name must be greater than 1 character.";
            isValid = false;
        }
        // else {
		// 	// $("#teamName").next().text("*");
		// }
        $("#lastName").val(lastName);

        if($("#updatePassword").prop("checked") == true) {
            // validate the teamName
            const password1 = $("#password1").val().trim();
            if (password1 == "") {
                // $("#teamName").next().text("Team Name field is required.");
                alerts[alerts.length] = "Password field is required!";
                isValid = false;
            } else if (password1 <= 7) {
                alerts[alerts.length] = "Password must be at least than 7 characters.";
                isValid = false;
            } else if (password1 != $("#password2").val().trim()) {
                alerts[alerts.length] = "Passswords don't match.";
                isValid = false;
            }
            // else {
            // 	// $("#teamName").next().text("*");
            // }
            $("#password1").val(password1);
        }

        // $(".block").each((index, block) => {
        //     if ($(block).find(":selected").text() == ""){
        //         alerts[alerts.length] = $(block).attr("id") + " must have selection";
        //         // $("#teamName").next().text($(block).attr("id") + " must have selection");
        //         isValid = false;
        //     }
        // })

        // // validate the phone number with a regular expression
        // const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
        // const phone = $("#phone").val().trim();
        // if (phone == "") {
        //     $("#phone").next().text("This field is required.");
        //     isValid = false;
        // } else if ( !phonePattern.test(phone) ) {
        //     $("#phone").next().text("Use 999-999-9999 format.");
        //     isValid = false;
        // } else {
        //     $("#phone").next().text("*");
        // }
        // $("#phone").val(phone);

        // prevent the submission of the form if any entries are invalid
        if (!isValid) {
            evt.preventDefault();
            let alertString = ""
            for (let alert of alerts) {
                let stringHTML = `<div id="alert" class="alert alert-danger alter-dismissable fade show" role="alert">`;
                stringHTML += alert;
                stringHTML += `<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span>
                           </button></div>`;
                $("#alertBanner").append(stringHTML);
            }
        }
            // if ($("#alert").length > 0){
            //     let errorString = ""
            //     errorString += alertString;
            //     errorString += `<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span>
            //                </button></div>`;
            //     $("#alert").html(errorString);
            // } else {
            //     let stringHTML = `<div id="alert" class="alert alert-danger alter-dismissable fade show" role="alert">`;
            //     stringHTML += alertString;
            //     stringHTML += `<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span>
            //                </button></div>`;
            //     $("#alertBanner").append(stringHTML);
            // }
    });
});