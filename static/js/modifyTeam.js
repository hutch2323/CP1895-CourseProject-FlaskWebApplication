// import json;

$(document).ready( () => {

    // var teams = {{ poolTeams|tojson }};
    // console.log(teams)
    let playerList = null;
    $("#teamSelector").on("change", () => {
        // console.log($("#teamSelector").find(":selected").text());
        // teamName = $("#teamSelector").find(":selected").text();
        // let playerList = $("#teamSelector").val();
        // console.log(playerList);
        // $("#teamName").val(teamName);
        // count = 0;
        // if (playerList != null){
        //     count = 1
        //     for (let player of playerList){
        //         console.log(player);
        //         blockSelector = `block${count}`;
        //         console.log(blockSelector);
        //         // $(blockSelector).val(player);
        //         if (count == 1){
        //             $("#1").val(player);
        //         }
        //         // $(`"#${count}"`).val(player);
        //         count++;
        //     }
        // }

        // let team= JSON.parse($("#teamSelector").val());
        // console.log(team.teamName);
    })

    $(".block").on("change", evt => {
        const block = evt.currentTarget;
        console.log($(block).find(":selected").text())
    })
});