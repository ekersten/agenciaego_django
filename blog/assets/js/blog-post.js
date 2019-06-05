

var $container = $('.blog-posts').infiniteScroll({
    path: function() {
        return $('.blog-post').last().find('.pagination__next').attr('href');
    },
    append: '.blog-post',
    history: 'replace',
    checkLastPage: '.pagination__next',
    debug: false
});

$container.on('history.infiniteScroll', function (event, title, path) {
    var $blog_post = $('.blog-post[data-url="' + path + '"]');
    ga('send', 'pageview', window.location.pathname);
    $('header .container .header__title').text($blog_post.attr('data-title'));
});

$container.on('append.infiniteScroll', function (event, response, path, items) {
    giphyDisplay();
    heartLiker();
    window.Sharer.init();
    timeReader();
});

