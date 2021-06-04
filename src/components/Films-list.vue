<template>


  <div class="mx-auto flex justify-center items-center p-2 md:p-0 mt-6">
    <div class="grid gap-4" :class="showedArrows ? 'grid-cols-5' : 'grid-cols-3' ">
      <films-list-arrows :show-arrows="showedArrows" @prev="prevArrowClicked" @next="nextArrowClicked">

        <template v-slot:prev-arrow/>

        <template v-slot:default>
          <div v-for="movie in showedMovies" :key="movie"
               class="item border border-gray-300 bg-white shadow-lg rounded-lg p-10">
            <img class="w-48 h-48 mx-auto" src="https://i.imgur.com/oX0hGJs.jpeg" alt="">
            <div class="description mt-5">
              <h3>Название фильма: {{ movie.title }} </h3>
              <h2>Год: {{ movie.year }} </h2>
              <h2>Страна: {{ movie.country }}</h2>
            </div>
          </div>
        </template>

        <template v-slot:prev-next/>

      </films-list-arrows>

    </div>
  </div>

</template>

<script>

import FilmsListArrows from "./Films-list-arrows";

export default {
  name: "Films-list",
  components: {FilmsListArrows},
  computed: {

    filteredMovies() {
      return this.movies.filter((m) => m);
    },

    showedMovies() {
      return this.filteredMovies.slice(this.start, this.end);
    },

    showedArrows() {
      return this.filteredMovies.length > 3;
    }

  },
  methods: {
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
      movies: [
        {
          title: '',
          year: 1,
          country: '',
        },
        {
          title: '',
          year: 2,
          country: '',
        },
        {
          title: '',
          year: 3,
          country: '',
        },
        {
          title: '',
          year: 4,
          country: '',
        },
        {
          title: '',
          year: 5,
          country: '',
        },
        {
          title: '',
          year: 6,
          country: '',
        },
        {
          title: '',
          year: 7,
          country: '',
        }, {
          title: '',
          year: 8,
          country: '',
        }, {
          title: '',
          year: 9,
          country: '',
        },


      ],
    }
  }

}
</script>

<style scoped>

</style>