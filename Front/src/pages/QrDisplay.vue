<template>
  <div class="qr-wrap" dir="rtl">
    <div class="DriverRouting">
      <button
        class="btn btn-primary"
        @click="
          $router.push({
            name: 'DriverInfo',
            params: { slotId },
            query: { t: Date.now() },
          })
        "
      >
        مسیریابی
      </button>
    </div>

    <div class="brand">
      <img src="@/assets/icons/hero-logo.svg" alt="Parkingo" />
    </div>

    <div class="qr-card">
      <p class="title">
        کد ورود جایگاه: <b>{{ slotId }}</b>
      </p>

      <div class="qr-box" v-if="qrDataUrl">
        <img :src="qrDataUrl" alt="QR" />
      </div>
      <p v-else class="loading">در حال ساخت QR…</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import QRCode from 'qrcode' // ← نیاز به نصب پکیج

// اگر در روتر props: true گذاشتی:
const props = defineProps<{ slotId: string }>()
const slotId = props.slotId
// const selected = ref<string | null>(null)

const qrDataUrl = ref<string>('')

onMounted(async () => {
  // داده‌ای که می‌خواهی در QR قرار بگیرد
  const payload = JSON.stringify({ slotId, ts: Date.now() })
  // تولید DataURL
  qrDataUrl.value = await QRCode.toDataURL(payload, {
    width: 320,
    margin: 2,
    color: { dark: '#215A75', light: '#FFFFFF' },
  })
})


</script>

<style scoped>
.qr-wrap {
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  background-image: url('@/assets/images/hero-banner.png');
  /* background:#f7fafc;  */
  padding: 32px 16px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  box-shadow: inset 0 0 0 2000px #e2e8f05e;
  position: fixed;
  justify-content: center;
  align-items: center;
  text-align: center;
  justify-self: center;
}

.DriverRouting {
  position: absolute;
  top: 20px;
}

.brand {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 12px;
  color: #215a75;
  font-weight: 800;
  width: fit-content;
  justify-self: end;
  top: 20px;
  left: 20px;
}

.brand img {
  height: 200px;
}

.qr-card {
  background: #fff;
  border: 1px solid #e6ebef;
  border-radius: 12px;
  padding: 24px;
  justify-content: center;
  justify-self: center;
  width: min(420px, 92%);
  text-align: center;
  max-width: 80%;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
}

.title {
  margin: 0 0 12px;
  color: #334155;
}

.qr-box img {
  width: 100%;
  height: auto;
  display: block;
}

.loading {
  color: #64748b;
}

.btn {
  display: inline-block;
  padding: 10px 18px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition:
    background 0.2s ease,
    opacity 0.2s ease,
    box-shadow 0.2s ease;
  border: 0;
}

.btn-primary {
  background: #215a75;
  color: #fff;
  box-shadow: 0 2px 6px rgba(2, 119, 189, 0.12);
  gap: 50px;
  display: flex;
  justify-content: center;
  text-align: center;
}
.btn-primary:hover {
  background: #16618a;
}

@media (max-width: 480px) {
  .brand {
    top: 30px;
  }
  .brand img {
    height: 150px;
  }
}
</style>
