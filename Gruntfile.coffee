module.exports = (grunt) ->
	grunt.initConfig
		pkg :
			grunt.file.readJSON 'package.json'	
		#自动编译coffee文件
		coffee:
			build:
				expand:true
				cwd : 'static/coffee'
				src : [ '**/*.coffee' ]
				dest : 'static/js'
				ext :'.js'
		#自动编译scss文件
		sass:
			dist:
				files: [{
						expand : true
						cwd : "static/scss"
						src : ['**/*.scss']
						dest : 'static/css'
						ext : '.css'
					}]
		#查看文件变化				
		watch:
			options:
      			livereload: true
			scripts:
				files: [ '**/*.coffee','Gruntfile.coffee' ]
				tasks: ["coffee"]
				option: 
					spawn: false
			css:
				files :['**/*.scss']
				tasks : ["sass"]
				option:
					spawn :false

	grunt.loadNpmTasks 'grunt-contrib-coffee'
	grunt.loadNpmTasks 'grunt-contrib-watch'
	grunt.loadNpmTasks 'grunt-contrib-sass'

	grunt.registerTask "default", ->
    	grunt.task.run [
    	  "coffee"
    	  "sass"
	      "watch"
    	]

    grunt.registerTask "build", ['coffee','sass',"watch"]
