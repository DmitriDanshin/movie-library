<template>


  <div class="mx-auto flex justify-center items-center p-2 md:p-0 mt-6">
    <div class="grid gap-4" :class="showedArrows ? 'grid-cols-5' : 'grid-cols-3' ">
      <films-list-arrows :show-arrows="showedArrows" @prev="prevArrowClicked" @next="nextArrowClicked">

        <template v-slot:prev-arrow/>

        <template v-slot:default>

          <film-item v-for="movie in showedMovies" :title="movie.title" :year="movie.year" :genres="movie.genres"
                     :country="movie.country" @delete-movie="deleteMovie(movie)" @edit-movie="editMovie(movie)"
                     :is-edit-mode="false" :key="movie" :is-favorite="movie.isFavorite"
                     @switch-to-favorite="switchToFavorite(movie)"/>

        </template>

        <template v-slot:prev-next/>

      </films-list-arrows>

    </div>
  </div>

</template>

<script>

import FilmsListArrows from "./Films-list-arrows";
import FilmItem from "./Film-item";

export default {
  name: "Films-list",
  components: {FilmItem, FilmsListArrows},
  props: {

    movies: {
      type: Array,
      required: true
    },

    movieFavoriteFilter: {
      type: Boolean,
      required: false,
    },

    movieTitleFilter: {
      type: String,
      required: false,
    },

    toInterval: {
      type: Number,
      required: false,
    },

    fromInterval: {
      type: Number,
      required: false,
    },

  },
  computed: {

    filteredMovies() {

      return this.movies.filter((movie) => {

        const title = movie.title.toLowerCase(),
            filter = this.movieTitleFilter.toLowerCase();

        return title.includes(filter);

      }).filter((movie) => {

        const from = this.fromInterval,
            to = this.toInterval;

        return movie.year >= from && movie.year <= to;

      }).filter((movie) => {

        return this.movieFavoriteFilter ? movie.isFavorite : true;

      });

    },

    showedMovies() {
      return this.filteredMovies.slice(this.start, this.end);
    },

    showedArrows() {
      return this.filteredMovies.length > 3;
    }

  },
  emits: {
    'delete': null,
    'edit': null,
    'switch-to-favorite': null,
  },
  methods: {
    editMovie(movieToEdit) {
      this.$emit('edit', movieToEdit);
    },

    switchToFavorite(movie) {
      this.$emit('switch-to-favorite', movie);
    },

    deleteMovie(movieToDelete) {
      this.$emit('delete', movieToDelete);
    },

    prevArrowClicked() {

      if (this.start <= 0) {
        return;
      }

      this.start -= 3;
      this.end -= 3;

    },

    nextArrowClicked() {
      if (this.end >= this.filteredMovies.length) {
        return;
      }

      this.start += 3;
      this.end += 3;

    }
  },

  data() {
    return {
      start: 0,
      end: 3,

    }
  },

}
</script>

<style scoped>

</style>