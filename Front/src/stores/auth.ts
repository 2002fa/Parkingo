import { defineStore } from 'pinia'

function parseJwt(token = '') {
  try {
    const payload = token.split('.')[1]
    return JSON.parse(atob(payload))
  } catch (e) {
    return {}
  }
}

function safeParseUser() {
  try {
    const raw = localStorage.getItem('user')
    if (!raw || raw === 'undefined' || raw === 'null') return null
    return JSON.parse(raw)
  } catch (e) {
    return null
  }
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: safeParseUser()
  }),
  getters: {
    role: (state) => state.user?.role || (state.token ? parseJwt(state.token).role : null),
    isLoggedIn: (state) => !!(state.token && state.user)
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
      if (!this.token) return
      try {
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
      } catch (e) {
        this.clearAuth()
      }
    }
  }
})
