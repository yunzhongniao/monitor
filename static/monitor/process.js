function monitorProcess() {
    var process_id = $('#pid').val();
    var interval = $('#interval').val();
    var count = $('#count').val();
    $.get("/mon/" + interval + "/" + count + "/process/" + process_id, function (data) {
            alert("Success to monitor process :" + process_id);
        }
    ).fail(function () {
        alert("Failed to monitor process :" + process_id);
    })
}

function backMain() {
    window.location.href = "/index"
}