import { useQuery } from "@vue/apollo-composable";
import { GET_CATEGORIES } from "@/graphql/queries";
import { computed } from "vue";

export default function useCategories() {
  // Destructure the response from the query
  const { result, loading, error } = useQuery(GET_CATEGORIES);

  const categories = computed(() => result.value?.allCategories || []);

  console.log("Just result", result);
  return {
    categories,
    loading,
    error
  };
}
