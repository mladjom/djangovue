<template>
  <div>
    <!-- Show loading state -->
    <div v-if="loading">Loading...</div>

    <!-- Show error state -->
    <div v-if="error">Error: {{ error.message }}</div>

    <!-- Display articles once data is loaded -->
    <ul v-if="!loading && !error && articles.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 container mx-auto">
      <li
        v-for="article in articles"
        :key="article.node.id"
        class="bg-white shadow-md rounded-lg overflow-hidden hover:shadow-lg transition-shadow duration-300"
      >
        <div class="p-4">
          <!-- Article Title -->
          <h2 class="text-2xl font-semibold text-gray-900 mb-2">
            {{ article.node.title }}
          </h2>

          <!-- Article Excerpt -->
          <p class="text-gray-700 text-sm">
            {{ article.node.content }}
          </p>
        </div>
        <div class="bg-gray-100 px-4 py-2">
          <router-link
            :to="`/articles/${article.node.slug}`"
            class="text-gray-900 hover:text-gray-600 font-semibold"
          >
            Read more →
          </router-link>
        </div>
      </li>
    </ul>

    <!-- Load more button -->
    <div v-if="!loading && !error && hasNextPage" class="mt-4 text-center">
      <button @click="loadMoreArticles" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">
        Load More
      </button>
    </div>
  </div>
</template>

<script>
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

export default {
  name: "ArticlesList",
  setup() {
    const articles = ref([]); // Make articles a reactive ref
    const { result, loading, error, fetchMore } = useQuery(GET_ARTICLES, {
      first: 6,
      after: "", // Start with no cursor for pagination
    });

    // Reactive state for pagination info
    const hasNextPage = computed(() => result.value?.allArticles?.pageInfo?.hasNextPage);
    const endCursor = computed(() => result.value?.allArticles?.pageInfo?.endCursor);

    // Handle loading the articles
    watch(result, (newResult) => {
      if (newResult?.allArticles?.edges) {
        // Update articles when the query result changes
        articles.value = newResult.allArticles.edges;
      }
    }, { immediate: true }); // Immediately update when the query returns data

    const loadMoreArticles = () => {
      if (hasNextPage.value) {
        fetchMore({
          variables: {
            after: endCursor.value, // Use the cursor to fetch the next set of results
            first: 6,  // Number of articles to fetch
          },
        })
          .then((response) => {
            const newArticles = response.data.allArticles.edges;
            // Append the new articles to the existing articles
            articles.value = [...articles.value, ...newArticles];
            console.log("Loaded more articles", newArticles);
          })
          .catch((err) => {
            console.error("Error loading more articles:", err);
          });
      }
    };

    return {
      articles,
      loading,
      error,
      loadMoreArticles,
      hasNextPage,
    };
  },
};
</script>
