sizeRadio = document.getElementsByName 'size'
startButton = document.getElementById 'startButton'
stopButton = document.getElementById 'stopButton'
turboSpeed = document.getElementById 'turboSpeed'
displayarea = document.getElementById 'displayarea'
selectButton = document.getElementById 'selectButton'
class AsciiAnimation
	constructor: (@asciiArray)->
		 @asciiIndex = ''
		 @speed = 200
		 @currentIndex = -1
		 @nextFrame = null
		 @allFrames = null
	fontArray: ['7pt', '12pt', '24pt']
	init: ->
		stopButton.disabled = true
		@bindHandler(@)
	bindHandler: (self)->
		for radio in sizeRadio
			radio.addEventListener 'click', -> self.changeFontSize(self)
		startButton.addEventListener 'click', -> self.startAnimation(self)
		stopButton.addEventListener 'click', -> self.stopAnimation(self)
		turboSpeed.addEventListener 'click', -> self.speed = if turboSpeed.checked then 50 else 200
	changeFontSize: (self)->
		for radio, index in sizeRadio
			displayarea.style.fontSize = self.fontArray[index] if sizeRadio[index].checked
	chooseAnimation: (self)->
		self.asciiIndex = self.asciiArray[selectButton.value]
		self.allFrames = self.asciiIndex.split("=====\n")
	startAnimation: (self)->
		self.chooseAnimation(self)
		if self.allFrames[0] != ''
			self.actionAnimation(self, 0)
			stopButton.disabled = false
			startButton.disabled = true
			selectButton.disabled = true
	stopAnimation: (self)->
		clearTimeout(self.nextFrame)
		displayarea.value = self.asciiIndex
		stopButton.disabled = true
		startButton.disabled = false
		selectButton.disabled = false
	actionAnimation: (self, index)->
		self.currentIndex = if index < self.allFrames.length - 1 then (index + 1) else 0
		displayarea.value = self.allFrames[index]
		self.nextFrame = setTimeout(self.actionAnimation, self.speed, self, self.currentIndex)

module.exports = AsciiAnimation
