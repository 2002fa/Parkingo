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
                 <img src="@/assets/icons/uadmin.svg" alt="Admin Users" class="menu-icon" />
                <span>ادمین‌ها و اپراتورها</span>
              </router-link>
            </li>

            <!-- تنظیم شیفت‌ها -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/operators-shift') }">
              <router-link to="/dashboard/operators-shift">
                 <img src="@/assets/icons/Group.svg" alt="Shift Settings" class="menu-icon" />
                <span>تنظیم شیفت‌ها</span>
              </router-link>
            </li>

            <!-- آمار و گزارش ها -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/amar') }">
              <router-link to="/dashboard/amar">
                 <img src="@/assets/icons/stats.svg" alt="Statistics" class="menu-icon" />
                <span>آمار و گزارش‌ها</span>
              </router-link>
            </li>

            <!-- پارکینگ ها -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/parkings') }">
              <router-link to="/dashboard/parkings">
                 <img src="@/assets/icons/parkings.svg" alt="Parkings" class="menu-icon" />
                <span>پارکینگ‌ها</span>
              </router-link>
            </li>
          </template>

          <!-- منوهای مخصوص اپراتور -->
          <template v-if="userRole === 'operator'">
            <!-- پنل اپراتور -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard/panel') }">
              <router-link to="/dashboard/panel">
                 <img src="@/assets/icons/admin-panel.svg" alt="Operator Panel" class="menu-icon" />
                <span>پنل اپراتور</span>
              </router-link>
            </li>

            <!-- پارکینگ -->
            <li :class="{ 'is-active-link': isLinkActive('/dashboard') }">
              <router-link to="/dashboard">
                 <img src="@/assets/icons/parkings.svg" alt="Parking" class="menu-icon" />
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
        <!-- <button @click="emitLogout">
          <img src="@/assets/icons/logout.svg" alt="Logout" class="menu-icon" />
          <span>خروج</span>
        </button> -->

        <button @click="logout">
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
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

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
const router = useRouter();
const auth = useAuthStore();

const props = withDefaults(defineProps<Props>(), {
  isOpen: true,
  userRole: 'operator'
});

const emit = defineEmits<Emits>();

const isLinkActive = (path: string): boolean => {
  return route.path === path;
};

// const emitLogout = (): void => {
//   emit('logout');
// };

const emitToggleSidebar = (): void => {
  emit('update:is-open', !props.isOpen);
};

function logout() {
  auth.clearAuth()
  router.push({ name: 'home' })
}
</script>

<style scoped>
.sidebar {
  background: linear-gradient(#122E3B 0%, #2C779B 25%, #3DA8DB 49%, #2F81A8 75%,#215A76 99%, #0277bd 100%);
  color: white;
  padding: 0;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  position: fixed;
  height: 100%;
  top: 0;
  right: 0;
  width: 220px;
  transition: transform 0.3s ease-in-out;
  z-index: 101;
  direction: rtl;
  font-size: 13px; /* کاهش اندازه فونت کلی */
}

.sidebar.is-open {
  transform: translateX(0);
}

.sidebar.is-closed {
  transform: translateX(calc(220px - 50px)); /* کاهش عرض در حالت بسته */
  width: 50px;
}

.sidebar-toggle-area {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 50px; /* کاهش عرض */
  background: linear-gradient(#122E3B 0%, #2C779B 25%, #3DA8DB 49%, #2F81A8 75%,#215A76 99%, #0277bd 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 15px; /* کاهش padding */
  box-sizing: border-box;
  z-index: 102;
}

.strip-toggle-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  margin-top: 15px; /* کاهش margin */
  color: white;
  font-size: 18px; /* کاهش اندازه آیکون */
}

.strip-icon {
  width: 18px; /* کاهش اندازه آیکون */
  height: 18px;
}

.sidebar-content {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  overflow-y: auto;
  padding-left: 50px; /* کاهش padding */
  padding-right: 15px; /* کاهش padding */
  box-sizing: border-box;
}

.user-profile {
  display: flex;
  align-items: center;
  padding: 12px 0; /* کاهش padding */
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 15px; /* کاهش margin */
  padding-left: 8px; /* کاهش padding */
}

.profile-icon {
  font-size: 32px; /* کاهش اندازه آیکون */
  margin-left: 12px; /* کاهش margin */
  color: rgba(255, 255, 255, 0.9);
}

.username {
  font-size: 14px; /* کاهش اندازه فونت */
  font-weight: bold;
}

.sidebar-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar-nav li {
  margin-bottom: 4px; /* کاهش margin */
  position: relative;
}

.sidebar-nav li a {
  display: flex;
  align-items: center;
  padding: 12px 0; /* کاهش padding */
  color: white;
  text-decoration: none;
  transition: background-color 0.2s ease;
  font-size: 13px; /* کاهش اندازه فونت */
  border-radius: 4px; /* اضافه کردن border-radius */
}

.sidebar-nav li a:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.sidebar-nav li.is-active-link a {
  /* background: linear-gradient(#122E3B 0%, #2C779B 25%, #3DA8DB 49%, #2F81A8 75%,#215A76 99%, #0277bd 100%); */
  border-right: 4px solid #66C9DA; /* کاهش ضخامت border */
}

.menu-icon {
  width: 18px; /* کاهش اندازه آیکون */
  height: 18px;
  margin-left: 12px; /* کاهش margin */
  font-size: 16px; /* کاهش اندازه آیکون */
  display: flex;
  justify-content: center;
  align-items: center;
}

.logout-section {
  margin-top: auto;
  padding: 15px 0; /* کاهش padding */
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.logout-section button {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px 0; /* کاهش padding */
  background-color: transparent;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 13px; /* کاهش اندازه فونت */
  transition: background-color 0.2s ease;
  border-radius: 4px; /* اضافه کردن border-radius */
}

.logout-section button:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.logout-section .menu-icon {
  margin-left: 8px; /* کاهش margin */
  margin-right: 0;
}
</style>