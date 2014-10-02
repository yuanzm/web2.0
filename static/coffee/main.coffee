$ ->
	_contents = $(".content")
	_contents.mouseover ->
		_this = $(this)
		_details = _this.find(".details")
		_half = _details.find(".half")
		if _half.eq(0).text() is ""
			_this.css("font-size","16px")
			_half.replaceWith("<span>Updating</span>")