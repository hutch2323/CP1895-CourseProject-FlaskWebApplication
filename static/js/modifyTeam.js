// import json;
"use strict";
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

        if ($("#alert").length > 0){
            $("#alertBanner").html("");
        }

		// validate the team Name
        const teamName = $("#teamName").val().trim();
		if (teamName == "") {
            alerts[alerts.length] = "Team Name field is required.";
            isValid = false;
		} else {
			$("#teamName").next().text("*");
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

        // prevent the submission of the form if any entries are invalid
        // if (!isValid) {
        //     evt.preventDefault();
        //     let alertString = ""
        //     for (let alert of alerts) {
        //         let stringHTML = `<div id="alert" class="alert alert-danger alter-dismissable fade show" role="alert">`;
        //         stringHTML += alert;
        //         stringHTML += `<button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span>
        //                    </button></div>`;
        //         $("#alertBanner").append(stringHTML);
        //     }
        // }
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
        }
    });

    $(".col").on("change", evt => {
        const block = evt.currentTarget;
        console.log($(block).find(":selected").text())
    })
});