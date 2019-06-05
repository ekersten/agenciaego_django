$(window).on('load resize orientationchange', function() {
    $('.slider').each(function(){
        var $carousel = $(this);
        /* Initializes a slick carousel only on mobile screens */
        // slick on mobile
        if ($(window).width() > 768) {
            if ($carousel.hasClass('slick-initialized')) {
                $carousel.slick('unslick');
            }
        }
        else{
            if (!$carousel.hasClass('slick-initialized')) {
                $carousel.slick({
                    dots: true,
                    slidesToShow: 1,
                    //adaptiveHeight: true,
                    mobileFirst: true,
                    autoplay: false,
                    speed: 400,
                });
            }
        }
    });
});

