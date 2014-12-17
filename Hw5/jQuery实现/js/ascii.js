/*
 * Author: yuanzm
 * Last-Edit-Date: 2014/12/10
 */
;(function() {
	'use strict';
	var $sizeRadio = $("input[name='size']"),
 		$startButton = $("#startButton"),
		$stopButton = $("#stopButton"),
		$turboSpeed = $("#turboSpeed"),
		$displayarea = $("#displayarea"),
		$selectButton = $("#selectButton");

	$(function() {
		var ascii = new AsciiAnimation(ANIMATIONS);
		ascii.init();
	});
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
			$stopButton.prop('disabled', true);
			this.bindHandler(this);
		},
		bindHandler: function(self) {
			$sizeRadio.bind('click', function() { self.changeFontSize(self); });
			$startButton.bind('click', function() { self.startAnimation(self); });
			$stopButton.bind('click', function() { self.stopAnimation(self); });
			$turboSpeed.bind('click', function() { self.speed = $turboSpeed.prop('checked') ? 50:200; });
		},
		changeFontSize: function(self) {
			$sizeRadio.each(function(index) {
				if($(this).prop('checked')) { $displayarea.css('font-size', self.fontArray[index])}
			})
		},
		chooseAnimation: function(self) {
			self.asciiIndex = self.asciiArray[$selectButton.val()];
			self.allFrames = self.asciiIndex.split("=====\n");
		},
		startAnimation: function(self) {
			self.chooseAnimation(self);
			if (self.allFrames != '') {
				self.actionAnimation(self, 0);
				$stopButton.prop('disabled', false);
				$startButton.prop('disabled', true);
				$selectButton.prop('disabled', true);
			}
		},
		stopAnimation: function(self) {
			clearTimeout(self.nextFrame);
			$displayarea.val(self.asciiIndex);
			$stopButton.prop('disabled', true);
			$startButton.prop('disabled', false);
			$selectButton.prop('disabled', false);
		},
		actionAnimation: function(self, index) {
			self.currentIndex = index < self.allFrames.length - 1?(index + 1):0;
			$displayarea.val(self.allFrames[index]);
			self.nextFrame = setTimeout(self.actionAnimation, self.speed, self, self.currentIndex);
		}
	}
})()