<!-- src/views/Contact.vue -->
<template>
    <div class="py-10">
      <h1 class="text-3xl font-bold text-gray-900 mb-6">Contact Us</h1>
      <form class="space-y-4 max-w-md mx-auto bg-white shadow-md rounded-lg p-6">
        <div>
          <label for="name" class="block text-gray-700">Name</label>
          <input
            id="name"
            type="text"
            class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:ring-gray-300"
            placeholder="Your name"
          />
        </div>
        <div>
          <label for="email" class="block text-gray-700">Email</label>
          <input
            id="email"
            type="email"
            class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:ring-gray-300"
            placeholder="Your email"
          />
        </div>
        <div>
          <label for="message" class="block text-gray-700">Message</label>
          <textarea
            id="message"
            class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring focus:ring-gray-300"
            rows="4"
            placeholder="Your message"
          ></textarea>
        </div>
        <button
          type="submit"
          class="bg-gray-900 text-white rounded-md py-2 px-4 hover:bg-gray-700"
        >
          Submit
        </button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Contact',
  };
  </script>
  