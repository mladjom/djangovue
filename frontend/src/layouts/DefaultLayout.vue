<template>
    <div class="min-h-screen flex flex-col">
      <!-- Header -->
      <Header />
  
      <!-- Main Content -->
      <main class="flex-1 container mx-auto px-4 py-6 pt-20">
        <Breadcrumbs />
        <router-view />

      </main>
  
      <!-- Footer -->
      <Footer />
    </div>
  </template>
  
  <script setup>
  import Header from "@/components/common/Header.vue";
  import Breadcrumbs from "@/components/common/Breadcrumbs.vue";
  import Footer from "@/components/common/Footer.vue";
  </script>