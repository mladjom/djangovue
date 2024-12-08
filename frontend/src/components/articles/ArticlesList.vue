<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-if="error">Error: {{ error.message }}</div>

    <ul v-if="!loading && !error && articles.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 container mx-auto">
      <ArticleCard v-for="article in articles" :key="article.id" :article="article" />
    </ul>

    <div v-if="!loading && !error && hasNextPage" class="mt-4 text-center">
      <button @click="loadMore" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">
        Load More
      </button>
    </div>
  </div>
</template>

<script>
import ArticleCard from "@/components/articles/ArticleCard.vue";
import useArticles from "@/composables/useArticles";

export default {
  name: "ArticlesList",
  components: { ArticleCard },
  setup() {
    // Use the composable for articles logic
    const { articles, loading, error, loadMore, hasNextPage } = useArticles();

    return { articles, loading, error, loadMore, hasNextPage };
  },
};
</script>
