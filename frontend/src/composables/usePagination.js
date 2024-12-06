// src/composables/usePagination.js
import { ref } from 'vue';

export function usePagination() {
  // Pagination state
  const currentPage = ref(1);
  const hasNextPage = ref(false);
  const loading = ref(false);
  const afterCursor = ref(null);

  // Load more function to fetch the next set of articles
  const loadMore = () => {
    if (loading.value || !hasNextPage.value) return;

    loading.value = true;
    currentPage.value += 1;

    // Update afterCursor to fetch the next page
    afterCursor.value = afterCursor.value;

    loading.value = false;
  };

  return {
    currentPage,
    hasNextPage,
    loading,
    afterCursor,
    loadMore,
  };
}