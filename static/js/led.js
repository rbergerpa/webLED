function initLED() {
  $(document).on('click', '.on_button', function() {
    setState(0,1);
 });

  $(document).on('click', '.off_button', function() {
    setState(0,0);
  });
}

function setState(id, state) {
  putJSON('/led/' + id, { state: state });
}

function putJSON(url, data) {
  return $.ajax({
    url: url,
    type: 'PUT',
    contentType: 'application/json',
    dataType: 'json',
    data: JSON.stringify(data)
  });
}

$(initLED);
