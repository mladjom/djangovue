import { ref, watch } from "vue";

export default function usePagination(result, fetchMore) {
  const items = ref([]); // Holds the list of paginated items
  const hasNextPage = ref(false);
  const endCursor = ref("");

  // Watch the result and update state reactively
  watch(
    result,
    (newResult) => {
      if (newResult?.allArticles) {
        const { edges, pageInfo } = newResult.allArticles;

        // Append new items to the list
        items.value = [...items.value, ...edges.map((edge) => edge.node)];

        // Update pagination info
        hasNextPage.value = pageInfo.hasNextPage;
        endCursor.value = pageInfo.endCursor;
      }
    },
    { immediate: true } // Trigger on initial load
  );

  // Function to load more items
  const loadMore = async () => {
    if (hasNextPage.value) {
      try {
        const { data } = await fetchMore({
          variables: {
            first: 6, // Number of items to fetch
            after: endCursor.value, // Fetch after the last cursor
          },
        });

        if (data?.allArticles?.edges) {
          // Append new items to the list
          items.value = [
            ...items.value,
            ...data.allArticles.edges.map((edge) => edge.node),
          ];

          // Update pagination info
          hasNextPage.value = data.allArticles.pageInfo.hasNextPage;
          endCursor.value = data.allArticles.pageInfo.endCursor;
        }
      } catch (err) {
        console.error("Error loading more items:", err);
      }
    }
  };

  return { items, hasNextPage, loadMore };
}
