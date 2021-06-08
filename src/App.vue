<template>

  <films-menu @movie-title-filtered='filterMoviesByTitle' @fromInterval="filterByFromInterval"
              @toInterval="filterByToInterval" @add-movie="showAddBlock"/>

  <films-list v-if="!addMovie" :movieTitleFilter="movieTitleFilter" :fromInterval="fromInterval"
              :toInterval="toInterval" :movieToAdd="movieToAdd" :movies="movies" @delete="deleteMovie"/>
  <films-editor v-if="addMovie" @back="hideAddBlock" @save-movie="addMovieToList"/>
</template>

<script>

/*
 TODO
    Add functionality to change slider to grid;
    Add functionality to edit cards;
    Add functionality to load country list using API;
    Add functionality to adding to important;
    Use localstorage;
    In Films-editor.vue add ability to edit genres;
*/

import FilmsList from "./components/Films-list";
import FilmsMenu from "./components/Films-menu";
import FilmsEditor from "./components/Films-editor";

export default {
  name: 'App',
  components: {FilmsEditor, FilmsMenu, FilmsList},
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
            {
              title: 'Action',
              color: 'bg-red-500'
            },
            {
              title: 'Action',
              color: 'bg-blue-500'
            },
          ]
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
      this.addMovie === true ?
          this.addMovie = false :
          this.addMovie = true;
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
