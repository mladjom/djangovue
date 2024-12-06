export const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue'),  // Lazy-load Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/About.vue'),  // Lazy-load About
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('@/views/Contact.vue'),  // Lazy-load Contact
  },
];