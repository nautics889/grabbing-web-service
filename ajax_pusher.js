function call_links() {
	var msg = $('#links_form').serialize();
	$.ajax({
		type: 'POST',
		url: '/cgi-bin/handler_links.py',
		data: msg,
		success: function(data) {
			$('#results').html(data);
		},
		error: function(xhr, str) {
			alert('Возникла ошибка: ' + xhr.responseCode);
		}
	});
}

function call_numbers() {
	var msg = $('#links_form').serialize();
	$.ajax({
		type: 'POST',
		url: '/cgi-bin/handler_phones.py',
		data: msg,
		success: function(data) {
			$('#results').html(data);
		},
		error: function(xhr, str) {
			alert('Возникла ошибка: ' + xhr.responseCode);
		}
	});
}

function call_mails() {
	var msg = $('#links_form').serialize();
	$.ajax({
		type: 'POST',
		url: '/cgi-bin/handler_emails.py',
		data: msg,
		success: function(data) {
			$('#results').html(data);
		},
		error: function(xhr, str) {
			alert('Возникла ошибка: ' + xhr.responseCode);
		}
	});
}