<template>


  <div class="mx-auto flex justify-center items-center p-2 md:p-0 mt-6">
    <div class="grid gap-4" :class="showedArrows ? 'grid-cols-5' : 'grid-cols-3' ">
      <films-list-arrows :show-arrows="showedArrows" @prev="prevArrowClicked" @next="nextArrowClicked">

        <template v-slot:prev-arrow/>

        <template v-slot:default>
          <div v-for="movie in showedMovies" :key="movie"
               class="item border border-gray-300 bg-white shadow-lg rounded-lg p-10">
            <img class="w-48 h-48 mx-auto" src="https://i.imgur.com/oX0hGJs.jpeg" alt="">
            <div class="flex justify-center mt-2">
              <button class=" rounded-md bg-gray-800 text-white p-1" @click.stop="deleteMovie(movie)">Delete</button>
            </div>
            <div class="description mt-5">
              <h3>Название фильма: {{ movie.title }} </h3>
              <h2>Год: {{ movie.year }} </h2>
              <h2>Страна: {{ movie.country }}</h2>
              <div class="grid grid-cols-3 gap-2 mt-4">
                <div v-for="genre in movie.genres" :key="genre"
                     class="rounded-lg shadow-lg bg-blue-500 text-center p-1">
                  {{ genre }}
                </div>
              </div>


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
  props: {

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
    }
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

      });

    },

    showedMovies() {
      return this.filteredMovies.slice(this.start, this.end);
    },

    showedArrows() {
      return this.filteredMovies.length > 3;
    }

  },
  methods: {

    deleteMovie(movieToRemove) {
      this.movies = this.movies.filter(m => m !== movieToRemove);
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
        },


      ],
    }
  }

}
</script>

<style scoped>

</style>