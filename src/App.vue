<template>

  <films-menu @movie-title-filtered='filterMoviesByTitle' @fromInterval="filterByFromInterval"
              @toInterval="filterByToInterval"/>
  <films-list :movieTitleFilter="movieTitleFilter" :fromInterval="fromInterval" :toInterval="toInterval"/>

</template>

<script>


import FilmsList from "./components/Films-list";
import FilmsMenu from "./components/Films-menu";

export default {
  name: 'App',
  components: {FilmsMenu, FilmsList},
  data() {
    return {
      movieTitleFilter: '',
      fromInterval: 0,
      toInterval: new Date().getFullYear(),
    }
  },
  methods: {
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
