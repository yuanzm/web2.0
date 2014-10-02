(function() {
  $(function() {
    var _contents;
    _contents = $(".content");
    return _contents.mouseover(function() {
      var _details, _half, _this;
      _this = $(this);
      _details = _this.find(".details");
      _half = _details.find(".half");
      if (_half.eq(0).text() === "") {
        _this.css("font-size", "16px");
        return _half.replaceWith("<span>Updating</span>");
      }
    });
  });

}).call(this);
