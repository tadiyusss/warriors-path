

$(document).ready(function () {
    $('.btn-redirect').on('click', function () {
        const targetUrl = $(this).attr('x-src');
        if (targetUrl) {
            window.location.href = targetUrl;
        }
    });
});