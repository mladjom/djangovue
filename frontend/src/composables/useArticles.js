// src/composables/useArticles.js
import { useQuery } from "@vue/apollo-composable";
import { gql } from "graphql-tag";
import { ref, computed, watch } from "vue";

const GET_ARTICLES = gql`
  query GetArticles($first: Int, $after: String) {
    allArticles(first: $first, after: $after) {
      edges {
        node {
          id
          title
          content
          slug
        }
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
`;

export function useArticles(first = 5, after = null) {
    
    // Use Apollo composable to run the query
    const { result, loading, error, refetch } = useQuery(GET_ARTICLES, { 
        first, 
        after });
  
    // Define articles and pagination data as reactive properties
    const articles = computed(() => result.value?.allArticles.edges.map(edge => edge.node) || []);
    const pageInfo = computed(() => result.value?.allArticles.pageInfo || {});
  
    // Return the articles, loading, error, and page info
    return {
      articles,
      loading,
      error,
      pageInfo,
      refetch,
    };
  }
  