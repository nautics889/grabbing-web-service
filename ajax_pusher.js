function call() {
	var msg = $('#links_form').serialize();
	$.ajax({
		type: 'POST',
		url: '/cgi-bin/handler.py',
		data: msg,
		success: function(data) {
			$('#results').html(data);
		},
		error: function(xhr, str) {
			alert('Возникла ошибка: ' + xhr.responseCode);
		}
	});
}