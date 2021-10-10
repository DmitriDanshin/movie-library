<template>
  <div class="flex justify-start">
    <div
      v-for="color in colors"
      :class="color"
      :key="color"
      @click="getColor(color)"
      class="h-3 w-3 mx-0.5 border border-gray-900 cursor-pointer"
    ></div>
  </div>
</template>

<script>
export default {
  name: "Genres-palette",
  data() {
    return {
      colors: [
        "bg-blue-500",
        "bg-red-500",
        "bg-purple-500",
        "bg-green-500",
        "bg-pink-500",
        "bg-yellow-500",
        "bg-gray-500",
        "bg-black",
      ],
    };
  },

  emits: {
    "get-color": null,
  },

  methods: {
    getColor(color) {
      this.$emit("get-color", color);
    },
  },
};
</script>

<style scoped></style>
