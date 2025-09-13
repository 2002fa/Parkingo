<template>
  <div class="login-page">
    <div class="left-side">
      <img src="@/assets/images/car_location.png" />
    </div>

    <div class="right-side">
      <div class="logo-part">
        <img src="@/assets/icons/parkingo-logo.png" />
      </div>

      <div class="login-container">
        <h1>به پارکینگو خوش آمدید!</h1>

        <div class="login-box">
          <form @submit.prevent="submitLogin">
            <div class="input-group">
              <label for="emailOrPhone">ایمیل یا شماره موبایل</label>
              <input
                v-model="emailOrPhone"
                autocomplete="username"
                id="emailOrPhone"
                type="text"
                placeholder="ایمیل یا شماره موبایل خود را وارد کنید"
                required
                autofocus
              />
            </div>

            <div class="input-group">
              <label for="password">رمز عبور</label>
              <div class="password-container">
                <input
                  v-model="password"
                  :type="passwordVisible ? 'text' : 'password'"
                  id="password"
                  autocomplete="current-password"
                  placeholder="رمز عبور خود را وارد کنید"
                  required
                />

                <button
                  type="button"
                  class="eye-icon"
                  @click="togglePasswordVisibility"
                  :aria-pressed="passwordVisible"
                  :aria-label="passwordVisible ? 'پنهان کردن رمز' : 'نمایش رمز'"
                >
                  <img v-if="!passwordVisible" src="@/assets/icons/eye.png" alt="Show Password" />
                  <img v-else src="@/assets/icons/hide-password.png" alt="Hide Password" />
                </button>
              </div>
            </div>

            <div class="bottom-links">
              <p @click="$router.push({ name: 'forgotPassword' })" class="link-button">
                رمز عبور خود را فراموش کرده‌اید؟
              </p>
            </div>

            <button type="submit" :disabled="loading">ورود</button>
          </form>

          <div class="divider">
            <!-- <div class="line" style="margin-left: 5px"></div>
            <div class="has-acc" style="font-size: 15px">حساب کاربری ندارید؟</div> -->

            <div class="line"></div>
            <div class="has-acc">حساب کاربری ندارید؟</div>
          </div>

          <div class="bottom-links">
            <router-link :to="{ name: 'register' }">
              <button style="background-color: #215a75">ثبت نام</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const emailOrPhone = ref('')
const password = ref('')
const loading = ref(false)
const passwordVisible = ref(false) // وضعیت نمایش/مخفی بودن رمز
const router = useRouter()
const auth = useAuthStore()

// متد برای تغییر وضعیت نمایش رمز
function togglePasswordVisibility() {
  passwordVisible.value = !passwordVisible.value
}

// متد ورود
async function submitLogin() {
  loading.value = true
  try {
    const token = 'fake-token' // از API توکن می‌گیریم
    const role = 'operator' // نقش را از API می‌گیریم
    auth.setAuth(token, role, emailOrPhone.value)

    router.push({ name: 'dashboard' }) // هدایت به صفحه داشبورد
  } catch (error) {
    console.error('Login failed', error)
  } finally {
    password.value = ''
    loading.value = false
  }
}

// هدایت به صفحه ثبت نام
function goToRegister() {
  router.push({ name: 'register' })
}

// هدایت به صفحه فراموشی رمز عبور
function resetPassword() {
  router.push({ name: 'ForgotPassword' })
}
</script>

<style scoped>
.login-page {
  width: 100%;
  max-width: 1500px;
  justify-self: center;
  height: fit-content;
  background-color: #f5f8fa;
  margin: 0px;
  display: flex;
  direction: ltr;
  overflow-x: hidden;
}

.left-side {
  height: 100%;
  width: 45%;
  background-color: #ddeef8;
  padding-top: 100px;
  min-height: 600px;
}

.left-side img {
  width: 55vw;
  height: 65vw;
  max-width: 800px;
  max-height: 880px;
  z-index: 1;
}

.right-side {
  width: 60%;
  height: fit-content;
  align-items: center;
  text-align: justify;
}

.logo-part {
  width: fit-content;
  height: fit-content;
  margin-left: 62%;
  margin-right: 20px;
  margin-top: 2%;
}

.logo-part img {
  width: 180px;
}

.login-container {
  margin-top: 30px;
  padding: 0px;
  justify-content: center;
  align-items: center;
  width: 100%;
  justify-self: center;
}

.login-box {
  width: 100%;
  max-width: 400px;
  margin: 40px auto;
  border-radius: 8px;
  direction: rtl;
  flex-direction: column;
}

h1 {
  text-align: center;
  font-size: 26px;
  font-weight: 800;
  color: #455a64;
  margin-bottom: 20px;
  margin-top: 0px;
  direction: rtl;
}

.input-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #455a64;
}

input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 16px;
  box-sizing: border-box;
  padding-right: 20px;
}

.divider {
  /* display: flex;  */
  align-items: center;
  justify-content: center;
  margin: 40px 0;
  text-align: center;
}

.line {
  z-index: 1;
  width: 100%;
  height: 2px;
  justify-self: center;
  align-items: center;
  text-align: center;
  background-color: #8a9295;
  margin-bottom: -10px;
}

.has-acc {
  z-index: 2;
  min-width: fit-content;
  font-size: 16px;
  margin: 0 12px;
  color: #6b7a85;
  text-align: center;
  justify-self: center;
  padding: 0 10px;
  background-color: #f5f8fa;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #0158ff;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
}

button:disabled {
  background-color: #ccc;
}

button:hover {
  background-color: #457ee8;
}

.bottom-links {
  margin-top: -10px;
  text-align: left;
  margin-bottom: 20px;
}

.Reg-btn {
  background-color: #215a75;
}

.Reg-btn:hover {
  background-color: #286987;
}

.bottom-links p {
  color: #0277bd;
  cursor: pointer;
}

.bottom-links p:hover {
  text-decoration: underline;
}

.link-button {
  display: inline-block;
  color: #0158ff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
  text-align: center;
  text-decoration: none;
  margin-bottom: 20px;
}

.link-button:hover {
  text-decoration: underline;
}

.eye-icon {
  position: absolute;
  left: 15px;
  top: 62%;
  transform: translateY(-50%);
  cursor: pointer;
  color: #0277bd;
  font-size: 16px;
  font-weight: bold;
  width: 25px;
  transform: translateY(-50%);
  background: transparent;
  border: 0;
  padding: 0;
}

.password-container {
  position: relative;
}

@media (max-width: 1000px) {
  .left-side img {
    width: 490px;
    height: 600px;
  }
  .left-side {
    height: 70vw;
  }
  .login-container {
    width: 70%;
  }
}
@media (max-width: 880px) {
  .left-side img {
    margin-left: -40px;
  }
  .bottom-links {
    text-align: center;
    font-size: 14px;
  }
  .logo-part {
    margin-left: 50%;
  }
}

@media (max-width: 800px) {
  .left-side img {
    margin-left: -60px;
  }
}

@media (max-width: 720px) {
  .left-side {
    display: none;
  }
  .right-side {
    width: 100%;
  }

  .logo-part {
    right: 20px;
  }
  .logo-part img {
    width: 130px;
  }
}
@media (max-width: 460px) {
  h1 {
    font-size: 23px;
  }
  .bottom-links {
    font-size: 14px;
    text-align: center;
  }
  .login-box {
    width: 100%;
  }
  .login-page {
    width: 100%;
  }
  .has-acc { font-size: 14px;}
}
</style>
