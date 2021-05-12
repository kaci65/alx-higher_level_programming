$(function () {
  $.ajax({
    type: 'Get',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
