$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    data.results.forEach(function (film){
        $('UL#list_movies').append(`<li>${film.title}</li>`);
    })
});
