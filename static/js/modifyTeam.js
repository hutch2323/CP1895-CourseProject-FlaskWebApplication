

$(document).ready( () => {

    // var teams = {{ poolTeams|tojson }};
    // console.log(teams)

    $("#teamSelector").on("change", () => {
        console.log($("#teamSelector").find(":selected").text());
        teamName = $("#teamSelector").find(":selected").text();
        const object = $("#teamSelector").val();
        console.log(json.dumps(object.teamName);
        $("#teamName").val(teamName);
    })

    $(".block").on("change", evt => {
        const block = evt.currentTarget;
        console.log($(block).find(":selected").text())
    })
});