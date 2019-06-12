let mix = require('laravel-mix');

mix.sass('core/assets/sass/admin.scss', 'core/static/css/admin.css').sourceMaps()
mix.copyDirectory('core/assets/img', 'core/static/img');