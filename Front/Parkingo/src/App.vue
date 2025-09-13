<!-- <script setup lang="ts">
import router from './router'
import Header from './components/layout/Header.vue'
import Footer from './components/layout/Footer.vue' -->

<!-- // export default {
//   components: {
//     Header,
//     Footer,
//   },
//   watch: {
//     $route(to) {
//       if (to.meta.hideLayout) {
//         document.body.classList.add('no-scroll')
//       } else {
//         document.body.classList.remove('no-scroll')
//       }
//     },
//   },
//   mounted() {
//     if (this.$route.meta.hideLayout) {
//       document.body.classList.add('no-scroll')
//     } else {
//       document.body.classList.remove('no-scroll')
//     }
//   },
// } -->
<!-- </script> -->

<!-- <template>
  <div id="app"> -->
    <!-- <Header v-if="!$route.meta.hideLayout" /> -->
    <!-- <router-view /> -->
    <!-- <Footer v-if="!$route.meta.hideLayout" /> -->
  <!-- </div>
</template> -->

<!-- <style src="./styles/main.css">
.no-scroll {
  overflow: hidden;
  height: 100vh;
}
</style> -->



<script setup lang="ts">
import { useRoute } from 'vue-router'
import Header from '@/components/layout/Header.vue'
import Footer from '@/components/layout/Footer.vue'
const route = useRoute()
</script>

<template>
  <div id="app">
    <Header v-if="!route.meta.hideLayout" />
    <router-view />
    <Footer v-if="!route.meta.hideLayout" />
  </div>
</template>

<style src="./styles/main.css"></style>
