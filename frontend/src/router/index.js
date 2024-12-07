// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import { routes } from './routes';
import { updateMeta } from "@/utils/meta";

// Create the router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),  // Use web history mode for SPA
  routes,  // Pass the imported routes from routes.js
});

// Global Navigation Guard to set page titles
router.beforeEach((to, from, next) => {
  // Update page title
  document.title = to.meta.title || "DjangoVue Blog"; // Fallback title

  // Update meta description
  updateMeta(to.meta.description || "Default description for DjangoVue Blog.");
  next();
});

export default router;