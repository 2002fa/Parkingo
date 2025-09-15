// import { defineStore } from 'pinia'

// type Role = 'driver' | 'operator' | 'admin' | null

// export const useAuthStore = defineStore('auth', {
//   state: () => ({
//     token: '' as string,
//     role: null as Role,
//     phone: '' as string,
//   }),
//   getters: {
//     isAuthenticated: (state) => !!state.token,
//   },
//   actions: {
//     setAuth(token: string, role: Role, phone: string) {
//       this.token = token
//       this.role = role
//       this.phone = phone
//       localStorage.setItem('sp_token', token)
//       localStorage.setItem('sp_role', role || '')
//       localStorage.setItem('sp_phone', phone || '')
//     },
//     loadAuth() {
//       this.token = localStorage.getItem('sp_token') || ''
//       this.role = (localStorage.getItem('sp_role') as Role) || null
//       this.phone = localStorage.getItem('sp_phone') || ''
//     },
//     logout() {
//       this.token = ''
//       this.role = null
//       this.phone = ''
//       localStorage.removeItem('sp_token')
//       localStorage.removeItem('sp_role')
//       localStorage.removeItem('sp_phone')
//     },
//   },
// })

// src/stores/auth.js
import { defineStore } from 'pinia'

function parseJwt(token = '') {
  try {
    const payload = token.split('.')[1]
    return JSON.parse(atob(payload))
  } catch (e) { return {} }
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user') || 'null')
  }),
  getters: {
    role: (state) => state.user?.role || (state.token ? parseJwt(state.token).role : null),
    isLoggedIn: (state) => !!(state.token || state.user)
  },
  actions: {
    setAuth({ token, user }) {
      if (token) {
        this.token = token
        localStorage.setItem('token', token)
      }
      if (user) {
        this.user = user
        localStorage.setItem('user', JSON.stringify(user))
      }
    },
    clearAuth() {
      this.token = null
      this.user = null
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    },
    async fetchProfile() {
      // فرض: endpoint /api/me/ که اطلاعات کاربر شامل role و avatar را برمی‌گرداند
      if (!this.token) return
      const res = await fetch('/api/me/', {
        headers: { 'Authorization': `Bearer ${this.token}` }
      })
      if (res.ok) {
        const data = await res.json()
        this.user = data
        localStorage.setItem('user', JSON.stringify(data))
      } else {
        this.clearAuth()
      }
    }
  }
})

