$('DIV#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').toggleClass('red');
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('green');
    $('header').toggleClass('red');
  }
});
