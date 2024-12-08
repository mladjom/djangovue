<template>
    <div class="categories-container">
      <!-- Unordered List to maintain consistency -->
      <ul class="space-y-6">
        <li v-for="category in categories" :key="category.id">
          <CategoryCard :category="category" />
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import CategoryCard from "@/components/categories/CategoryCard.vue"; // Import CategoryCard component
  import useCategories from "@/composables/useCategories"; // Import the useCategories composable
  
  export default {
    name: "CategoriesList",
    components: {
      CategoryCard,
    },
    setup() {
      // Use the composable to fetch categories
      const { categories, loading, error } = useCategories();
  
      return {
        categories,
        loading,
        error,
      };
    },
  };
  </script>