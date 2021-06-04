<template>

  <films-menu/>
  <films-list/>

</template>

<script>


import FilmsList from "./components/Films-list";
import FilmsMenu from "./components/Films-menu";

export default {
  name: 'App',
  components: {FilmsMenu, FilmsList}
}
</script>

<style>

</style>
