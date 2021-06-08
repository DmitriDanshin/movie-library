<template>

  <films-menu @movie-title-filtered='filterMoviesByTitle' @fromInterval="filterByFromInterval"
              @toInterval="filterByToInterval" @add-movie="showAddBlock"/>

  <films-list v-if="!isMovieEditorOpened" :movieTitleFilter="movieTitleFilter" :fromInterval="fromInterval"
              :toInterval="toInterval" :movieToAdd="movieToAdd" :movies="movies" @delete="deleteMovie"
              @edit="editMovie"/>

  <films-editor v-if="isMovieEditorOpened" @back="hideAddBlock" @save-movie="addMovieToList"
                :movie-to-edit="movieToEdit" @replace-movie="replaceMovie"/>
</template>

<script>

/*
 TODO
    Add functionality to change slider to grid;
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
      isMovieEditorOpened: false,
      movieToAdd: {},
      movieToEdit: {},

      movies: [
        {
          title: 'First',
          year: 1,
          country: 'USA',
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

    replaceMovie(movieToReplace) {
      this.deleteMovie(movieToReplace)
    },

    editMovie(movieToEdit) {
      this.movieToEdit = movieToEdit;
      this.showAddBlock();

    },

    deleteMovie(movieToRemove) {
      this.movies = this.movies.filter(m => m !== movieToRemove);
    },

    addMovieToList(movie) {
      this.movies.push(movie);
    },

    hideAddBlock() {
      this.movieToEdit = {};
      return this.isMovieEditorOpened = false;
    },

    showAddBlock() {
      this.isMovieEditorOpened === true ?
          this.isMovieEditorOpened = false :
          this.isMovieEditorOpened = true;
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
