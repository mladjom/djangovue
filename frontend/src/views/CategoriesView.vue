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
import CategoryCard from "@/components/CategoryCard.vue"; // Import CategoryCard component
import useCategories from "@/composables/useCategories"; // Import your composable for categories

export default {
  name: "CategoriesView",
  components: {
    CategoryCard,
  },
  setup() {
    const { categories, loading, error } = useCategories();

    return { categories, loading, error };
  },
};
</script>