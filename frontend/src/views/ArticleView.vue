<template>
  <div>
    <div v-if="loading" class="animate-pulse space-y-4">
      <div class="h-8 bg-gray-300 rounded"></div>
      <div class="h-4 bg-gray-300 rounded"></div>
      <div class="h-4 bg-gray-300 rounded"></div>
    </div>
    <div v-else-if="error" class="text-red-500">Error: {{ error.message }}</div>
    <div v-else>
      <!-- Article Content -->
      <h1 class="text-4xl font-bold mb-4">{{ article?.title }}</h1>
      <div class="text-gray-600 text-sm mb-6">
        <span>Published on: {{ formattedDate }}</span>
        <span v-if="article.category"> | Category: {{ article.category.name }}</span>
      </div>
      <div class="prose max-w-none" v-html="article?.content"></div>
      <div class="mt-8">
        <h3 class="text-lg font-semibold">Tags</h3>
        <ul class="flex space-x-2">
          <li v-for="tag in article?.tags || []" :key="tag.id" class="bg-gray-200 px-2 py-1 rounded">
            {{ tag.name }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { useQuery } from "@vue/apollo-composable";
import { computed } from "vue";
import { useRoute } from "vue-router";
import { GET_ARTICLE_BY_SLUG } from "@/graphql/queries";

export default {
  name: "ArticleView",
  setup() {
    const route = useRoute();
    const slug = route.params.slug;

    const { result, loading, error } = useQuery(GET_ARTICLE_BY_SLUG, { slug });

    const article = computed(() => result.value?.articleBySlug); // Correct data path
    const formattedDate = computed(() =>
      article.value?.createdAt
        ? new Date(article.value.createdAt).toLocaleDateString()
        : "Unknown"
    );

    return { article, formattedDate, loading, error };
  },
};
</script>