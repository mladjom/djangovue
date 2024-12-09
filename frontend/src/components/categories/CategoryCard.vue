<template>
  <div class="category-card">
    <router-link :to="{ name: 'CategoryPage', params: { slug: category.slug } }">
      <h2>{{ category.name }}</h2>
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
