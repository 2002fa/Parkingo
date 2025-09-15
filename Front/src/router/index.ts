import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import Login from '@/pages/Login.vue'
import Register from '@/pages/Register.vue'
import ForgetPassword from '@/pages/Forget-password.vue'
import Dashboard from '@/pages/ParkingMonitoring.vue'
import Home from '@/pages/Home.vue'
import financialReports from '@/pages/FinancialReports.vue'
import Parkings from '@/pages/Dashboard/Parkings.vue';
import AddParking from '@/pages/Dashboard/AddParking.vue';
import DetailsOfParking from '@/pages/Dashboard/DetailsOfParking.vue';
import OperatorsShift from '@/pages/Dashboard/OperatorsShift.vue';

// import Notfound from '@/pages/NotFound.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/home' },
  {
    path: '/home', name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: { hideLayout: true, guestOnly: true }
  },
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
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    meta: { hideLayout: true, guestOnly: true }
  },
  {
    path: "/dashboard/admins",
    component: () => import("@/pages/Dashboard/Admins.vue"),
    meta: { hideFooter: true },
  },
  {
    path: "/dashboard/add-admin",
    component: () => import("@/pages/Dashboard/AddAdmin.vue"),
    meta: { hideFooter: true }
  },
  {
    path: "/dashboard/operator-profile",
    component: () => import("@/pages/Dashboard/OperatorProfile.vue"),
    meta: { hideFooter: true }
  },
  {
    path: '/dashboard/parkings',
    name: 'parkings',
    component: Parkings,
    meta: { hideFooter: true }
  },
  {
    path: '/dashboard/add-parking',
    name: 'add-parking',
    component: AddParking,
    meta: { hideFooter: true }
  },
  {
    // path: '/dashboard/details-of-parking/:id',
    path: '/dashboard/details-of-parking',
    name: 'details-of-parking',
    component: DetailsOfParking,
    props: true,
    meta: { hideFooter: true }
  },
  {
    path: '/dashboard/operators-shift',
    name: 'operators-shift',
    component: OperatorsShift,
    props: true,
    meta: { hideFooter: true }
  }
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
