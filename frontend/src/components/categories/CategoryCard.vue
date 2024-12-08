<template>
    <div class="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
      <h2 class="text-xl font-semibold text-gray-800 mb-2">{{ category.name }}</h2>
      <p class="text-gray-600 text-sm mb-4">{{ category.description }}</p>
      <router-link
        :to="'/categories/' + category.id"
        class="text-blue-500 hover:underline text-sm"
      >
        View Category
      </router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: "CategoryCard",
    props: {
      category: {
        type: Object,
        required: true,
      },
    },
  };

  </script>
