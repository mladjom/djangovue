import './assets/tailwind.css'; // Import the Tailwind CSS file

import { createApp, provide, h } from "vue";
import { DefaultApolloClient } from "@vue/apollo-composable";
import App from "./App.vue";
import apolloClient from "./apollo";
import router from './router'

const app = createApp({
    setup() {
      provide(DefaultApolloClient, apolloClient); // Provide Apollo Client
    },
    render: () => h(App),
  });

app.use(router)

app.mount('#app')
