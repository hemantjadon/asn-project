var gulp = require('gulp');
var watch = require('gulp-watch');

var rename = require('gulp-rename');

//var minify = require('gulp-minify');
var tsc = require('gulp-typescript');
var tsProject = tsc.createProject('tsconfig.json');

var less = require('gulp-less');
var LessPluginCleanCSS = require('less-plugin-clean-css');
var LessPluginAutoPrefix = require('less-plugin-autoprefix');
var cleancss = new LessPluginCleanCSS({ advanced: true });
var autoprefix = new LessPluginAutoPrefix({ browsers: ["last 2 versions"] });

var config = require('./gulp.config')();

gulp.task('compile-less', function () {
    return gulp.src([config.angular_less_files_src,'!node_modules/**'])
        .pipe(less({}))
        .pipe(rename(function(path){
            var x = path.dirname.split('/');
            x.pop();
            x.push('css');
            path.dirname = x.join('/');
            return path;
        }))
        .pipe(gulp.dest(config.angular_less_files_dest));
});

gulp.task('transpile-ts', function () {
    return tsProject.src([config.angular_ts_files_src,'!node_modules/**','!typings/**'])
        .pipe(tsc(tsProject))
        .pipe(rename(function(path){
            var x = path.dirname.split('/');
            if(x[x.length-1] === 'ts'){
                x.pop();
                x.push('js');   
            }
            path.dirname = x.join('/');
            return path;
        }))
        .pipe(gulp.dest(config.angular_ts_files_dest));
});

gulp.task('watch',function () {
    watch([config.angular_less_files_src,config.angular_ts_files_src,'!node_modules/**','!typings/**'],function(){
        gulp.start('compile-less');
        gulp.start('transpile-ts');
    });
});
gulp.task('default',['compile-less','transpile-ts','watch']);
