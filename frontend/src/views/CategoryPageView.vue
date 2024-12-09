<template>
    <div>
        <h1>Category: {{ categoryName }}</h1>
        <ArticlesList :slug="slug" />
    </div>
</template>

<script>
import { useRoute } from 'vue-router';
import ArticlesList from "@/components/articles/ArticlesList.vue";

export default {
    name: 'CategoryPageView',
    components: {
        ArticlesList, // Register the component
    },
    setup() {
        const route = useRoute();
        const slug = route.params.slug;

        return {
            slug,
            categoryName: slug.replace('-', ' ').toUpperCase(),
        };
    },
};
</script>