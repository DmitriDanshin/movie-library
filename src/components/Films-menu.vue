<template>

  <div class="container mx-auto flex justify-center items-center p-2 md:p-0 ">
    <div class="border border-gray-300 p-6 grid grid-cols-1 gap-6 bg-white shadow-lg rounded-lg relative">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="grid grid-cols-1 gap-2 border border-gray-200 p-2 rounded">
          <div class="flex border rounded bg-gray-300 items-center p-2 ">
            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="search"
                 class="fill-current text-gray-800 mr-2 w-5 svg-inline--fa fa-search fa-w-16" role="img"
                 xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
              <path fill="currentColor"
                    d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"></path>
            </svg>
            <input type="text" placeholder="Enter text here..." v-model="movieTitleFilter"
                   class="bg-gray-300 max-w-full focus:outline-none text-gray-700"/>
          </div>
        </div>

        <div class="grid grid-cols-1 gap-2 rounded">
          <button class=" rounded-md bg-gray-800 text-white">Add</button>
        </div>
        <div class="grid grid-cols-1 gap-2  p-2 rounded">
          Year:
          <input type="text" placeholder="From"
                 class="bg-gray-300 max-w-full focus:outline-none text-gray-700 pl-4" v-model.number="fromInterval"/>
          <input type="text" placeholder="To"
                 class="bg-gray-300 max-w-full focus:outline-none text-gray-700  pl-4" v-model.number="toInterval"/>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: "Films-menu",
  data() {
    return {
      movieTitleFilter: '',
      fromInterval: 0,
      toInterval: new Date().getFullYear(),
    }
  },

  emits: {
    "movie-title-filtered": null,
    "from-interval": null,
    "to-interval": null,

  },

  watch: {
    movieTitleFilter() {
      this.$emit('movie-title-filtered', this.movieTitleFilter);
    },
    fromInterval() {
      this.$emit('from-interval', this.fromInterval);
    },
    toInterval() {
      this.$emit('to-interval', this.toInterval);
    }
  }
}
</script>

<style scoped>

</style>