// src/composables/usePagination.js
import { ref, computed, watch } from "vue";

export function usePagination(result, fetchMore) {
  const articles = ref([]);
  const hasNextPage = computed(() => result.value?.allArticles?.pageInfo?.hasNextPage);
  const endCursor = computed(() => result.value?.allArticles?.pageInfo?.endCursor);

  watch(result, (newResult) => {
    if (newResult?.allArticles?.edges) {
      articles.value = newResult.allArticles.edges;
    }
  }, { immediate: true });

  const loadMore = () => {
    if (hasNextPage.value) {
      fetchMore({
        variables: {
          after: endCursor.value,
          first: 6,
        },
      }).then((response) => {
        const newArticles = response.data.allArticles.edges;
        articles.value = [...articles.value, ...newArticles];
      }).catch((err) => console.error("Error loading more articles:", err));
    }
  };

  return { articles, hasNextPage, loadMore };
}
