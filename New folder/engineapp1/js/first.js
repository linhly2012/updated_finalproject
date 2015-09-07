$(document).ready(function() {

	var menu = $('.menu'),
		a = menu.find('a');

		a.wrapInner($('<span />'));
		// include the text in <span /> element.

		a.each(function(){
			var t = $(this), span = t.find('span');
			for (i=0;i<2;i++){
				span.clone().appendTo(t);
			}
			// add new <span /> elements to get a strong blur effect.
		});

		a.hover(function(){
			var t = $(this), s = t.siblings('a');
			t.toggleClass('shadow');
			s.toggleClass('blur');
		});


		$(a[0]).delay(500).queue(function(n) {
			$(this).mouseenter();
			n();
		});


		$(a[0]).delay(500).queue(function(n) {
			$(this).mouseleave();
			n();
		});

});
