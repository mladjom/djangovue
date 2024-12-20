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
          <!-- Categories Dropdown -->
          <li class="relative group">
            <span class="hover:text-gray-400 cursor-pointer flex items-center">
              Categories
              <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 h-4 w-4" fill="none" viewBox="0 0 24 24"
                stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
              </svg>
            </span>
            <ul
              class="absolute left-0 mt-2 bg-white text-gray-900 shadow-lg rounded hidden group-hover:block z-10 w-48">
              <li v-for="category in categories" :key="category.id" class="px-4 py-2 hover:bg-gray-100">
                <router-link :to="`/categories/${category.slug}`" class="block">
                  {{ category.name }}
                </router-link>
              </li>
              <li v-if="loading" class="px-4 py-2">Loading...</li>
              <li v-if="error" class="px-4 py-2 text-red-500">Error loading categories</li>
            </ul>
          </li>
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
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-6 w-6">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-if="isMobileMenuOpen" class="lg:hidden bg-gray-800 text-white p-4 transition-all">
      <ul>
        <li class="py-2">
          <router-link to="/blog" class="block">Blog</router-link>
        </li>
        <li>
          <span class="block font-semibold py-2">Categories</span>
          <ul>
            <li
              v-for="category in categories"
              :key="category.id"
              class="py-2"
            >
              <router-link :to="`/categories/${category.slug}`" class="block">
                {{ category.name }}
              </router-link>
            </li>
            <li v-if="loading" class="py-2">Loading...</li>
            <li v-if="error" class="py-2 text-red-500">Error loading categories</li>
          </ul>
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

// Fetch categories
const { categories, loading, error } = useCategories();

const isMobileMenuOpen = ref(false);

const toggleMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};
</script>
