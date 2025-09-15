import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import Login from '@/pages/Login.vue'
import Register from '@/pages/Register.vue'
import ForgetPassword from '@/pages/Forget-password.vue'
import Dashboard from '@/pages/ParkingMonitoring.vue'
import Home from '@/pages/Home.vue'
import financialReports from '@/pages/FinancialReports.vue'
import QrDisplay from '@/pages/QrDisplay.vue'
import DriverRouting from '@/pages/Driver-routing.vue'
// import Notfound from '@/pages/Not-found.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/home' },
  { path: '/home', name: 'home', component: Home },
  { path: '/login', name: 'login', component: Login, meta: { hideLayout: true, guestOnly: true } },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: { hideLayout: true, guestOnly: true },
  },
  {
    path: '/forget-password',
    name: 'forgotPassword',
    component: ForgetPassword,
    meta: { hideLayout: true },
  },
  {
    path: '/financial-reports',
    name: 'financialReports',
    component: financialReports,
    meta: { requiresAuth: true },
  },

  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    meta: { hideLayout: true, guestOnly: true },
  },
  {
    path: '/qr/:slotId',
    name: 'qr',
    component: QrDisplay,
    props: true,
    meta: { hideLayout: true },
  },
  {
    path: '/Driver-routing',
    name: 'DriverRouting',
    component: DriverRouting,
    meta: { hideLayout: true, guestOnly: true },
  },
  // { path: '/:pathMatch(.*)*', name: 'NotFound', component: Notfound, meta: { hideLayout: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const forceLogin = localStorage.getItem('force_login') === '1'
  const token = forceLogin ? '' : localStorage.getItem('sp_token')

  if (to.meta.requiresAuth && !token) return { name: 'home' }
  // if (to.meta.guestOnly && token) return { name: 'dashboard' }
})

export default router
