// import json;
"use strict";
console.log("Hello")
$(document).ready( () => {
    // hide the options for uploading an image by default
    $("#logoContainer").hide();

    // if the checkbox is checked or uncheck, either show or hide the options for uploading a team image
    $("#updateImage").change( () => {
      if($("#updateImage").prop("checked") == true) {
        console.log("checked");
        $("#logoContainer").show();
      } else {
        $("#logoContainer").hide();
      }
    });

    // set focus to the team name textbox
    $("#teamName").focus();

	// the handler for the click event of the submit button
    $("#submit").click( evt => {
        let isValid = true;
        let alerts = [];

        if ($("#alert").length > 0) {
            $("#alertBanner").html("");
        }

        // validate file size. File type will be validated by server
        if($("#updateImage").prop("checked") == true) {
            try {
                if ($("#teamLogo")[0].files[0].size !== undefined) {
                    const fileSize = $("#teamLogo")[0].files[0].size;
                    if (fileSize > 500000) {
                        alerts[alerts.length] = "File size is too large!";
                        isValid = false;
                    }
                }
            } catch (TypeError) { // ensure that a file is selected
                alerts[alerts.length] = "Team logo is required!";
                isValid = false;
            }
        }

        // validate the team Name
        const teamNamePattern = /\b[A-Za-z0-9\s]{6,30}\b/;
        const teamName = $("#teamName").val().trim();
        if (teamName == "") {
            alerts[alerts.length] = "Team Name field is required.";
            isValid = false;
        } else if ((teamName.length < 6) || (teamName.length > 30)) {
			alerts[alerts.length] = "Team Name field must be between 6 and 30 characters!";
            isValid = false;
        } else if ( !teamNamePattern.test(teamName) ) {
            alerts[alerts.length] = "Team name must only contain alphanumeric characters [A-Z, a-z, or 0-9] or white space."
            isValid = false;
        }
        $("#teamName").val(teamName);

        // validate the player selection blocks
        $(".col").each((index, block) => {
            console.log("block");
            console.log($(block).attr("id"));
            if ($(block).find(":selected").text() == ""){
                alerts[alerts.length] = $(block).attr("id") + " must have selection";
                isValid = false;
            }
        })
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

    $(".col").on("change", evt => {
        const block = evt.currentTarget;
        console.log($(block).find(":selected").text())
    })
});