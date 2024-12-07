<template>
    <nav class="text-sm text-gray-500 mb-4" aria-label="breadcrumb">
      <ol class="flex space-x-2">
        <!-- Home breadcrumb -->
        <li class="flex items-center">
          <router-link to="/" class="hover:underline flex items-center">
            <!-- Home Icon (you can replace this with any other icon or image) -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9l9-7 9 7v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z"></path>
              <path d="M9 22V12h6v10"></path>
            </svg>
          </router-link>
          <span class="mx-2">/</span>
        </li>
  
        <!-- Dynamic breadcrumbs -->
        <li v-for="(crumb, index) in breadcrumbs" :key="index" class="flex items-center">
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
  import { useRoute } from "vue-router";
  import { ref, watch } from "vue";
  
  export default {
    name: "Breadcrumbs",
    setup() {
      const route = useRoute();
      const breadcrumbs = ref([]);
  
      // Function to update breadcrumbs
      const updateBreadcrumbs = () => {
        breadcrumbs.value = [
  
          ...route.matched
            .map((match) => {
              // Get breadcrumb label from meta
              const label = match.meta.breadcrumb || match.name;
  
              // Return breadcrumb only if label exists
              return label ? {
                label,
                path: match.path !== route.path ? match.path : null,
              } : null;
            })
            .filter(Boolean), // Remove any null values (routes without valid breadcrumbs)
        ];
      };
  
      // Call it initially to set the breadcrumbs
      updateBreadcrumbs();
  
      // Watch for route changes and update breadcrumbs
      watch(route, updateBreadcrumbs);
  
      return { breadcrumbs };
    },
  };
  </script>
  