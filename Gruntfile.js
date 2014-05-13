module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      dist: {
        options: {
          sourcemap: true,
          style: 'compressed'
        },
        files: {
          './<%= pkg.name %>/static/css/app.css': './<%= pkg.name %>/static/scss/app.scss'
        }
      }
    },

    watch: {
      sass: {
        files: ['<%= pkg.name %>/static/scss/**/*.scss'],
        tasks: ['sass']
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['sass']);
  grunt.registerTask('dev', ['default', 'watch']);
};
