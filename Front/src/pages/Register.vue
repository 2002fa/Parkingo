<template>
  <div class="register-page" dir="rtl">
    <div class="left-side">
      <img src="@/assets/images/car_location.png" alt="car illustration" />
    </div>

    <div class="right-side">
      <div class="logo-part">
        <img src="@/assets/icons/parkingo-logo.png" alt="پارکینگو" />
      </div>

      <div class="register-container">
        <h1>حساب کاربری خود را بسازید.</h1>

        <form class="register-form" @submit.prevent="submitRegister" novalidate>
          <!-- ایمیل -->
          <div class="input-group">
            <label for="email">ایمیل</label>
            <input
              id="email"
              type="email"
              v-model.trim="email"
              autocomplete="email"
              placeholder="مثال: user@example.com"
              :class="{ invalid: email && !isValidEmail }"
              required
            />
            <small v-if="email && !isValidEmail" class="hint error">فرمت ایمیل معتبر نیست.</small>
          </div>

          <!-- موبایل -->
          <div class="input-group">
            <label for="phone">شماره موبایل</label>
            <input
              id="phone"
              type="tel"
              inputmode="numeric"
              pattern="[0-9]*"
              v-model.trim="phone"
              autocomplete="tel"
              placeholder="مثال: 09XXXXXXXXX یا +989XXXXXXXXX"
              :class="{ invalid: phone && !isValidPhone }"
              required
            />
            <small v-if="phone && !isValidPhone" class="hint error"
              >شماره موبایل معتبر وارد کنید.</small
            >
          </div>

          <!-- نام کاربری -->
          <div class="input-group">
            <label for="username">نام کاربری</label>
            <input
              id="username"
              type="text"
              v-model.trim="username"
              autocomplete="username"
              placeholder="حداقل ۳ کاراکتر"
              :class="{ invalid: username && !isValidUsername }"
              required
            />
            <small v-if="username && !isValidUsername" class="hint error">حداقل ۳ کاراکتر.</small>
          </div>

          <!-- رمز عبور -->
          <div class="input-group">
            <label for="password">رمز عبور</label>
            <div class="password-wrap">
              <input
                :type="showPwd ? 'text' : 'password'"
                id="password"
                v-model="password"
                autocomplete="new-password"
                placeholder="حداقل ۶ کاراکتر"
                :class="{ invalid: password && !isValidPassword }"
                required
              />
              <button
                type="button"
                class="eye-btn"
                @click="showPwd = !showPwd"
                :aria-pressed="showPwd"
                title="نمایش/مخفی‌سازی رمز"
                :aria-label="showPwd ? 'پنهان کردن رمز' : 'نمایش رمز'"
              >
                <img v-if="!showPwd" src="@/assets/icons/eye.png" alt="Show Password" />
                <img v-else src="@/assets/icons/hide-password.png" alt="Hide Password" />
              </button>
            </div>
            <small v-if="password && !isValidPassword" class="hint error">حداقل ۶ کاراکتر.</small>
          </div>

          <p v-if="formError" class="form-error">{{ formError }}</p>

          <button class="submit-btn" type="submit" :disabled="!canSubmit || submitting">
            {{ submitting ? 'در حال ارسال…' : 'ادامه' }}
          </button>

          <div class="divider">
            <div class="line"></div>
            <div class="had-reg">از قبل ثبت نام کرده‌اید؟</div>
          </div>

          <div class="bottom-links">
            <router-link :to="{ name: 'login' }">
              <button type="button" class="alt-btn">ورود</button>
            </router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const phone = ref('')
const username = ref('')
const password = ref('')
const submitting = ref(false)
const showPwd = ref(false)
const formError = ref('')

// ولیدیشن‌های ساده
const isValidEmail = computed(() => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim()))
const isValidPhone = computed(() => /^(\+98|0)?9\d{9}$/.test(phone.value.trim()))
const isValidUsername = computed(() => username.value.trim().length >= 3)
const isValidPassword = computed(() => password.value.length >= 6)

const canSubmit = computed(
  () => isValidEmail.value && isValidPhone.value && isValidUsername.value && isValidPassword.value,
)

async function submitRegister() {
  formError.value = ''
  if (!canSubmit.value) {
    formError.value = 'اطلاعات فرم را به‌درستی کامل کنید.'
    return
  }
  submitting.value = true
  try {
    // TODO: اتصال به API رجیستر
    await new Promise((r) => setTimeout(r, 800))
    // سناریو رایج: بعد از ساخت حساب → هدایت به لاگین
    router.push({ name: 'login' })
  } catch (e) {
    formError.value = 'ثبت‌نام ناموفق بود. لطفاً دوباره تلاش کنید.'
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>

.register-page {
  width: 100%;
  max-width: 1500px;
  justify-self: center;
  background-color: #f5f8fa;
  margin: 0;
  display: flex;
  direction: ltr;
  min-height: 600px;
  overflow-x: hidden;
}

.left-side {
  width: 45%;
  background-color: #ddeef8;
  padding-top: 100px;
  display: grid;
  place-items: start center;
  min-height: 750px;
}

.left-side img {
  width: 55vw;
  height: 65vw;
  max-width: 800px;
  max-height: 880px;
}

.right-side {
  width: 60%;
  align-items: center;
  text-align: justify;
  height: fit-content;
}

.logo-part {
  height: fit-content;
  width: fit-content;
  margin-left: 62%;
  margin-right: 20px;
  margin-top: 2%;
}

.logo-part img {
  width: 180px;
}


.register-container {
  margin-top: 30px;
  padding: 0px;
  justify-content: center;
  align-items: center;
  width: 100%;
  justify-self: center;
}

h1 {
  text-align: center;
  font-size: 26px;
  font-weight: 800;
  color: #455a64;
  margin-top: 0;
  direction: rtl;
  margin-bottom: 20px;
}


/* فرم و ورودی‌ها) */
.register-form {
  width: 100%;
  max-width: 420px;
  margin: 0 0 40px 20%;
  direction: rtl;
  justify-content: center;
  justify-self: center;
}

.input-group {
  margin: 18px 0;
}

label {
  display: block;
  margin-bottom: 6px;
  font-weight: 700;
  color: #455a64;
}

input {
  width: 100%;
  padding: 12px 10px;
  border: 1px solid #dcdfe3;
  border-radius: 10px;
  font-size: 15px;
  outline: none;
  background: #fff;
  transition:
    border-color 0.2s,
    box-shadow 0.2s;
  direction: rtl;
}

input:focus {
  border-color: #7bb8ff;
  box-shadow: 0 0 0 3px rgba(2, 119, 189, 0.08);
}
input.invalid {
  border-color: #e57373;
}
.hint {
  font-size: 12px;
  margin-top: 6px;
  display: inline-block;
}
.hint.error {
  color: #c62828;
}

.password-wrap {
  position: relative;
}
.eye-btn {
  position: absolute;
  left: 0px;
  top: 62%;
  transform: translateY(-50%);
  background: transparent;
  border: 0;
  padding: 0;
  cursor: pointer;
  font-size: 18px;
  font-weight: bold;
  color: #0277bd;
}

.form-error {
  color: #c62828;
  margin: 6px 0 2px;
}

/* دکمه‌ها */
.submit-btn,
.alt-btn {
  width: 100%;
  padding: 12px;
  border: 0;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 16px;
}
.submit-btn {
  background-color: #0158ff;
  color: #fff;
}
.submit-btn:hover {
  background-color: #457ee8;
}
.submit-btn:disabled {
  background-color: #c6d2f9;
  cursor: not-allowed;
}

.alt-btn {
  background-color: #215a75;
  color: #fff;
}
.alt-btn:hover {
  background-color: #286987;
}

/* دیوایدر و لینک‌ها */
.divider {
  align-items: center;
  justify-content: center;
  margin: 28px 0 6px;
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

.had-reg {
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

.bottom-links {
  text-align: left;
  margin-bottom: 24px;
}

@media (max-width: 1000px) {
  .left-side img {
    width: 490px;
    height: 600px;
  }
  .left-side {
    height: 70vw;
  }
  .register-container {
    width: 70%;
  }
}
@media (max-width: 880px) {
  .left-side img {
    margin-left: -40px;
  }
  .logo-part {
    margin-left: 50%;
  }
  .bottom-links {
    text-align: center;
    font-size: 14px;
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
    margin-left: 65%;
  }
  .logo-part img {
    width: 130px;
  }
  .register-form {
    margin: 0 auto;
    padding: 0 20px;
  }
}
@media (max-width: 460px) {
  .had-reg {
    font-size: 14px;
  }
  h1 {
    font-size: 23px;
    text-align: center;
  }
  .bottom-links {
    text-align: center;
    font-size: 14px;
  }
  .logo-part {
    margin-left: 58%;
  }
  .divider {
    margin-top: 40px;
  }
  .register-form {
    width: 100%;
  }
  .register-page {
    width: 100%;
  }
}
</style>
