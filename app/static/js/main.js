$(document).ready(function () {
    $('#correctionForm').submit(function (e) {
        e.preventDefault();

        $(".alert").remove();
        $('#correctedText').hide();
        $('#correctedContent').text('');

        var formData = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/",
            data: formData,
            success: function (response) {
                var taskId = response.task_id;
                $('#correctedText').hide();
                pollForCompletion(taskId);
            },
            error: function (xhr, status, error) {
                var errorMessage = JSON.parse(xhr.responseText).error || "Unknown error";
                displayError(errorMessage);
            }
        });
    });
});

function pollForCompletion(taskId) {
    var checkTask = function () {
        $.ajax({
            type: "GET",
            url: "/task/" + taskId,
            success: function (data) {
                if (data.state == 'SUCCESS') {
                    $('#correctedContent').text(data.result);
                    $('#correctedText').show();
                } else if (data.state != 'FAILURE') {
                    setTimeout(checkTask, 1000); // Poll rate
                } else {
                    displayError('Error processing your request.');
                }
            }
        });
    };
    checkTask();
}

function displayError(message) {
    $(".alert").remove();

    const alertHTML = `<div class="alert alert-danger">${message}</div>`;
    $(alertHTML).prependTo('.container');
}