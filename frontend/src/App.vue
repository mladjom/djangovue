<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div class="bg-gray-100 min-h-screen">
    <!-- Header -->
    <Header />

    <!-- Main Content -->
    <main class="pt-16 container mx-auto px-4">
      <router-view />
    </main>
  </div>
</template>

<script>
import Header from './components/Header.vue';

export default {
  name: 'App',
  components: {
    Header,
  },
};
</script>
