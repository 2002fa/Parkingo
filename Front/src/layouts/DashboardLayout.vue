<template>
  <div class="flex flex-col min-h-screen">
    <Header @toggleSidebar="sidebarOpen = !sidebarOpen" />
    <Sidebar :isOpen="sidebarOpen" />
    <main class="flex-1 p-6 bg-gray-50 mt-[15px]">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Header from '@/components/DashboardHeader.vue'
import Sidebar from '@/components/Sidebar.vue'

const sidebarOpen = ref(false)
</script>
