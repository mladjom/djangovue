<template>
  <CategoriesList />
</template>

<script>
import CategoriesList from "@/components/categories/CategoriesList.vue"; // Import CategoriesList component

export default {
  name: "CategoriesView",
  components: {
    CategoriesList,
  },
};
</script>