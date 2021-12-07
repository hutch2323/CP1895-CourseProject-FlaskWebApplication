// import json;
"use strict";
$(document).ready( () => {
    // hide the options for uploading an image by default
    $("#teamLogoLabel").hide();
    $("#teamLogo").hide();

    // if the checkbox is checked or uncheck, either show or hide the options for uploading a team image
    $("#updateImage").change( () => {
      if($("#updateImage").prop("checked") == true) {
        console.log("checked");
        $("#teamLogoLabel").show();
        $("#teamLogo").show();
      } else {
        $("#teamLogoLabel").hide();
        $("#teamLogo").hide();
      }
    });

    // set focus to the team name textbox
    $("#teamName").focus();

	// the handler for the click event of the submit button
    $("#submit").click( evt => {
        let isValid = true;

		// validate the team Name
        const teamName = $("#teamName").val().trim();
		if (teamName == "") {
            $("#teamName").next().text("This field is required.");
            isValid = false;
		} else {
			$("#teamName").next().text("*");
		}
        $("#teamName").val(teamName);

        // validate the player selection blocks
        $(".block").each((index, block) => {
            console.log("block");
            console.log($(block).attr("id"));
            if ($(block).find(":selected").text() == ""){
                $("#teamName").next().text($(block).attr("id") + " must have selection");
                isValid = false;
            }
        })

        // prevent the submission of the form if any entries are invalid
        if (!isValid) {
            evt.preventDefault();
        }
    });

    $(".block").on("change", evt => {
        const block = evt.currentTarget;
        console.log($(block).find(":selected").text())
    })
});