// src/router/routes.js
import DefaultLayout from "@/layouts/DefaultLayout.vue";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import BlogView from "@/views/BlogView.vue";
import ContactView from "@/views/ContactView.vue";
import ArticleView from "@/views/ArticleView.vue"; // Import the single article view
import CategoriesView from "@/views/CategoriesView.vue";

export const routes = [
  {
    path: "/",
    component: DefaultLayout,
    children: [
      {
        path: "",
        name: "home",
        component: HomeView,
        meta: {
          title: "Home - DjangoVue Blog",
          description: "Home description of the DjangoVue blog platform.",
        },

      },
      {
        path: "/categories",
        name: "categories",
        component: CategoriesView,
        meta: { breadcrumb: "Categories", title: "Categories",
          description: "Description Categories"
         },
      },
      {
        path: "about",
        name: "about",
        component: AboutView,
        meta: {
          title: "About Us - DjangoVue Blog",
          description: "Learn more about the DjangoVue blog platform and our team.",
          breadcrumb: "About Us"
        },
      },
      {
        path: "blog",
        name: "blog",
        component: BlogView,
        meta: {
          title: "Blog - DjangoVue Blog",
          description: "Blog Desc",
          breadcrumb: "Blog"
        },
      },
      {
        path: "contact",
        name: "contact",
        component: ContactView,
        meta: {
          title: "Contact - DjangoVue Blog",
          description: "Contact description the DjangoVue blog platform.",
          //breadcrumb: "Contact"
        },
       },
       {
        path: "articles/:slug", // Dynamic route for single articles
        name: "article",
        component: ArticleView,
        meta: { title: "Article", breadcrumb: "Article" },
      },
    ],
  },
];