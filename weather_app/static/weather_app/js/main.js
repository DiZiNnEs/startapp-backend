$(document).ready(() => {

    // $('.intro-section .button').on('click', function() {
    //     $('.section').hide();
    //     $('.city-section').fadeIn();
    // });

    // $('.city-section form').on('submit', function() {
    //     $('.section').hide();
    //     $('.home-section').fadeIn();
    // });

    // E-mail Ajax Send
    $("form").submit(function (event) {
        let city = $('#city').val();
        window.location.href = "/home/city=" + city;
        return false;
    });


    // Модальные окна
    var overlay = $(".overlay"),
        modal = $(".modal"),
        modalClose = $(".modal__close"),
        modalOpen = $(".modal__open");

    overlay.click(function (e) {
        if ($(e.target).closest(".modal").length == 0) {
            $(this).fadeOut();
            modal.fadeOut();
        }
    });

    modalClose.click(function () {
        overlay.fadeOut();
        modal.fadeOut();
    });

    modalOpen.each(function () {
        $(this).on("click", function (e) {
            var modalId = $(this).attr("data-modal"),
                EachModal = $('.modal[data-modal="' + modalId + '"]');
            overlay.fadeIn();
            EachModal.fadeIn();
        });
    });

});
