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
        :key="article.id"
        class="bg-white shadow-md rounded-lg overflow-hidden hover:shadow-lg transition-shadow duration-300"
      >
        <div class="p-4">
          <!-- Article Title -->
          <h2 class="text-2xl font-semibold text-gray-900 mb-2">
            {{ article.title }}
          </h2>

          <!-- Article Excerpt -->
          <p class="text-gray-700 text-sm">
            {{ article.content }}
          </p>
        </div>
        <div class="bg-gray-100 px-4 py-2">
          <router-link
            :to="`/articles/${article.id}`"
            class="text-gray-900 hover:text-gray-600 font-semibold"
          >
            Read more →
          </router-link>
        </div>
      </li>
    </ul>

    <!-- Fallback message if no articles are available -->
    <div v-else>No articles available.</div>
  </div>
</template>

<script>
import { useQuery } from "@vue/apollo-composable";
import { gql } from "graphql-tag";
import { computed } from 'vue'; 

const GET_ARTICLES = gql`
  query GetArticles {
    allArticles {
      id
      title
      content
    }
  }
`;

export default {
  name: "ArticlesList",
  setup() {
    const { result, loading, error } = useQuery(GET_ARTICLES);

    // Log the result to see what data is returned
    console.log("Query Result:", result.value);

    // Use computed to make articles reactive
    const articles = computed(() => result.value?.allArticles || []);

    return {
      articles,
      loading,
      error,
    };
  },
};

</script>
