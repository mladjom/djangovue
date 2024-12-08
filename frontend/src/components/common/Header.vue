<template>
  <header class="bg-gray-900 text-white fixed top-0 left-0 w-full z-50 shadow-lg">
    <div class="container mx-auto flex justify-between items-center p-4">
      <!-- Logo Section -->
      <div class="text-2xl font-bold">
        <router-link to="/" class="text-white hover:text-gray-400">
          djangovue
        </router-link>
      </div>

      <!-- Navigation Links -->
      <nav class="hidden lg:block">
        <ul class="flex space-x-8 text-lg">
          <li>
            <router-link to="/blog" class="hover:text-gray-400">blog</router-link>
          </li>
          <li><router-link to="/categories" class="hover:text-gray-400">
            categories</router-link></li>
          <li>
            <router-link to="/about" class="hover:text-gray-400">about</router-link>
          </li>
          <li>
            <router-link to="/contact" class="hover:text-gray-400">contact</router-link>
          </li>
        </ul>
      </nav>

      <!-- Mobile Menu Button -->
      <div class="lg:hidden">
        <button @click="toggleMenu" class="text-white">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            class="h-6 w-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            ></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div
      v-if="isMobileMenuOpen"
      class="lg:hidden bg-gray-800 text-white p-4 transition-all"
    >
      <ul>
        <li class="py-2">
          <router-link to="/" class="block">Home</router-link>
        </li>
        <li class="py-2">
          <router-link to="/about" class="block">About</router-link>
        </li>
        <li class="py-2">
          <router-link to="/contact" class="block">Contact</router-link>
        </li>
      </ul>
    </div>
  </header>
</template>

<script setup>
import { ref } from "vue";
import useCategories from "@/composables/useCategories";

const isMobileMenuOpen = ref(false);

const toggleMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};
</script>
