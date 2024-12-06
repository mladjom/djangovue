// src/router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import { routes } from './routes';

// Create the router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),  // Use web history mode for SPA
  routes,  // Pass the imported routes from routes.js
});

export default router;