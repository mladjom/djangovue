// src/composables/useArticles.js
import { useQuery } from "@vue/apollo-composable";
import { GET_ARTICLES } from "@/graphql/queries";
import usePagination from "@/composables/usePagination";

export default function useArticles() {
  const { result, loading, error, fetchMore } = useQuery(GET_ARTICLES, {
    first: 6,
    after: "",
  });

  // Use pagination composable to manage pagination
  const { items: articles, hasNextPage, loadMore } = usePagination(result, fetchMore);

  return { articles, loading, error, loadMore, hasNextPage };
}
