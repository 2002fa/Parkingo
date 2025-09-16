import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
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

const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/home' },

  { path: '/home', name: 'home', component: Home },

  { path: '/login', name: 'login', component: Login, meta: { hideLayout: true, guestOnly: true } },
  { path: '/register', name: 'register', component: Register, meta: { hideLayout: true, guestOnly: true } },
  { path: '/forget-password', name: 'forgotPassword', component: ForgetPassword, meta: { hideLayout: true } },
  {
    path: '/dashboard',
    component: DashboardLayout,
    meta: { requiresAuth: true, hideFooter: true },
    children: [
      { path: '', name: 'dashboard-home', component: ParkingMonitoring },
      { path: 'financial-reports', name: 'financialReports', component: FinancialReports },
      { path: 'admins', component: Admins },
      { path: 'add-admin', component: AddAdmin },
      { path: 'operator-profile', component: OperatorProfile },
      { path: 'parkings', name: 'parkings', component: Parkings },
      { path: 'add-parking', name: 'add-parking', component: AddParking },
      { path: 'details-of-parking', name: 'details-of-parking', component: DetailsOfParking, props: true },
      { path: 'operators-shift', name: 'operators-shift', component: OperatorsShift }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  // const forceLogin = localStorage.getItem('force_login') === '1'
  // const token = forceLogin ? '' : localStorage.getItem('sp_token')

  // if (to.meta.requiresAuth && !token) return { name: 'home' }
})

export default router
