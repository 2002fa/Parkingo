<template>
  <div class="forget-page">
    <div class="left-side">
      <img src="@/assets/images/car_location.png" />
    </div>

    <div class="right-side">
      <div class="logo-part">
        <img src="@/assets/icons/parkingo-logo.png" />
      </div>

      <div class="forget-container">
        <div class="forget-box">
          <!-- فرم ارسال رمز یکبار مصرف -->
          <form v-if="!codeSent" @submit.prevent="sendOtp">
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

            <button type="submit" :disabled="loading">ارسال رمز یکبار مصرف</button>
          </form>

          <!-- نمایش کد 4 رقمی بعد از ارسال رمز یکبار مصرف -->
          <div v-if="codeSent" class="otp-container">
            <h2>کد ارسال شده را وارد نمایید.</h2>
            <form @submit.prevent="verifyOtp">
              <input
                v-model.trim="otpCode"
                type="text"
                maxlength="4"
                inputmode="numeric"
                pattern="[0-9]*"
                placeholder="کد را وارد کنید"
                class="otp-input"
                required
                autofocus
              />
              <button type="submit" :disabled="loading">تایید کد</button>
            </form>
          </div>

          <!-- بخش حساب کاربری ندارید؟ و دکمه ثبت نام -->
          <div class="divider">
            <div class="line" style="margin-left: 5px"></div>
            <div class="has-acc" style="font-size: 15px">حساب کاربری ندارید؟</div>
            <div class="line" style="margin-right: 5px"></div>
          </div>

          <div class="bottom-links">
            <router-link :to="{ name: 'register' }">
              <button style="background-color: #215a75">ثبت نام</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- پاپ‌آپ موفقیت -->
    <!-- <transition name="fade" @after-leave="popupVisible = false">
      <div v-if="popupVisible" class="popup-success">
        <p>ورود با موفقیت انجام شد</p>
      </div>
    </transition> -->
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const emailOrPhone = ref('')
const otpCode = ref('')
const loading = ref(false)
const codeSent = ref(false) // وضعیت ارسال رمز یکبار مصرف
const popupVisible = ref(false) // وضعیت نمایش پاپ‌آپ
const router = useRouter()
const auth = useAuthStore()

// ارسال رمز یکبار مصرف (OTP)
async function sendOtp() {
  loading.value = true
  try {
    // شبیه‌سازی ارسال OTP
    setTimeout(() => {
      otpCode.value = ''
      codeSent.value = true
      loading.value = false
    }, 1000)
  } catch (error) {
    console.error('Error sending OTP', error)
    loading.value = false
  }
}

// تایید کد ۴ رقمی
async function verifyOtp() {
  const code = (otpCode.value || '').trim()
  if (!/^\d{4}$/.test(code)) {
    alert('کد تایید ۴ رقمی معتبر وارد کنید')
    return
  }
  loading.value = true
  try {
    // TODO: اینجا به API واقعی وصل شو و کد را اعتبارسنجی کن
    await new Promise((r) => setTimeout(r, 600))

    // شبیه‌سازی موفقیت: ساخت سشن
    const token = 'demo-token'
    const role: 'operator' = 'operator'
    const phone = (emailOrPhone.value || '').trim()
    auth.setAuth(token, role, phone) // ذخیره در Pinia + localStorage

    // اگر در روتِرِت route name = 'dashboard' است:
    router.push({ name: 'dashboard' })
    // اگر روتِ اختصاصی داری (مثلاً 'operator.dashboard')، از همین استفاده کن:
    // router.push({ name: 'operator.dashboard' })
  } catch (e) {
    alert('تأیید کد ناموفق بود. دوباره تلاش کنید.')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.forget-page {
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

.forget-container {
  margin-top: 60px;
  padding: 0px;
  justify-content: center;
  align-items: center;
  width: 100%;
  justify-self: center;
}

.forget-box {
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

h2 {
  text-align: center;
  font-size: 19px;
  font-weight: 900;
  color: #455a64;
  margin-bottom: 20px;
  margin-top: 0px;
  direction: rtl;
}

.input-group {
  margin-top: 80px;
  margin-bottom: 30px;
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

/* استایل برای کد تایید */
.otp-container {
  transition: transform 1s ease-in-out;
  transform: translateX(0); /* پیش‌فرض: نمایش */
}

.otp-container-enter-active,
.otp-container-leave-active {
  transition: transform 0.5s ease-in-out;
  margin-bottom: 50px;
}

.otp-container-enter,
.otp-container-leave-to {
  transform: translateX(100%); /* انیمیشن حرکت از راست به چپ */
}

/* استایل‌های دیگر */
.divider {
  display: flex;
  margin: 60px 0px 20px;
  width: 100%;
  justify-content: center;
  align-items: center;
}

.line {
  width: 30%;
  height: 2px;
  background-color: #8a9295;
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
  margin-top: 40px;
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

/* استایل برای پاپ‌آپ موفقیت */
.popup-success {
  background-color: #bed7e6;
  color: #215a75;
  padding: 15px;
  text-align: center;
  border-radius: 5px;
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: auto;
  max-width: 300px;
  height: fit-content;
  transition: opacity 2.2s ease-in-out;
  animation-delay: 1000ms;
}

.popup-success p {
  font-size: 18px;
}

/* ترنزیشن برای پاپ‌آپ */
.popup-success.fade-leave-active {
  opacity: 0;
}

@media (max-width: 1000px) {
  .left-side img {
    width: 490px;
    height: 600px;
    /* height: 70vw; */
  }
  .left-side {
    height: 70vw;
  }
  .forget-container {
    width: 70%;
  }
}
@media (max-width: 880px) {
  .left-side img {
    margin-left: -40px;
  }
  .divider {
    display: flex;
    align-items: center;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  .line {
    width: 25%;
  }
  .had-reg {
    font-size: 16px;
    text-align: center;
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
    margin-left: 60%;
  }
  .logo-part img {
    width: 130px;
  }
}
@media (max-width: 460px) {
  .divider {
    margin-top: 40px;
  }
  .line {
    width: 19%;
  }

  h1 {
    font-size: 23px;
  }

  .bottom-links {
    font-size: 14px;
    text-align: center;
  }

  .forget-box {
    width: 100%;
  }
  .forget-page {
    width: 100%;
  }
}
</style>
