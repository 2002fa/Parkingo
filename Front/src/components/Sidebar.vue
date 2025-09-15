<template>
  <aside :class="['sidebar', { 'is-open': isOpen, 'is-closed': !isOpen }]">
    <div class="sidebar-toggle-area">
      <button @click="emitToggleSidebar" class="strip-toggle-btn">
        <img v-if="!isOpen" src="@/assets/icons/hamburger.svg" alt="باز کردن منو" class="strip-icon" />
        <img v-else src="@/assets/icons/close-sidebar.svg" alt="بستن منو" class="strip-icon" />
      </button>
    </div>

    <div v-if="isOpen" class="sidebar-content">
      <div class="user-profile">
        <img src="@/assets/icons/user-profile.svg" alt="User Profile" class="profile-icon" />
        <span class="username">{{ userRole === 'admin' ? 'مدیر سیستم' : 'اپراتور' }}</span>
      </div>

      <nav class="sidebar-nav">
        <ul>
          <!-- صفحه اصلی -->
          <li :class="{ 'is-active-link': isLinkActive('/home') }">
            <router-link to="/home">
              <img src="@/assets/icons/home.svg" alt="Home" class="menu-icon" />
              <span>صفحه اصلی</span>
            </router-link>
          </li>

          <!-- منوهای مخصوص ادمین -->
          <template v-if="userRole === 'admin'">
            <!-- ادمین‌ها و اپراتورها -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/admins') }">
              <router-link to="/dashboard/admins">
                <img src="@/src/assets/icons/user-admin.svg" alt="Admin Users" class="menu-icon" />
                <span>ادمین‌ها و اپراتورها</span>
              </router-link>
            </li>

            <!-- تنظیم شیفت‌ها -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/operators-shift') }">
              <router-link to="/dashboard/operators-shift">
                <img src="@/src/assets/icons/Group.svg" alt="Shift Settings" class="menu-icon" />
                <span>تنظیم شیفت‌ها</span>
              </router-link>
            </li>

            <!-- آمار و گزارش ها -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/amar') }">
              <router-link to="/dashboard/amar">
                <img src="@/src/assets/icons/start-test.svg" alt="Statistics" class="menu-icon" />
                <span>آمار و گزارش ها</span>
              </router-link>
            </li>

            <!-- پارکینگ ها -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/parkings') }">
              <router-link to="/dashboard/parkings">
                <img src="@/src/assets/icons/Group.svg" alt="Parkings" class="menu-icon" />
                <span>پارکینگ ها</span>
              </router-link>
            </li>
          </template>

          <!-- منوهای مخصوص اپراتور -->
          <template v-if="userRole === 'operator'">
            <!-- پنل اپراتور -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/panel') }">
              <router-link to="/dashboard/panel">
                <img src="@/src/assets/icons/admin-panel.svg" alt="Operator Panel" class="menu-icon" />
                <span>پنل اپراتور</span>
              </router-link>
            </li>

            <!-- پارکینگ -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard') }">
              <router-link to="/dashboard">
                <img src="@/src/assets/icons/Group.svg" alt="Parking" class="menu-icon" />
                <span>پارکینگ</span>
              </router-link>
            </li>
          </template>

          <!-- تنظیمات (مشترک بین ادمین و اپراتور) -->
          <li :class="{ 'is-active-link': isLinkActive('/settings') }">
            <router-link to="/settings">
              <img src="@/assets/icons/settings.svg" alt="Settings" class="menu-icon" />
              <span>تنظیمات</span>
            </router-link>
          </li>
        </ul>
      </nav>

      <div class="logout-section">
        <button @click="emitLogout">
          <img src="@/assets/icons/logout.svg" alt="Logout" class="menu-icon" />
          <span>خروج</span>
        </button>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { computed, defineProps, defineEmits } from 'vue';
import { useRoute } from 'vue-router';

// تعریف نوع‌های TypeScript
type UserRole = 'admin' | 'operator' | null;

interface Props {
  isOpen: boolean;
  userRole: UserRole;
}

interface Emits {
  (e: 'update:is-open', value: boolean): void;
  (e: 'logout'): void;
}

const route = useRoute();

const props = withDefaults(defineProps<Props>(), {
  isOpen: false,
  userRole: null
});

const emit = defineEmits<Emits>();

const isLinkActive = (path: string): boolean => {
  return route.path === path;
};

const emitLogout = (): void => {
  emit('logout');
};

const emitToggleSidebar = (): void => {
  emit('update:is-open', !props.isOpen);
};
</script>

<style scoped>
.sidebar {
  background-color: #1e2a5a;
  color: white;
  padding: 0;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  position: fixed;
  height: 100%;
  top: 0;
  right: 0;
  width: 250px;
  transition: transform 0.3s ease-in-out;
  z-index: 101;
  direction: rtl;
}

.sidebar.is-open {
  transform: translateX(0);
}

.sidebar.is-closed {
  transform: translateX(calc(250px - 60px));
}

.sidebar-toggle-area {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 60px;
  background-color: #1e2a5a;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20px;
  box-sizing: border-box;
  z-index: 102;
}

.strip-toggle-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  margin-top: 20px;
}

.strip-icon {
  width: 30px;
  height: 30px;
}

.sidebar-content {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  overflow-y: auto;
  padding-left: 60px;
  padding-right: 20px;
  box-sizing: border-box;
}

.user-profile {
  display: flex;
  align-items: center;
  padding: 15px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 20px;
  padding-left: 10px;
}

.profile-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 5px;
  margin-left: 15px;
}

.username {
  font-size: 1.2em;
  font-weight: bold;
}

.sidebar-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar-nav li {
  margin-bottom: 5px;
  position: relative;
}

.sidebar-nav li a {
  display: flex;
  align-items: center;
  padding: 15px 0;
  color: white;
  text-decoration: none;
  transition: background-color 0.2s ease;
  font-size: 1.1em;
}

.sidebar-nav li a:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.sidebar-nav li.is-active-link a {
  background-color: #33427f;
  border-right: 5px solid #66C9DA;
}

.menu-icon {
  width: 24px;
  height: 24px;
  margin-left: 15px;
}

.notification-badge {
  background-color: #66C9DA;
  color: white;
  border-radius: 50%;
  padding: 2px 7px;
  font-size: 0.8em;
  margin-right: 10px;
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
}

.logout-section {
  margin-top: auto;
  padding: 20px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.logout-section button {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 15px 0;
  background-color: transparent;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 1.1em;
  transition: background-color 0.2s ease;
}

.logout-section button:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.logout-section .menu-icon {
  margin-left: 10px;
  margin-right: 0;
}
</style>