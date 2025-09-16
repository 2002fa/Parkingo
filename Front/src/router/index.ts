// src/router/index.ts
import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// صفحات
import Login from '@/pages/Login.vue'
import Register from '@/pages/Register.vue'
import ForgetPassword from '@/pages/Forget-password.vue'
import Home from '@/pages/Home.vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import ParkingMonitoring from '@/pages/ParkingMonitoring.vue'
import FinancialReports from '@/pages/FinancialReports.vue'
import Parkings from '@/pages/Dashboard/Parkings.vue'
import AddParking from '@/pages/Dashboard/AddParking.vue'
import DetailsOfParking from '@/pages/Dashboard/DetailsOfParking.vue'
import OperatorsShift from '@/pages/Dashboard/OperatorsShift.vue'
import Admins from '@/pages/Dashboard/Admins.vue'
import AddAdmin from '@/pages/Dashboard/AddAdmin.vue'
import OperatorProfile from '@/pages/Dashboard/OperatorProfile.vue'
import financialReports from '@/pages/FinancialReports.vue'
import QrDisplay from '@/pages/QrDisplay.vue'
import DriverInfo from '@/pages/Driver-info.vue'
import DriverRouting from '@/pages/Driver-routing.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/home' },

  { path: '/home', name: 'home', component: Home },

  { path: '/login', name: 'login', component: Login, meta: { hideLayout: true, guestOnly: true } },
  { path: '/register', name: 'register', component: Register, meta: { hideLayout: true, guestOnly: true } },
  { path: '/forget-password', name: 'forgotPassword', component: ForgetPassword, meta: { hideLayout: true } },
  {
    path: '/financial-reports',
    name: 'financialReports',
    component: financialReports,
    meta: { requiresAuth: true },
  },
  {
    path: '/qr/:slotId',
    name: 'qr',
    component: QrDisplay,
    props: true,
    meta: { hideLayout: true },
  },
  {
    path: '/driver-info/:slotId?',
    name: 'DriverInfo',
    component: DriverInfo,
    props: true,
    meta: { hideLayout: true, guestOnly: true },
  },
  {
    path: '/driver-routing/:slotId?',
    name: 'DriverRouting',
    component: DriverRouting,
    props: true,
    meta: { hideLayout: true, guestOnly: true },
  },

  {
    path: '/dashboard',
    component: DashboardLayout,
    meta: { requiresAuth: true, hideFooter: true },
    children: [
      { path: '', name: 'dashboard', component: ParkingMonitoring },

      // گزارشات مالی فقط برای ادمین
      { path: 'financial-reports', name: 'financialReports', component: FinancialReports, meta: { roles: ['admin'] } },

      // مدیریت ادمین‌ها فقط برای ادمین
      { path: 'admins', component: Admins, meta: { roles: ['admin'] } },
      { path: 'add-admin', component: AddAdmin, meta: { roles: ['admin'] } },

      // پروفایل اپراتور برای اپراتور و ادمین
      { path: 'operator-profile', component: OperatorProfile, meta: { roles: ['operator', 'admin'] } },

      // مدیریت پارکینگ‌ها برای ادمین
      { path: 'parkings', name: 'parkings', component: Parkings, meta: { roles: ['admin'] } },
      { path: 'add-parking', name: 'add-parking', component: AddParking, meta: { roles: ['admin'] } },
      { path: 'details-of-parking', name: 'details-of-parking', component: DetailsOfParking, props: true, meta: { roles: ['admin'] } },

      // شیفت اپراتورها برای ادمین و اپراتور
      { path: 'operators-shift', name: 'operators-shift', component: OperatorsShift, meta: { roles: ['admin', 'operator'] } }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// گارد نقش و لاگین
router.beforeEach((to) => {
  const auth = useAuthStore()

  // نیاز به لاگین
  if (to.meta.requiresAuth && !auth.isLoggedIn) {
    return { name: 'login' }
  }

  // اگر نقش لازم تعریف شده باشه
  if (to.meta.roles) {
    const allowedRoles = to.meta.roles as string[]
    if (!allowedRoles.includes(auth.role)) {
      // اگه کاربر اجازه نداشت → بفرست به صفحه اصلی یا داشبورد
      return { name: 'home' }
    }
  }

  // فقط مهمان (login/register) → وقتی لاگین هست نذاره
  // if (to.meta.guestOnly && auth.isLoggedIn) {
  //   return { name: 'dashboard' }
  // }
})

export default router
