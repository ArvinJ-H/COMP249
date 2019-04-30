(function() {
	$(document).ready(function() {
		$('#likeform').submit(function(event) {
			var input = $(this).children("input[name='thing']");
			var thing = $(input).val();
			$(input).val('');

			if (thing[0] === '#' && thing.length === 7) {
				$('body').css('background-color', thing);
			} else {
				var toAdd = '<li>' + thing + '</li>';
				$('#likes').append(toAdd);
				toAdd.click(function() {
					console.log(Math.random());
					$(this).remove();
				});
			}
			event.preventDefault();
		});
	});
})();
