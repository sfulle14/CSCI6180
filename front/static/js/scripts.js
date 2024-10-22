Dropzone.autoDiscover = false;
    $(document).ready(function () {
        var myDropzone = new Dropzone("#myDropzone", {
            paramName: "video_file",  // The name that will be used to transfer the file
            maxFilesize: 50,  // MB
            maxFiles: 5,  // Maximum number of files
            acceptedFiles: "video/*",  // Allow only video files
        });
    });


document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    var videoUrl = document.querySelector('input[name="video_url"]').value;
    document.querySelector('input[name="video_url"]').value = encodeURIComponent(videoUrl);
    this.submit();
});

$(document).ready(function () {
    var video = document.getElementById('my-video');
    var slider = document.getElementById('video-slider');

    // Update the slider as the video plays
    video.addEventListener('timeupdate', function () {
        slider.value = (video.currentTime / video.duration) * 100;
    });

    // Seek the video when the slider is changed
    slider.addEventListener('input', function () {
        var newTime = (slider.value / 100) * video.duration;
        video.currentTime = newTime;
    });
});


