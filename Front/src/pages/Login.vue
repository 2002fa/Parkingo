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
          <form v-if="step === 'creds'" @submit.prevent="submitLogin">
            <div class="input-group">
              <label for="emailOrUsername">ایمیل یا نام کاربری</label>
              <input
                v-model="emailOrUsername"
                autocomplete="username"
                id="emailOrUsername"
                type="text"
                placeholder="ایمیل یا نام کاربری خود را وارد کنید"
                required
                autofocus
              />
            </div>

            <div class="input-group">
              <label for="phone">شماره تلفن</label>
              <div class="phone-container">
                <input
                  v-model.trim="phone"
                  id="phone"
                  type="tel"
                  inputmode="numeric"
                  pattern="[0-9]*"
                  autocomplete="tel"
                  placeholder="شماره موبایل خود را وارد کنید"
                  required
                />
              </div>
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

            <div v-if="step === 'creds'" class="bottom-links">
              <p @click="$router.push({ name: 'forgotPassword' })" class="link-button">
                رمز عبور خود را فراموش کرده‌اید؟
              </p>
            </div>

            <button type="submit" :disabled="loading">ورود</button>
          </form>

          <!-- مرحله دوم: تایید کد -->
          <div v-else class="otp-stage">
            <h2>کد ارسال شده را وارد نمایید.</h2>

            <form @submit.prevent="submitOtp" class="otp-form">
              <div class="otp-boxes" dir="ltr">
                <input
                  v-for="(v, i) in 4"
                  :key="i"
                  ref="otpInputs"
                  type="text"
                  inputmode="numeric"
                  pattern="[0-9]*"
                  maxlength="1"
                  class="otp-input"
                  :value="otp[i]"
                  @input="onOtpInput($event, i)"
                  @keydown.backspace.prevent="onOtpBackspace(i)"
                  @paste.prevent="onOtpPaste($event)"
                />
              </div>

              <p v-if="otpError" class="otp-error">{{ otpError }}</p>

              <button type="submit" :disabled="verifying">
                {{ verifying ? 'در حال تأیید…' : 'تأیید' }}
              </button>

              <div class="bottom-links otp-actions">
                <button type="button" class="linklike" @click="backToCreds">
                  ویرایش اطلاعات
                </button>
                <button type="button" class="linklike" @click="resendOtp">ارسال مجدد کد</button>
              </div>
            </form>
          </div>

          <!-- <div class="divider">
            <div class="line"></div>
            <div class="has-acc">حساب کاربری ندارید؟</div>
          </div>

          <div class="bottom-links">
            <router-link :to="{ name: 'register' }">
              <button style="background-color: #215a75">ثبت نام</button>
            </router-link>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const emailOrUsername = ref('')
const phone = ref('')
const password = ref('')
const loading = ref(false)
const passwordVisible = ref(false) // وضعیت نمایش/مخفی بودن رمز
const router = useRouter()
const auth = useAuthStore()
const isValidPhone = (v: string) => /^(\+98|0)?9\d{9}$/.test(v.trim())

// مرحله‌ی ورود: 'creds' = اطلاعات کاربر، 'otp' = تایید کد
const step = ref<'creds' | 'otp'>('creds')
// وضعیت و مقادیر OTP
const otp = ref(['', '', '', '']) // چهار خانه
const otpInputs = ref<HTMLInputElement[]>([])
const otpError = ref('')
const verifying = ref(false)

// متد برای تغییر وضعیت نمایش رمز
function togglePasswordVisibility() {
  passwordVisible.value = !passwordVisible.value
}

// متد ورود
async function submitLogin() {
  // فعلاً مرحله‌ی اول فقط اعتبارسنجی فرمی ساده و رفتن به مرحله OTP
  if (!emailOrUsername.value || !phone.value || !password.value) return

  // چک صحت شماره موبایل
  if (!isValidPhone(phone.value)) {
    alert('شماره موبایل معتبر وارد کنید')
    return
  }
  loading.value = true
  // TODO: اگر خواستی در همین‌جا API ارسال OTP بزنی
  setTimeout(() => {
    loading.value = false
    step.value = 'otp' // نمایش صفحه دوم
    // فوکوس روی خانهٔ اول کد
    requestAnimationFrame(() => otpInputs.value[0]?.focus())
  }, 500)
}

// هدایت به صفحه ثبت نام
function goToRegister() {
  router.push({ name: 'register' })
}

// هدایت به صفحه فراموشی رمز عبور
function resetPassword() {
  router.push({ name: 'ForgotPassword' })
}

function backToCreds() {
  step.value = 'creds'
  otp.value = ['', '', '', '']
  otpError.value = ''
  passwordVisible.value = false
}

function onOtpInput(e: Event, idx: number) {
  const el = e.target as HTMLInputElement
  const val = el.value.replace(/\D/g, '') // فقط رقم
  otp.value[idx] = val.slice(-1) || ''
  if (otp.value[idx] && idx < 3) {
    otpInputs.value[idx + 1]?.focus()
  }
}

function onOtpBackspace(idx: number) {
  if (otp.value[idx]) {
    otp.value[idx] = ''
    return
  }
  if (idx > 0) {
    otpInputs.value[idx - 1]?.focus()
    otp.value[idx - 1] = ''
  }
}

function onOtpPaste(e: ClipboardEvent) {
  const text = e.clipboardData?.getData('text') || ''
  const digits = text.replace(/\D/g, '').slice(0, 4).split('')
  digits.forEach((d, i) => (otp.value[i] = d))
  const next = digits.length >= 4 ? 3 : digits.length
  otpInputs.value[next]?.focus()
}

async function submitOtp() {
  otpError.value = ''
  const code = otp.value.join('')
  if (!/^\d{4}$/.test(code)) {
    otpError.value = 'کد تایید باید ۴ رقم باشد.'
    return
  }
  verifying.value = true
  try {
    // TODO: اینجا به API تایید OTP وصل شو
    await new Promise((r) => setTimeout(r, 700))
    
    // شبیه‌سازی ورود موفق:
    const token = 'fake-token'
    const role = 'operator'
    auth.setAuth(token, role, phone.value)
    router.push({ name: 'dashboard' })
  } catch (e) {
    otpError.value = 'کد نامعتبر است. دوباره تلاش کنید.'
  } finally {
    verifying.value = false
  }
}

function resendOtp() {
  // TODO: درخواست ارسال مجدد کد به بک
  otp.value = ['', '', '', '']
  otpInputs.value[0]?.focus()
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
  min-height: 700px;
}

.left-side img {
  width: 55vw;
  height: 60vw;
  margin-left: -20px;
  max-width: 800px;
  max-height: 880px;
  z-index: 1;
}

.right-side {
  width: 60%;
  display: grid;
  grid-template-rows: auto 1fr;
  justify-items: center;
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

input::placeholder {
  text-align: right;
}

.divider {
  /* display: flex;  */
  align-items: center;
  justify-content: center;
  margin: 20px 0;
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
  margin-top: 10px;
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
  margin-bottom: 10px;
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
  margin-bottom: 10px;
}

.link-button:hover {
  text-decoration: underline;
}

.eye-icon {
  position: absolute;
  left: 15px;
  top: 30%;
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

.phone-container {
  position: relative;
}

/* ==== OTP Stage ==== */
.otp-stage {
  margin-top: 50px;
  direction: rtl;
}

.otp-stage h2 {
  text-align: center;
  font-size: 19px;
  font-weight: 900;
  color: #455a64;
  margin: 10px 0 20px;
}

.otp-form {
  max-width: 400px;
  margin: 30px auto;
}

.otp-boxes {
  display: flex;
  gap: 12px;
  justify-content: center;
  margin: 20px 0 8px;
  text-align: center;
}

.otp-input {
  width: 56px;
  height: 56px;
  text-align: center;
  align-items: center;
  justify-content: center;
  justify-self: center;
  font-size: 24px;
  border: 1px solid #ddd;
  border-radius: 12px;
  outline: none;
  padding: 1px;
  background: #fff;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.02);
}

.otp-input:focus {
  border-color: #207be3;
  box-shadow: 0 0 0 3px rgba(2, 119, 189, 0.08);
}

.otp-error {
  color: #c62828;
  text-align: center;
  margin: 6px 0 0;
}

.linklike {
  background: none;
  border: 0;
  padding: 0;
  cursor: pointer;
  color: #0277bd;
  width: 50%;
  margin: 50px 0 40px;
}

.linklike:hover {
  text-decoration: underline;
  background: none;
}

.otp-actions {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
}

@media (max-width: 1000px) {
  .left-side img {
    width: 450px;
    height: 500px;
    margin-top: 60px;
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
  .has-acc {
    font-size: 14px;
  }
  .otp-actions {
    gap: 10px;
  }
}
</style>
