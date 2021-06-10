<template>


  <div class="container mx-auto flex justify-center mt-5 p-2 md:p-0 bg-white">
    <genres-editor v-if="isGenresEditorOpened" @back="isGenresEditorOpened = false" @get-genre="addGenreToGenres"
                   :item-genres="genres"/>
    <div v-if="!isGenresEditorOpened" class="w-full max-w-xs">
      <form class="bg-white shadow-md px-8 pt-6 pb-8 mb-4  shadow-lg">
        <div class="mb-4">

          <span class="block text-gray-700 text-sm font-bold mb-2">
            Name of movie:
          </span>
          <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              type="text" placeholder="Name" v-model="title">
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="year">
            Year of movie:
          </label>
          <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="year" type="text" placeholder="Year" v-model.number="year">
        </div>

        <div class="mb-4">

          <button @click="isGenresEditorOpened=true"
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  type="button">
            Add genres to movie
          </button>
        </div>

        <div class="mb-4 flex justify-between">
          <div class="block">
            <span class="text-gray-700 ">Country: </span>
            <select class="mt-2 " v-model="country">
              <option v-for="country in handledListOfCountries" :key="country"> {{ country }}</option>
            </select>
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

    <film-item :title="title" :year="year" :genres="genres" :country="country" :is-edit-mode="true"
               :is-favorite="isFavorite" @switch-to-favorite="switchToFavorite"/>

  </div>
</template>


<script>
import FilmItem from "./Film-item";
import GenresEditor from "./Genres-editor";
import APIs from "../API";

export default {
  name: "Films-editor",
  components: {GenresEditor, FilmItem},
  emits: {
    'back': null,
    'save-movie': null,
    'replace-movie': null,
  },

  props: {
    movieToEdit: {
      required: false,
      type: Object
    }
  },

  computed: {
    handledListOfCountries() {

      const countriesToReplace = new Map([
        ["Bolivia (Plurinational State of)", "Bolivia"],
        ["Congo (Democratic Republic of the)", "Congo"],
        ["Iran (Islamic Republic of)", "Iran"],
        ["Lao People's Democratic Republic", "Laos"],
        ["Syrian Arab Republic", "Syria"],
        ["Korea (Democratic People's Republic of)", "North Korea"],
        ["Korea (Republic of)", "South Korea"],
        ["Tanzania, United Republic of", "Tanzania"],
        ["United Arab Emirates", "UAE"],
        ["Korea (Republic of)", "South Korea"],
        ["United Kingdom of Great Britain and Northern Ireland", "UK"],
        ["United States of America", "USA"],
        ["Venezuela (Bolivarian Republic of)", "Venezuela"]
      ]);

      const filteredCountries = this.listOfCountries
          .filter(country => country.population > 5e6)
          .map(country => country.name)
          .filter(country => !countriesToReplace.has(country));

      filteredCountries.push(...countriesToReplace.values());

      return filteredCountries.sort();

    },
  },

  data() {
    return {
      title: this.movieToEdit.title ?? '',
      year: this.movieToEdit.year ?? new Date().getFullYear(),
      country: this.movieToEdit.country ?? 'USA',
      genres: this.movieToEdit.genres ?? [],
      isFavorite: this.movieToEdit.isFavorite ?? false,
      isGenresEditorOpened: false,
      listOfCountries: ['USA', 'UK', 'Russia'],
    }
  },

  methods: {

    async loadListOfCountries() {
      this.listOfCountries = await APIs.getListOfCountries();
    },

    switchToFavorite() {
      this.isFavorite = !this.isFavorite;
    },

    addGenreToGenres(color, title) {
      const genres = this.genres.map(item => item.title);

      if (genres.includes(title) || title === '') {
        return;
      }

      this.genres.push({title, color});
    },

    back() {

      this.$emit('back');
    },

    handleKey(event) {
      if (event.key === "Escape") {
        this.back();
      }
    },

    save() {

      const movie = {
        title: this.title,
        year: this.year,
        genres: this.genres,
        country: this.country,
        isFavorite: this.isFavorite,
      };

      // is edited

      if (Object.keys(this.movieToEdit).length !== 0) {

        this.$emit('replace-movie', this.movieToEdit, movie);
        return;
      }

      this.$emit('save-movie', movie)
      this.back();
    }
  },

  mounted() {
    this.loadListOfCountries();
    document.addEventListener('keydown', this.handleKey);
  },

  beforeUnmount() {
    document.removeEventListener('keydown', this.handleKey);
  },
}
</script>

<style scoped>

</style>