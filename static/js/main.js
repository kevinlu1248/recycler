'use strict';
$ = jQuery;
$(document).ready(() => {

    // make image show up
    var fr = new FileReader();
    fr.onload = (e) => {
        $("#selected-image")[0].src = e.target.result;
    };

    $("#image").on('change', (e) => {
        console.log($("#image")[0].files[0]);
        fr.readAsDataURL($("#image")[0].files[0]);
        $("#submit").removeAttr("disabled");
        $("#image-upload").submit();
    });

    // drag and drop image
    var isAdvancedUpload = function () {
        var div = document.createElement('div');
        return (('draggable' in div) || ('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window;
    }();

    var $form = $('.box');
    var droppedFile, droppedFiles;
    $form.addClass('has-advanced-upload');
    $form.on('drag dragstart dragend dragover dragenter dragleave drop', function (e) {
        e.preventDefault();
        e.stopPropagation();
    }).on('dragover dragenter', function () {
        $form.addClass('is-dragover')
            .removeClass('is-success')
            .removeClass('is-error');
    }).on('dragleave dragend drop', function () {
        $form.removeClass('is-dragover')
            .removeClass('.is-success')
            .removeClass('.is-error');
    }).on('drop', function (e) {
        console.log(e.originalEvent.dataTransfer.files[0]);
        droppedFiles = e.originalEvent.dataTransfer.files;
        droppedFile = droppedFiles[0];
        $("#image-label").html(droppedFile.name);
        fr.readAsDataURL(droppedFile);
        //$("#submit").attr("disabled", false);
        $("#image-upload").submit();
    });

    // make box clickable
    $form.click((e) => {
        if (e.target != $form[0]) {
            return;
        }
        $("#image-label").trigger("click");
    });

    // file submission
    var types = ["paper", "cardboard", "glass", "metal", "plastic", "trash"];
    var capitalize_first = (s) => {
        return s.slice(0, 1).toUpperCase() + s.slice(1);
    };

    $("#image-upload").submit((e) => {
        e.preventDefault();

        if ($form.hasClass('is-uploading')) return false;
        $form.addClass('is-uploading').removeClass('is-error');

        // TODO: check for legacy browsers
        // if (isAdvancedUpload) {
        //     // ajax for modern browsers
        // } else {
        //     // ajax for legacy browsers
        // }

        var data = new FormData($("#image-upload")[0]);

        if (droppedFile) {
            console.log(droppedFile);
            data.set("image", droppedFile);
        }

        $("#classification").html(`<div class="spinner-border text-success" role="status">
                <span class="sr-only">Loading...</span>
                </div>`);

        console.log(data.get('image'));
        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/classify",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function (data) {
                console.log("SUCCESS : ", data);
                if (!data.success) {
                    $("#output").html("An unexpected error has occurred. Please try again later.");
                    return;
                }
                var conf = data.normalized;
                $("#classification").html(`${capitalize_first(data.classification.name)} (${(data.classification.confidence * 100).toFixed(1)}%)`);

                // if (!conf) {
                //     conf = {};
                //     types.forEach((v, i) => {
                //         conf[v] = 0;
                //     })
                // }
                if (conf) {
                    types.sort((a, b) => conf[b] - conf[a]);
                    $("#output").html("");
                    types.forEach((v) => {
                        console.log(`${v} yields ${conf[v]}`);
                        if (v !== data.classification.name) {

                            $("#output").append(`<li>${capitalize_first(v)} (${(conf[v] * 100).toFixed(1)}%)</li>`);
                        }
                    });
                }

                $form.addClass('is-success').removeClass('is-uploading');
                // $("#image-label").html("Done. Click or drag image here to upload another image.");
            },
            error: function (e) {
                console.log("ERROR : ", e);
                $("#output").html("ERROR : ", e);

            }
        });
        console.log("Image sent successfully");
    });
});
