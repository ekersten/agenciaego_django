$(document).ready(function () {
    $('a[data-target="projectModal"]').on('click', function (e) {
        var $this = $(e.currentTarget);
        var preloader = setInterval(function () {
            if ($('.pace.pace-active .pace-progress').length > 0) {
                var prog = parseInt($('.pace.pace-active .pace-progress').attr('data-progress-text'));
                // console.log('prog: ' + prog);
                prog *= 3;
                $this.find('.project-loader').css({
                    width: prog + '%',
                    'max-width': '100%'
                });
                if($this.find('.text-reveal').length > 0) {
                    $this.find('.text-reveal').css({
                        width: prog + '%',
                        'max-width': '100%'
                    });
                }
            }
        }, 100);
        Pace.once('done', function () {
            // console.log('fin')
            $this.find('.project-loader').css({
                width: '100%'
            });
            clearInterval(preloader);
            setTimeout(function () {
                $this.find('.project-loader').fadeOut(0).css({
                    width: '0'
                });
                if ($this.find('.text-reveal').length > 0) {
                    $this.find('.text-reveal').fadeOut(0).css({
                        width: '0'
                    });
                }
            }, 500)
        });
        
    });
});