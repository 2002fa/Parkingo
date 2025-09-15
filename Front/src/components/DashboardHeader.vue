<!-- src/components/ui/Header.vue -->
<template>
  <header class="header">
    <!-- نوار رنگی نازک 15px -->
    <div class="color-bar"></div>

    <!-- نوار اصلی هدر -->
    <div class="main-bar">
      <!-- سمت راست: متن پارکینگو + دکمه همبرگر (RTL: ظاهر در سمت راست) -->
      <div class="right-section">
        <button @click="$emit('toggle-sidebar')"
                aria-label="باز/بسته کردن منو"
                class="menu-button">
          <!-- همبرگر آیکون -->
          <img src="@/assets/icons/.svg" class="hamburger-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"/>
          </img>
        </button>
        <div class="logo-text">پارکینگو</div>
      </div>

      <!-- سمت چپ: آواتار و اسم کاربر (RTL: سمت چپ نشان‌دهنده پروفایل) -->
      <div class="left-section">
        <div class="avatar-container">
          <!-- <img :src="user?.avatar || defaultAvatar" alt="avatar" class="avatar-image"/> -->
           <img src="@/assets/icons/default-avatar.png" alt="profile" class="avatar-image">
          <!-- اسم روی تصویر یا کنار آن -->
        </div>
        <div class="user-info">
          <div class="user-name">{{ user?.full_name || user?.username || 'کاربر' }}</div>
          <div class="user-role">{{ user?.role === 'admin' ? 'مدیر' : user?.role === 'operator' ? 'اپراتور' : '' }}</div>
        </div>
      </div>
    </div>
    <Footer v-if="!$route.meta.hideFooter" />
  </header>
</template>

<script setup>
  import { computed } from 'vue'
  import { useAuthStore } from '@/stores/auth'
  const auth = useAuthStore()
  const user = computed(() => auth.user)
  const defaultAvatar = '@/assets/icons/default-avatar.png' // مسیر دلخواه
</script>

<style scoped>
/* استایل‌های اصلی */
.header {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* نوار رنگی */
.color-bar {
  height: 15px;
  width: 100%;
  background: linear-gradient(to right, #1f5970, #2aa3c0, #3db0d1);
}

/* نوار اصلی هدر */
.main-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  background-color: transparent;
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
  border-radius: 0.25rem;
  transition: background-color 0.2s;
  border: none;
  background: transparent;
  cursor: pointer;
}

.menu-button:hover {
  background-color: #f3f4f6;
}

/* آیکون همبرگر */
.hamburger-icon {
  height: 1.5rem;
  width: 1.5rem;
}

/* متن لوگو */
.logo-text {
  font-size: 1.125rem;
  font-weight: 700;
  user-select: none;
}

/* بخش سمت چپ */
.left-section {
  display: flex;
  align-items: center;
  gap: 0.75rem;
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
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

/* اطلاعات کاربر */
.user-info {
  font-size: 0.875rem;
  color: #374151;
}

.user-name {
  font-weight: 500;
}

.user-role {
  font-size: 0.75rem;
  color: #9ca3af;
}
</style>