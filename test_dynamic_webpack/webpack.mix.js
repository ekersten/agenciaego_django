let mix = require('laravel-mix');

mix.sass('test_dynamic_webpack/assets/sass/styles.scss', 'test_dynamic_webpack/static/css/styles.css').sourceMaps()