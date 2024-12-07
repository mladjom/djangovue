<template>
  <nav class="text-sm text-gray-500 mb-4" aria-label="breadcrumb">
    <ol class="flex space-x-2">
      <!-- Home Breadcrumb -->
      <li class="flex items-center">
        <router-link to="/" class="hover:underline flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 9l9-7 9 7v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z" />
            <path d="M9 22V12h6v10" />
          </svg>
        </router-link>
      </li>

      <!-- Dynamic Breadcrumb for Articles -->
      <li v-for="(crumb, index) in breadcrumbs" :key="index" class="flex items-center uppercase">
        <router-link v-if="crumb.path" :to="crumb.path" class="hover:underline">
          {{ crumb.label }}
        </router-link>
        <span v-else>{{ crumb.label }}</span>
        <span v-if="index < breadcrumbs.length - 1" class="mx-2">/</span>
      </li>
    </ol>
  </nav>
</template>

<script>
import { computed } from "vue";
import { useRoute } from "vue-router";

export default {
  name: "Breadcrumbs",
  setup() {
    const route = useRoute();

    // Create a computed property to generate breadcrumbs
    const breadcrumbs = computed(() => {
      return route.matched.map((match) => {
        let label = "";
        let path = match.path;
        let name = match.name;
        let breadcrumb = match.meta.breadcrumb;

    // If on the article page, prepend "Article"
    if (name === "article" && route.params.slug) {
      // Prepend "Article" breadcrumb
      if (route.path !== match.path) {
        return [
          {
            label: "Article",
            path: "/articles/",
          },
          {
            label: route.params.slug.replace(/-/g, " "), // Article title
            path: null,
          },
        ];
      } else {
        label = route.params.slug.replace(/-/g, " "); // Set the article title
        path = null;
      }
        } else if (breadcrumb) {
          label = breadcrumb;
        } else {
          label = name ? name : "";
        }

        return {
          label,
          path,

           };
        }).flat();
    });

    return { breadcrumbs };
  },
};
</script>
