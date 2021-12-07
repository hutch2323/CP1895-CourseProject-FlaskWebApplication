// import json;
"use strict";
$(document).ready( () => {
    // set focus to the team name text box
    $("#teamName").focus();

	// the handler for the click event of the submit button
    $("#submit").click( evt => {
        let isValid = true;
        let alerts = [];

        // // validate the file upload to ensure that a file is
        const teamLogo = $("#teamLogo").val();
		if (teamLogo == "") {
            // $("#teamName").next().text("Team logo is required.");
            alerts[alerts.length] = "Team logo is required!";
            isValid = false;
		}

		// validate the teamName
        const teamName = $("#teamName").val().trim();
		if (teamName == "") {
            // $("#teamName").next().text("Team Name field is required.");
            alerts[alerts.length] = "Team Name field is required!";
            isValid = false;
		} else {
			// $("#teamName").next().text("*");
		}
        $("#teamName").val(teamName);


        // // validate the email entry with a regular expression
        // const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
        // const email = $("#email").val().trim();
        // if (email == "") {
        //     $("#email").next().text("This field is required.");
        //     isValid = false;
        // } else if ( !emailPattern.test(email) ) {
        //     $("#email").next().text("Must be a valid email address.");
        //     isValid = false;
        // } else {
        //     $("#email").next().text("*");
        // }
        // $("#email").val(email);

        $(".block").each((index, block) => {
            if ($(block).find(":selected").text() == ""){
                alerts[alerts.length] = $(block).attr("id") + " must have selection";
                // $("#teamName").next().text($(block).attr("id") + " must have selection");
                isValid = false;
            }
        })

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
            for(let alert of alerts){
                alertString += alert + "\n"
            }
            window.alert(alertString);
        }
    });

    $(".block").on("change", evt => {
        const block = evt.currentTarget;
        console.log($(block).find(":selected").text())
    })
});