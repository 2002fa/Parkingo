<template>
  <header class="header">
    <!-- نوار اصلی هدر -->
    <div class="main-bar">
      <!-- سمت راست: متن پارکینگو + دکمه همبرگر -->
      <div class="right-section">
        <button 
          @click="$emit('toggle-sidebar')"
          aria-label="باز/بسته کردن منو"
          class="menu-button"
        >
          <!-- استفاده از آیکون همبرگر -->
          <svg class="hamburger-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M3 12H21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <path d="M3 6H21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            <path d="M3 18H21" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        <div class="logo-text">پارکینگو</div>
      </div>
      <div class="user-info">
        <div class="user-name">{{ user?.full_name || user?.username || 'کاربر' }}</div>
        <div class="user-role">
          {{ user?.role === 'admin' ? 'مدیر' : user?.role === 'operator' ? 'اپراتور' : '' }}
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// Define the events that this component can emit
const emit = defineEmits<{
  (e: 'toggle-sidebar'): void
}>()

// Mock user data - replace with real data from backend later
const user = ref({
  full_name: 'امین رضایی',
  username: 'admin',
  role: 'admin' as const
})

// Optional: You can add a method to handle profile click
const handleProfileClick = () => {
  console.log('Profile clicked')
}

// Optional: Loading state for future use
const isLoading = ref(false)
</script>

<style scoped>
/* استایل‌های اصلی */
.header {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* نوار اصلی هدر */
.main-bar {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 0.5rem 1rem;
  background: linear-gradient(90deg, #0277bd 0%, #6be2bc 100%);
  /* background: linear-gradient(90deg, #6be2bc 0%, #0277bd 100%); */
}

/* بخش سمت راست */
.right-section {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

/* دکمه منو */
.menu-button {
  padding: 0.5rem;
  border-radius: 0.5rem;
  transition: background-color 0.2s;
  border: none;
  background: transparent;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.menu-button:hover {
  background-color: #f3f4f6;
}

/* آیکون همبرگر */
.hamburger-icon {
  height: 1.5rem;
  width: 1.5rem;
  color: #4b5563;
}

/* متن لوگو */
.logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  user-select: none;
  color: #1f5970;
}

/* بخش سمت چپ */
.left-section {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.5rem;
}

/* بخش پروفایل */
.profile-section {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  direction: rtl;
}

/* کانتینر آواتار */
.avatar-container {
  position: relative;
}

/* تصویر آواتار */
.avatar-image {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* اطلاعات کاربر */
.user-info {
  font-size: 0.875rem;
  color: #374151;
  text-align: right;
}

.user-name {
  font-weight: 600;
  color: #b4ccd5;
}

.user-role {
  font-size: 0.75rem;
  color: #85cfba;
}

/* تصویر فریم هدر */
.frame-header {
  width: 400px;
  height: 80px;
}
</style>