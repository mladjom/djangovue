import DefaultLayout from "@/layouts/DefaultLayout.vue";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue";
import ContactView from "@/views/ContactView.vue";

export const routes = [
  {
    path: "/",
    component: DefaultLayout,
    children: [
      {
        path: "",
        //name: "home",
        component: HomeView,
        meta: {
          title: "Home - DjangoVue Blog",
          description: "Home description of the DjangoVue blog platform.",
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
        path: "contact",
        name: "contact",
        component: ContactView,
        meta: {
          title: "Contact - DjangoVue Blog",
          description: "Contact description the DjangoVue blog platform.",
          //breadcrumb: "Contact"
        },

      },
    ],
  },
];