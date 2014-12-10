/*
 * Author: yuanzm
 * Last-Edit-Date: 2014/12/10
 */
;(function() {
	'use strict';
	var fontSize =  $("fontSize");
	var sizeRadio = $A(fontSize.getElementsByTagName('input'));
	var stratbutton = $("startButton");
	var stopButton = $("stopButton");
	var turboSpeed = $("turboSpeed");
	var displayarea = $("displayarea");

	window.onload = function() {
		var ascii = new asciiAnimation(ANIMATIONS);
		ascii.init();
		ascii.bindHandler();
	}
	function asciiAnimation(asciiArray) {
		this.asciiArray = asciiArray;
		this.asciiIndex = asciiArray[$F('selectButton')];
		this.speed = 200;
		this.currentIndex = -1;
		this.nextFrame = null;
		this.currentFrame = null;
	}
	asciiAnimation.prototype = {
		constructor: asciiAnimation,
		fontArray: $w('7pt 12pt 24pt'),
		init: function() {
			stopButton.disabled = true;
		},
		bindHandler: function() {
			var self = this;
			fontSize.observe('click', function() {
				self.changeFontSize(self);
			});
			stratbutton.observe('click', function() {
				self.startAnimation(self);
			});
			stopButton.observe('click', function() {
				self.stopAnimation(self);
			});
			turboSpeed.observe('click', function() {
				var speed = $F('turboSpeed') === 'on'? 50:200;
				self.turboAnimation(speed);
			})
		},
		changeFontSize: function(self) {
			sizeRadio.each(function(item, index) {
				if(item.checked) {
					displayarea.style.fontSize = self.fontArray[index];
				}
			})
		},
		chooseAnimation: function(self) {
			self.asciiIndex = self.asciiArray[$F('selectButton')];
			self.currentFrame = self.asciiIndex.split("=====\n");
		},
		startAnimation: function(self) {
			self.chooseAnimation(self);
			if (self.currentFrame != '') {
				self.actionAnimation(self, 0);
				stopButton.disabled = false;
				startButton.disabled = true;
				selectButton.disabled = true;
			}
		},
		stopAnimation: function(self) {
			clearTimeout(self.nextFrame);
			displayarea.value = self.asciiIndex;
			startButton.disabled = false;
			stopButton.disabled = true;
			selectButton.disabled = false;
		},
		turboAnimation: function(speed) {
			this.speed = speed;
		},
		actionAnimation: function(self, index) {
			if (self.currentFrame.length > 0) {
				if (index < self.currentFrame.length - 1) {
					self.currentIndex = index + 1;
				} else {
					self.currentIndex = 0;
				}
				displayarea.value = self.currentFrame[index];
				self.nextFrame = setTimeout(self.actionAnimation, self.speed, self, self.currentIndex);
			}
		}
	}
})()