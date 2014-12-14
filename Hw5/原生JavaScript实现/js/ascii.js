/*
 * Author: yuanzm
 * Last-Edit-Date: 2014/12/10
 */
;(function() {
	'use strict';
	var sizeRadio = document.getElementById('fontSize').getElementsByTagName('input'),
		startButton = document.getElementById('startButton'),
		stopButton = document.getElementById('stopButton'),
		turboSpeed = document.getElementById('turboSpeed'),
		displayarea = document.getElementById('displayarea'),
		selectButton = document.getElementById('selectButton');

	window.onload = function() {
		var ascii = new AsciiAnimation(ANIMATIONS);
		ascii.init();
	}
	function AsciiAnimation(asciiArray) {
		this.asciiArray = asciiArray;
		this.asciiIndex = '';
		this.speed = 200;
		this.currentIndex = -1;
		this.nextFrame = null;
		this.allFrames = null;
	}
	AsciiAnimation.prototype = {
		constructor: AsciiAnimation,
		fontArray: ['7pt', '12pt', '24pt'],
		init: function() {
			stopButton.disabled = true;
			this.bindHandler(this);
		},
		bindHandler: function(self) {
			for(var i = 0;i < sizeRadio.length;i++) {
				sizeRadio[i].addEventListener('click', function() { self.changeFontSize(self)}, false);
			}
			startButton.addEventListener('click', function() { self.startAnimation(self); });
			stopButton.addEventListener('click', function() { self.stopAnimation(self); });
			turboSpeed.addEventListener('click', function() { self.speed = turboSpeed.checked === true ? 50:200; });
		},
		changeFontSize: function(self) {
			for (var i = 0;i < sizeRadio.length;i++) {
				if(sizeRadio[i].checked) { displayarea.style.fontSize = self.fontArray[i]}
			}
		},
		chooseAnimation: function(self) {
			self.asciiIndex = self.asciiArray[selectButton.value];
			self.allFrames = self.asciiIndex.split("=====\n");
		},
		startAnimation: function(self) {
			self.chooseAnimation(self);
			if (self.allFrames != '') {
				self.actionAnimation(self, 0);
				stopButton.disabled = false;
				startButton.disabled = true;
				selectButton.disabled = true;
			}
		},
		stopAnimation: function(self) {
			clearTimeout(self.nextFrame);
			displayarea.value = self.asciiIndex;
			stopButton.disabled = true;
			startButton.disabled = false;
			selectButton.disabled = false;
		},
		actionAnimation: function(self, index) {
			self.currentIndex = index < self.allFrames.length - 1?(index + 1):0;
			displayarea.value = self.allFrames[index];
			self.nextFrame = setTimeout(self.actionAnimation, self.speed, self, self.currentIndex);
		}
	}
})()