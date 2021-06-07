<template>
  <div class="container mx-auto flex justify-center mt-5 p-2 md:p-0 bg-white">
    <div class="w-full max-w-xs">
      <form class="bg-white shadow-md px-8 pt-6 pb-8 mb-4  shadow-lg">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
            Name of movie:
          </label>
          <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="name" type="text" placeholder="Name" v-model="title">
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="year">
            Year of movie:
          </label>
          <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="year" type="text" placeholder="Year" v-model.number="year">
        </div>

        <div class="mb-4 flex justify-between">
          <div class="block">
            <span class="text-gray-700 ">Country: </span>
            <select class="mt-2 " v-model="country">
              <option>Russia</option>
              <option>USA</option>
              <option>UK</option>
            </select>
          </div>

          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="genre">
              Genres of movie:
            </label>
            <input
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="genre" type="text" placeholder="Genre" v-model="genre">
          </div>
        </div>


        <div class="flex items-center content-between mt-3">
          <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="button" @click="save" @keydown.enter="save">
            Save
          </button>
          <span @click.prevent="back"
                class="ml-5 inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800 cursor-pointer">
            Back
          </span>
        </div>
      </form>

    </div>
    <film-item :title="title" :year="year" :genres="genres" :country="country" :is-needed-delete-button="false"/>
  </div>
</template>


<script>
import FilmItem from "./Film-item";

export default {
  name: "Films-add",
  components: {FilmItem},
  emits: {
    'back': null,
    'save-movie': null
  },
  data() {
    return {
      title: '',
      year: new Date().getFullYear(),
      country: 'USA',
      genres: [],
      genre: '',

    }
  },
  methods: {
    addGenreFromInput() {
      this.genres.push(this.genre);
    },
    back() {
      this.$emit('back');
    },
    handleKey(event) {
      if (event.key === "Escape") {
        this.back();
      }
      if (event.key === "Enter" && this.genre.length !== 0) {
        this.addGenreFromInput();
        this.genre = '';
      }
    },
    save() {

      const movie = {
        title: this.title,
        year: this.year,
        genres: this.genres,
        country: this.country
      };

      this.$emit('save-movie', movie)
      this.back();
    }
  },
  mounted() {
    document.addEventListener('keydown', this.handleKey);
  },
  beforeUnmount() {
    document.removeEventListener('keydown', this.handleKey);
  },
}
</script>

<style scoped>

</style>