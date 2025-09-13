// import { createRouter, createWebHistory } from 'vue-router'
// import Login from '@/pages/Login.vue'
// import Register from '@/pages/Register.vue'
// import ForgotPassword from '@/pages/Forget-password.vue'
// import Dashboard from '@/pages/Dashboard.vue'
// // import Notfound from '@/pages/Notfound.vue'

// const routes = [
//   // {
//   //   path: '/',
//   //   name: 'login',
//   //   component: Login,
//   // },
//   {
//     path: '/dashboard',
//     name: 'dashboard',
//     component: Dashboard,
//   },
//   {
//     path: '/',
//     name: 'login',
//     component: Login,
//     meta: { hideLayout: true },
//   },
//   {
//     path: '/register',
//     name: 'register',
//     component: Register,
//     meta: { hideLayout: true },
//   },
//   {
//     path: '/forgot-password',
//     name: 'forgotPassword',
//     component: ForgotPassword,
//     meta: { hideLayout: true },
//   },
//   {
//     path: '/dashboard',
//     name: 'dashboard',
//     component: Dashboard,
//   },

//   // {
//   //   path: '/:pathMatch(.*)*',
//   //   name: 'NotFound',
//   //   component: Notfound,
//   // },
// ]

// const router = createRouter({
//   history: createWebHistory(),
//   routes,
// })

// export default router

import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import Login from '@/pages/Login.vue'
import Register from '@/pages/Register.vue'
import ForgetPassword from '@/pages/Forget-password.vue'
import Dashboard from '@/pages/Dashboard.vue'
// import Notfound from '@/pages/NotFound.vue'

const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/login' },
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
  { path: '/dashboard', name: 'dashboard', component: Dashboard, meta: { requiresAuth: true } },
  // { path: '/:pathMatch(.*)*', name: 'NotFound', component: Notfound, meta: { hideLayout: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// نگهبان مسیر ساده بر اساس توکن لوکال‌استوریج
// router.beforeEach((to) => {
//   const token = localStorage.getItem('sp_token')
//   if (to.meta.requiresAuth && !token) {
//     return { name: 'login' }
//   }
//   if (to.meta.guestOnly && token) {
//     return { name: 'dashboard' }
//   }
// })

router.beforeEach((to) => {
  const forceLogin = localStorage.getItem('force_login') === '1'
  const token = forceLogin ? '' : localStorage.getItem('sp_token')

  if (to.meta.requiresAuth && !token) return { name: 'login' }
  if (to.meta.guestOnly && token) return { name: 'dashboard' }
})


export default router
