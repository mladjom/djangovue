<template>
  <div class="py-10">
    <h1 class="text-4xl font-bold text-gray-900 mb-4">Welcome to Our Website</h1>
    <ArticlesList />
  </div>
</template>

<script>
import ArticlesList from "@/components/articles/ArticlesList.vue";

export default {
  components: {
    ArticlesList,
  },
};
</script>
