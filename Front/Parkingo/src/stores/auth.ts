import { defineStore } from 'pinia'

type Role = 'driver' | 'operator' | 'admin' | null

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: '' as string,
    role: null as Role,
    phone: '' as string,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    setAuth(token: string, role: Role, phone: string) {
      this.token = token
      this.role = role
      this.phone = phone
      localStorage.setItem('sp_token', token)
      localStorage.setItem('sp_role', role || '')
      localStorage.setItem('sp_phone', phone || '')
    },
    loadAuth() {
      this.token = localStorage.getItem('sp_token') || ''
      this.role = (localStorage.getItem('sp_role') as Role) || null
      this.phone = localStorage.getItem('sp_phone') || ''
    },
    logout() {
      this.token = ''
      this.role = null
      this.phone = ''
      localStorage.removeItem('sp_token')
      localStorage.removeItem('sp_role')
      localStorage.removeItem('sp_phone')
    },
  },
})
