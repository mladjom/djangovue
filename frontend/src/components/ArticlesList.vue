<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-if="error">Error: {{ error.message }}</div>

    <ul v-if="!loading && !error && articles.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 container mx-auto">
      <ArticleCard v-for="article in articles" :key="article.node.id" :article="article.node" />
    </ul>

    <div v-if="!loading && !error && hasNextPage" class="mt-4 text-center">
      <button @click="loadMore" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">
        Load More
      </button>
    </div>
  </div>
</template>

<script>
import { useQuery } from "@vue/apollo-composable";
import { GET_ARTICLES } from "@/graphql/queries";
import { usePagination } from "@/composables/usePagination";
import ArticleCard from "@/components/ArticleCard.vue";

export default {
  name: "ArticlesList",
  components: { ArticleCard },
  setup() {
    const { result, loading, error, fetchMore } = useQuery(GET_ARTICLES, {
      first: 6,
      after: "",
    });

    const { articles, hasNextPage, loadMore } = usePagination(result, fetchMore);

    return { articles, loading, error, loadMore, hasNextPage };
  },
};
</script>
