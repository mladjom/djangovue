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
import { ref, watch, computed } from "vue";
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

    // Reactive state
    const articles = ref([]);
    const hasNextPage = ref(false);
    const endCursor = ref("");

    // Watch the result and update state
    watch(
      result,
      (newResult) => {
        if (newResult?.allArticles) {
          const { edges, pageInfo } = newResult.allArticles;

        // Append fetched articles
        articles.value = [...articles.value, ...edges.map((edge) => edge.node)]

          // Update pagination state
          hasNextPage.value = pageInfo.hasNextPage;
          endCursor.value = pageInfo.endCursor;
        }
      },
      { immediate: true }
    );


    const loadMore = async () => {
      if (hasNextPage.value) {
        try {
          const { data } = await fetchMore({
            variables: {
              first: 6,
              after: endCursor.value, // Use the updated cursor
            },
          });

          if (data?.allArticles?.edges) {
            // Append new articles to the list
            articles.value = [
              ...articles.value,
              ...data.allArticles.edges.map((edge) => edge.node),
            ];

            // Update pagination state
            hasNextPage.value = data.allArticles.pageInfo.hasNextPage;
            endCursor.value = data.allArticles.pageInfo.endCursor;
          }
        } catch (err) {
          console.error("Error fetching more articles:", err);
        }
      }
    };




    return { articles, loading, error, loadMore, hasNextPage };
    },
};
</script>
