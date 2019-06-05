var main_menu_visible = false;

$(document).ready(function(e) {
	//btMenu
	$('#nav-toggle').on('click', function(){

		if(main_menu_visible){
			main_menu_visible=false;
		}
		else{
			main_menu_visible=true;
		}

        $(this).toggleClass("active");
        $( ".nav" ).stop(true,true).toggleClass("nav-open");
		$('i.x').stop(true,true).fadeToggle(400, 'linear');
        $(".overlay").stop(true,true).fadeToggle(300, "linear");
	});

	$('header').on('click', function(e){
			e.stopPropagation();
	});
	$('i.x').on('click', function(e){
		if($('nav').hasClass('nav-open')){
			$('.nav').removeClass('nav-open');
            $('i.x').fadeOut(100);
            $(".overlay").fadeOut(300);
            $('#nav-toggle').removeClass("active");
		}
	});

});

$(window).scroll(function(){

	if($('.nav').hasClass('nav-open')){
		$('.nav').removeClass('nav-open');
        $('i.x').fadeOut(100);
        $(".overlay").fadeToggle(300, "linear" );
        $('#nav-toggle').removeClass("active");
    }
    if ( $(window).width() < 800) {
        if($(window).scrollTop() > 1){
            $(".js-header").addClass("-scrolled");
        }
        else if($(window).scrollTop() < 2) {
            $(".js-header").removeClass("-scrolled");
        }
    } else {
        if($(window).scrollTop() > 75){
            $(".js-header").addClass("-scrolled");
        }
        else if($(window).scrollTop() < 76) {
            $(".js-header").removeClass("-scrolled");
        }
    }

    if($(window).scrollTop() > 500){
        $(".header__title").css('opacity', 1);
    }
    else if($(window).scrollTop() < 501) {
        $(".header__title").css('opacity', 0);
    }

});