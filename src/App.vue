<template>

  <films-menu @movie-title-filtered='filterMoviesByTitle' @fromInterval="filterByFromInterval"
              @toInterval="filterByToInterval" @add-movie="showAddBlock"/>
  <films-list v-if="!addMovie" :movieTitleFilter="movieTitleFilter" :fromInterval="fromInterval"
              :toInterval="toInterval" :movieToAdd="movieToAdd" :movies="movies" @delete="deleteMovie"/>
  <films-add v-if="addMovie" @back="hideAddBlock" @save-movie="addMovieToList"/>
</template>

<script>


import FilmsList from "./components/Films-list";
import FilmsMenu from "./components/Films-menu";
import FilmsAdd from "./components/Films-add";

export default {
  name: 'App',
  components: {FilmsAdd, FilmsMenu, FilmsList},
  data() {
    return {
      movieTitleFilter: '',
      fromInterval: 0,
      toInterval: new Date().getFullYear(),
      addMovie: false,
      movieToAdd: {},
      movies: [
        {
          title: 'First',
          year: 1,
          country: '',
          genres: [
            'Action', 'Comedy', 'Drama'
          ]
        },
        {
          title: 'First',
          year: 1,
          country: '',
          genres: [
            'Action', 'Comedy', 'Drama'
          ]
        },
        {
          title: 'Second',
          year: 2,
          country: '',
          genres: [
            'Fantasy', 'Horror', 'Mystery'
          ]
        },
        {
          title: 'Third',
          year: 3,
          country: '',
          genres: [
            'Fantasy', 'Horror', 'Mystery'
          ]
        },
        {
          title: 'Fourth',
          year: 4,
          country: '',
          genres: [
            'Fantasy', 'Horror', 'Mystery'
          ]
        },
        {
          title: 'Fifth',
          year: 5,
          country: '',
          genres: [
            'Fantasy', 'Horror', 'Mystery'
          ]
        },
        {
          title: 'Sixth',
          year: 6,
          country: '',
          genres: [
            'Horror', 'Mystery'
          ]
        },
        {
          title: 'Seventh',
          year: 7,
          country: '',
          genres: [
            'Fantasy', 'Horror', 'Mystery'
          ]
        },
        {
          title: 'Eight',
          year: 8,
          country: '',
          genres: [
            'Horror', 'Fantasy', 'Mystery'
          ]
        },
        {
          title: 'Ninth',
          year: 9,
          country: '',
          genres: [
            'Horror',
          ]
        },
        {
          title: 'Tenth',
          year: 9,
          country: '',
          genres: []
        },


      ],
    }
  },


  methods: {
    deleteMovie(movieToRemove) {
      this.movies = this.movies.filter(m => m !== movieToRemove);
    },
    addMovieToList(movie) {
      this.movies.push(movie);
    },
    hideAddBlock() {
      return this.addMovie = false;
    },
    showAddBlock() {
      return this.addMovie = true;
    },
    filterMoviesByTitle(e) {
      this.movieTitleFilter = e;
    },
    filterByFromInterval(e) {
      this.fromInterval = e;
    },
    filterByToInterval(e) {
      this.toInterval = e;
    }
  }
}
</script>

<style>

</style>
