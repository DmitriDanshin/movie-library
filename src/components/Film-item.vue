<template>
  <div class="item border border-gray-300 bg-white shadow-lg rounded-lg p-10">
    <img class="w-48 h-48 mx-auto" src="https://i.imgur.com/oX0hGJs.jpeg" alt="">

    <div class="flex justify-center mt-2">
      <button v-if="!isEditMode" class=" rounded-md bg-gray-800 text-white p-1" @click="handleDelete">Delete
      </button>
      <button v-if="!isEditMode" class="rounded-md bg-gray-800 text-white p-1 px-4 ml-2">Edit</button>
    </div>

    <div class="description mt-5">
      <h3>Name: {{ title }} </h3>
      <h2>Year: {{ year }} </h2>
      <h2>Country: {{ country }}</h2>
      <div class="grid grid-cols-3 gap-2 mt-4">
        <div v-for="genre in genres" :key="genre"
             :class="genre.color === 'bg-black' ? 'bg-black text-white' : genre.color" class="rounded-lg shadow-lg  text-center p-1 text-sm">
          {{ genre.title }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Film-item",
  emits: {
    'delete-movie': null,
  },
  methods: {
    handleDelete() {
      this.$emit('delete-movie');
    }
  },
  props: {
    isEditMode: {
      type: Boolean,
      required: true,
    },
    title: {
      type: String,
      required: true
    },
    country: {
      type: String,
      required: true,
    },

    year: {
      type: Number,
      required: true
    },
    genres: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

</style>