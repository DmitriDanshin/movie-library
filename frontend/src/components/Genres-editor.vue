<template>
  <div class="w-full max-w-xs">
    <form
      class="bg-white shadow-md px-8 pt-6 pb-8 mb-4 shadow-lg"
      @keydown.enter.prevent
    >
      <div class="mb-4">
        <span class="block text-gray-700 text-sm font-bold mb-2">
          Genres of movie:
        </span>
        <input
          v-model="title"
          @keydown.enter="getGenre(colorClass, title)"
          class="
            shadow
            appearance-none
            border
            rounded
            w-full
            py-2
            px-3
            text-gray-700
            leading-tight
            focus:outline-none focus:shadow-outline
          "
          type="text"
          placeholder="Genre"
        />

        <div
          :class="{ hidden: !filteredExamples.length }"
          class="
            h-8
            w-full
            bg-gray-300
            flex
            justify-start
            items-center
            shadow-lg
            rounded-sm
          "
        >
          <div
            v-for="example in filteredExamples"
            :key="example"
            :class="
              colorClass === 'bg-black' ? 'bg-black text-white' : colorClass
            "
            class="
              rounded-sm
              text-xs
              shadow-lg
              text-center
              p-1
              mx-0.5
              cursor-pointer
            "
            @click="getGenre(colorClass, example)"
          >
            {{ example }}
          </div>
        </div>
      </div>
      <span class="block text-gray-700 text-sm font-bold mb-2">
        Add color to genre:
      </span>
      <div class="border p-4 rounded">
        <colors-palette @get-color="getColor" />
      </div>
      <div class="flex items-center content-between mt-3">
        <button
          @click="getGenre(colorClass, title)"
          class="
            bg-blue-500
            hover:bg-blue-700
            text-white
            font-bold
            py-2
            px-4
            rounded
            focus:outline-none focus:shadow-outline
          "
          type="button"
        >
          Add
        </button>
        <span
          @click.prevent="back"
          class="
            ml-5
            inline-block
            align-baseline
            font-bold
            text-sm text-blue-500
            hover:text-blue-800
            cursor-pointer
          "
        >
          Back
        </span>
      </div>
    </form>
  </div>
</template>

<script>
import ColorsPalette from "./Colors-palette";

export default {
  name: "Genres-editor",
  components: { ColorsPalette },
  computed: {
    filteredExamples() {
      const genres = this.itemGenres.map((item) => item.title.toLowerCase());
      return this.listOfGenresExamples
        .filter((genre) => !genres.includes(genre.toLowerCase()))
        .filter((genres) => genres.includes(this.title.toLowerCase()))
        .slice(0, 4);
    },
  },
  data() {
    return {
      listOfGenresExamples: ["Action", "Horror", "Drama", "Comedy"],
      colorClass: "bg-green-500",
      title: "",
    };
  },
  props: {
    itemGenres: {
      type: Array,
      required: true,
    },
  },
  emits: {
    back: null,
    "get-genre": null,
  },
  methods: {
    back() {
      this.$emit("back");
    },

    getGenre(color, title) {
      this.title = "";
      this.$emit("get-genre", color, title);
    },

    getColor(color) {
      this.colorClass = color;
    },
  },
};
</script>

<style scoped></style>
