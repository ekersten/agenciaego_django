let mix = require('laravel-mix');
let fs = require('fs');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

// mix.disableNotifications();

if (!mix.inProduction()) {
    mix.webpackConfig({
        devtool: 'inline-source-map'
    })
}

mix.options({
    postCss: [
        require('autoprefixer')({
            browsers: ['last 2 versions', '> 5%', 'Firefox ESR'],
            cascade: false
        })
    ]
}).sourceMaps(false);

mix.autoload({
    'jquery': ['jQuery', '$'],
});

// disable manifest
Mix.manifest.refresh = _ => void 0


/* agenciaego */
mix.sass('agenciaego/assets/sass/main.scss', 'agenciaego/static/css/main.css').options({ processCssUrls: false });
mix.sass('agenciaego/assets/sass/slick.scss', 'agenciaego/static/css/slick-slider.css').options({ processCssUrls: false });
mix.sass('agenciaego/assets/sass/editable.scss', 'agenciaego/static/css/editable.css').options({ processCssUrls: false });
mix.copyDirectory('agenciaego/assets/fonts', 'agenciaego/static/fonts');
mix.copyDirectory('agenciaego/assets/img', 'agenciaego/static/img');


mix.scripts([
    // vendor
    'node_modules/jquery/dist/jquery.min.js',
    'node_modules/materialize-css/dist/js/materialize.min.js',
    'node_modules/sharer.js/sharer.min.js',
    'agenciaego/assets/js/clamp.min.js',
    'agenciaego/assets/js/navbar.js',
    'agenciaego/assets/js/app.js'

], 'agenciaego/static/js/app.js');

mix.scripts([
    // vendor
    'agenciaego/assets/js/pace.min.js'

], 'agenciaego/static/js/pace.js');

mix.scripts([
    'agenciaego/assets/js/slick.min.js',
    'agenciaego/assets/js/slider.js'

], 'agenciaego/static/js/slider.js');

/* blog */

mix.scripts([
    'node_modules/jquery/dist/jquery.min.js',
    'node_modules/sharer.js/sharer.min.js',
    'node_modules/infinite-scroll/dist/infinite-scroll.pkgd.js',
    'blog/assets/js/blog-post.js'
], 'blog/static/js/blog-post.js');

/* behance */
mix.scripts([
    'behance/assets/js/projects.js'
], 'behance/static/js/projects.js');


let scanDirs = function(dir='./') {
    return fs.readdirSync(dir).filter(file => {
        return fs.statSync(`${dir}/${file}`).isDirectory() && file.substr(0,1) !== '.'
    })
}

const dirs = scanDirs()
dirs.forEach(dir => {
    const mixFile = `./${dir}/webpack.mix.js`
    if (fs.existsSync(mixFile)) {
        require(mixFile)
    }
})