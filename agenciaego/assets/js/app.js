//HOME
//Text overflow
var module = document.getElementsByClassName("textOverflow");
for (i = 0; i < module.length; i++) {
    $clamp(module[i], {clamp: 4});
}

(function($){
    
    if ($(window).width() > 768) {
        $('.publications__col').hover(
            function(){
                $('.section__publications .col').not(this).css({'opacity': '0.4'});
                $('.section__publications').css({'border-color':'transparent'});
            },
            function(){
                $('.section__publications .col').css({'opacity': '1'});
                $('.section__publications').css({'border-color':'#e5e5e5'});
            }
        );
    }
   
    //Parallax image
    $('.parallax').parallax();

    (function() {
        window.addEventListener('scroll', function() {
            var depth, i, layer, layers, len, movement, topDistance, translate3d;
            topDistance = this.pageYOffset;
            layers = document.querySelectorAll("[data-type='parallax']");
            for (i = 0, len = layers.length; i < len; i++) {
            layer = layers[i];
            depth = layer.getAttribute('data-depth');
            movement = -(topDistance * depth);
            translate3d = 'translate3d(0, ' + movement + 'px, 0)';
            layer.style['-webkit-transform'] = translate3d;
            layer.style['-moz-transform'] = translate3d;
            layer.style['-ms-transform'] = translate3d;
            layer.style['-o-transform'] = translate3d;
            layer.style.transform = translate3d;
            }
        });

    }).call(this);

     $('.accordion__label').click(function(j) {
        var dropDown = $(this).closest('.accordion__dropdown').find('.accordion__content');

        $(this).closest('.accordion').find('.accordion__content').not(dropDown).slideUp();

        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
        } else {
            $(this).closest('.accordion').find('.accordion__label.active').removeClass('active');
            $(this).addClass('active');
        }

        dropDown.stop(false, true).slideToggle();

        j.preventDefault();
    });
    
})(jQuery); 

//Projects
 $(document).ready(function() {
    //Modal
    var modal = $('.project-modal');
    var last_modal_url = '';
    $('.modal-trigger').click(function(i) {
        i.preventDefault();
        // grabra url actual
        window.last_modal_url = window.location.href;
        // poner flag de que el modal esta abierto
        var $el = $(i.currentTarget);
        
        modal.load($el.attr('href'), function() {
            history.pushState({}, '', $el.attr('href'));
            ga('send','pageview',window.location.pathname);
            $(".pace").addClass('hide-pace');
            modal.stop(true, true).delay(500).fadeIn(0, "linear", function() {
                $(this).scrollTop(0);

                $(this).css({
                    visibility : 'visible',
                    opacity : 0
                });

                $(this).animate({ opacity: 1 }, 300);
            });

            $('body').css('overflow', 'hidden');
        });
    });
    
     modal.on('click', function(k){
        k.stopPropagation();
    });

     $('.project-modal').on('click', '.modal-close, .project-overlay', function() {
        modal.fadeOut(300, "linear");
        history.pushState({},'', window.last_modal_url);
        ga('send','pageview',window.location.pathname);
        $('body').css('overflow','auto');
        $(".pace").addClass('hide-pace');
    });  

    $("#projectModal").scroll(function() {
        if($(this).scrollTop()> 25) {
            $(".project-modal__header").addClass('header-fixed');    
        } else {
            $(".project-modal__header").removeClass('header-fixed');
        }
    });   

});


//BLOG POSTS
//Giphy display
giphyDisplay = function () {
    var yOff = 300;
    var xOff = -100;
    var textHover = $('a[href$=".gif"]');

    textHover.each(function (e) {
        $(this).hover(function (e) {
            $("body").append("<p id='giphy-image'><img src='" + $(this).attr('data-gif') + "'/></p>");
            $("#giphy-image").css("position", "absolute");
            if ($(window).width() > 768) {
                $("#giphy-image")
                .css("top", (e.pageY - yOff) + "px")
                .css("left", (e.pageX + xOff) + "px");
            } else if ($(window).width() < 767) {
                $("#giphy-image")
                .css("top", (e.pageY - 130) + "px")
                .css("left", (e.pageX + -100) + "px");
            }
            $("#giphy-image img").delay(400).animate({opacity: 1}, 100);
        },
            function(){
                $("#giphy-image").remove();
            }
        );

    });

    textHover.each(function (e) {
        $(this).mousemove(function (e) {
            if ($(window).width() > 768) {
                $("#giphy-image")
                .css("top", (e.pageY - yOff) + "px")
                .css("left", (e.pageX + xOff) + "px");
            } else if ($(window).width() < 767) {
                $("#giphy-image")
                .css("top", (e.pageY - 130) + "px")
                .css("left", (e.pageX + -100) + "px");
            }
        });
    });    
}    


//Like heart
heartLiker = function () {
    var $heart = $('input[type=checkbox].hackyBox');
    $heart.each(function (e) {
        if($(this).length > 0) {
            $(this).on('click', function(e) {
                var $this = $(this);
                var url = $(this).prop('checked') ? '/api/like/' + $(this).attr('data-post-id') : '/api/unlike/' + $(this).attr('data-post-id')
                $.getJSON(url, function(data) {
                    $this.parent().siblings('.value').text(data.likes);
                    console.log(data.likes);
                });
                
            });
        }
    });
    
} 

/* var iframes = document.getElementsByTagName('iframe');
for (var i = 0; i < iframes.length; i++) {
  iframes[i].src += "&version=3&loop=1&controls=0&showinfo=0&autoplay=1&mute=1&modestbranding=1";
} */

iframeModifier = function () {
    var iframes = $('iframe');
    var videoId;

    iframes.each(function () {
        var src = $(this).attr('src');
        if (src.match(/(\?|&)v=([^&#]+)/)) {
            videoId = src.match(/(\?|&)v=([^&#]+)/)[0];
            $(this).attr('src', src + '&showinfo=0&loop=1&playlist='+videoId+'&mute=1');
/*             $(this).wrap("<div class='top'><div class='wrapper'></div></div>");
 */        } else if (src.match(/(\.be\/)+([^\/]+)/)) {
            videoId = src.match(/(\.be\/)+([^\/]+)/)[0];
            $(this).attr('src', src + '&showinfo=0&loop=1&playlist='+videoId+'&mute=1');
/*             $(this).wrap("<div class='top'><div class='wrapper'></div></div>");
 */        } else if (src.match(/(\embed\/)+([^\/]+)/)) {
            videoId = src.match(/(\embed\/)+([^\/]+)/)[2].replace('?rel=0','');
            $(this).attr('src', src + '&showinfo=0&loop=1&playlist='+videoId+'&mute=1');
/*             $(this).wrap("<div class='top'><div class='wrapper'></div></div>");
 */        } else if (src.match(/(?:www\.|player\.)?vimeo.com\/(?:channels\/(?:\w+\/)?|groups\/(?:[^\/]*)\/videos\/|album\/(?:\d+)\/video\/|video\/|)(\d+)(?:[a-zA-Z0-9_\-]+)?/i)) {
            $(this).attr('src', src + '&transparent=0&loop=1&muted=1');
/*             $(this).wrap("<div class='top'><div class='wrapper'></div></div>");
 */        }
                
    });

}

timeReader = function() {
    var post = $(".editable");
    post.each(function (e) {
        if($(this).find('.reading-time').length <= 0) {
            var wordsPerMinute = 200;
            var noOfWords = $(this).text().toString().split(/\s/g).length;
            var minutes = noOfWords / wordsPerMinute;
            var readTime = Math.ceil(minutes);
            var title = $(this).find("h1");
            $("<p class='reading-time'><span>"+readTime+" min.</span> de lectura</p>" ).insertAfter(title);
            console.log($(this).text());
        }
    });
} 

iframeModifier();

$(document).ready(function() {
    giphyDisplay();
    timeReader();
}); 





  