

$(document).ready( () => {
    $("h3").next().hide();

    $("h3").click( evt => {
        evt.preventDefault();
        const h3 = evt.currentTarget;
        if ($(h3).next().is(":visible")) {
            $(h3).next().hide();
        } else {
            $(h3).next().show();
        }
    });

	// the handler for the click event of the submit button
    $("#removeTeam").click( evt => {
        let teamToRemove = $("#teamRemoval").find(":selected").text();
        if (!confirm("Confirm Removal of " + teamToRemove)) {
            evt.preventDefault();
        }
    });

    $("#removeUser").click( evt => {
        let userToRemove = $("#userRemoval").find(":selected").text();
        if (!confirm("Confirm Removal of " + userToRemove)) {
            evt.preventDefault();
        }
    });

});