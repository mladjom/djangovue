<!-- src/components/ArticleCard.vue -->
<template>
    <li class="bg-white shadow-md rounded-lg overflow-hidden hover:shadow-lg transition-shadow duration-300">
      <div class="p-4">
        <h2 class="text-2xl font-semibold text-gray-900 mb-2">
          {{ article.title }}
        </h2>
        <p class="text-gray-700 text-sm">
          {{ article.content }}
        </p>
      </div>
      <div class="bg-gray-100 px-4 py-2">
        <router-link :to="`/articles/${article.slug}`" class="text-gray-900 hover:text-gray-600 font-semibold">
          Read more →
        </router-link>
      </div>
    </li>
  </template>
  
  <script>
  export default {
    name: "ArticleCard",
    props: {
      article: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  