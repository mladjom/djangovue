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
import { computed, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import { GET_ARTICLE_BY_SLUG } from "@/graphql/queries";

export default {
  name: "ArticleView",
  setup() {
    const route = useRoute();
    const router = useRouter();
    const slug = route.params.slug;

    // Query the article by slug
    const { result, loading, error } = useQuery(GET_ARTICLE_BY_SLUG, { slug });

    const article = computed(() => result.value?.articleBySlug); // Access article data

    const formattedDate = computed(() =>
      article.value?.createdAt
        ? new Date(article.value.createdAt).toLocaleDateString()
        : "Unknown"
    );

    // Watch article and set page title
    watch(article, (newArticle) => {
      if (newArticle?.title) {
        document.title = `${newArticle.title} - DjangoVue Blog`; // Set the page title dynamically
        // Update breadcrumb dynamically when article data is loaded
        router.currentRoute.value.meta.breadcrumb = newArticle.title; // Update breadcrumb meta
      }
    });

    return { article, formattedDate, loading, error };
  },
};
</script>
