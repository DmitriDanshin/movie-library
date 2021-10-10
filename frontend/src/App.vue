<template>
  <films-menu
    @movie-title-filtered="filterMoviesByTitle"
    @fromInterval="filterByFromInterval"
    @toInterval="filterByToInterval"
    @add-movie="showAddBlock"
    @movie-favorite-filtered="sortByFavorite"
  />

  <films-list
    v-if="!isMovieEditorOpened"
    :movieTitleFilter="movieTitleFilter"
    :fromInterval="fromInterval"
    :toInterval="toInterval"
    :movieToAdd="movieToAdd"
    :movies="movies"
    @delete="deleteMovie"
    @edit="editMovie"
    @switch-to-favorite="switchToFavorite"
    :movieFavoriteFilter="movieFavoriteFilter"
  />

  <films-editor
    v-if="isMovieEditorOpened"
    @back="hideAddBlock"
    @save-movie="addMovieToList"
    :movie-to-edit="movieToEdit"
    @replace-movie="replaceMovie"
  />
</template>

<script>
import FilmsList from "./components/Films-list";
import FilmsMenu from "./components/Films-menu";
import FilmsEditor from "./components/Films-editor";

export default {
  name: "App",
  components: { FilmsEditor, FilmsMenu, FilmsList },

  data() {
    return {
      movieTitleFilter: "",
      movieFavoriteFilter: false,
      fromInterval: 0,
      toInterval: new Date().getFullYear(),
      isMovieEditorOpened: false,
      movieToAdd: {},
      movieToEdit: {},
      movies: [],
    };
  },

  created() {
    const moviesList = localStorage.getItem("movies");
    if (moviesList) {
      this.movies = JSON.parse(moviesList);
    }
  },

  watch: {
    movies() {
      localStorage.setItem("movies", JSON.stringify(this.movies));
    },
  },

  methods: {
    sortByFavorite(mode) {
      this.movieFavoriteFilter = mode;
    },

    switchToFavorite(movieToFavorite) {
      const movieToSwitch = this.movies.find(
        (movie) => movie === movieToFavorite
      );
      movieToSwitch.isFavorite = !movieToFavorite.isFavorite;
      this.replaceMovie(movieToFavorite, movieToSwitch);
    },

    replaceMovie(target, replace) {
      const index = this.movies.indexOf(target);
      this.movies[index] = replace;
      this.movies = [...this.movies];

      this.hideAddBlock();
    },

    editMovie(movieToEdit) {
      this.movieToEdit = movieToEdit;
      this.showAddBlock();
    },

    deleteMovie(movieToRemove) {
      this.movies = this.movies.filter((m) => m !== movieToRemove);
    },

    addMovieToList(movie) {
      this.movies = [...this.movies, movie];
    },

    hideAddBlock() {
      this.movieToEdit = {};
      return (this.isMovieEditorOpened = false);
    },

    showAddBlock() {
      this.isMovieEditorOpened === true
        ? (this.isMovieEditorOpened = false)
        : (this.isMovieEditorOpened = true);
    },

    filterMoviesByTitle(filter) {
      this.movieTitleFilter = filter;
    },

    filterByFromInterval(filter) {
      this.fromInterval = filter;
    },

    filterByToInterval(filter) {
      this.toInterval = filter;
    },
  },
};
</script>

<style></style>
