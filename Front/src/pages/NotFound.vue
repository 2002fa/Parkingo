<script setup lang="ts">
import { useRouter } from 'vue-router'
const router = useRouter()
</script>

<template>
  <div class="not-found" dir="rtl">
    <h1>صفحه پیدا نشد!</h1>
    <p>متاسفانه صفحه‌ای که درخواست کرده‌اید وجود ندارد.</p>
    <button @click="router.push({ name: 'dashboard' })">رفتن به داشبورد</button>
  </div>
</template>

<style scoped>
.not-found {
  text-align: center;
  padding: 64px 16px;
}
button {
  margin-top: 16px;
  padding: 8px 16px;
  border: 0;
  background: #0277bd;
  color: #fff;
  border-radius: 6px;
}
</style>
