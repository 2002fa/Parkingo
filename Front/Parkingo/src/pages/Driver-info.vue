<template>
  <div class="parking-navigation">
    <div class="logo">
      <img style="height: 60px" src="@/assets/icons/p-logo.svg" alt="Parkingo Logo" />
    </div>

    <!-- صفحه اول - اطلاعات راننده و جای پارک -->
    <div v-if="!routeShown" class="parking-info">
      <div class="header">
        <h1>جایگاه {{ driverInfo.parkingSlot }}</h1>
      </div>

      <div class="info">
        <div class="licence-plate">
          <strong>شماره پلاک:</strong>
          <div class="plate">
            <span class="plate-part">{{ plateParts[0] }}</span>
            <span class="plate-part">{{ plateParts[1] }}</span>
            <span class="plate-part">{{ plateParts[2] }}</span>
            <span class="plate-part">{{ plateParts[3] }}</span>
          </div>
        </div>

        <div class="time-part">
          <strong style="text-align: right; direction: rtl">زمان اختصاص:</strong>
        </div>

        <div class="info-part">
          <strong>زمان شروع:</strong>
          <div class="frame">{{ driverInfo.startTime }}</div>
        </div>

        <div class="info-part">
          <strong>زمان پایان:</strong>
          <div class="frame">{{ driverInfo.endTime }}</div>
        </div>

        <div class="info-part">
          <strong class="time">زمان تقریبی رسیدن:</strong>
          <div class="frame">{{ driverInfo.estimatedArrivalTime }}</div>
        </div>
      </div>

      <button
        class="btn btn-primary"
        @click="
          $router.push({
            name: 'DriverRouting', // اگر اسم صفحه‌ مسیر چیز دیگه‌ایه همونو بذار
            params: { slotId: driverInfo.parkingSlot }, // از داده واقعی استفاده کن
            query: { t: Date.now() },
          })
        "
      >
        مسیر رو نشونم بده
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, reactive, computed } from 'vue'

export default defineComponent({
  name: 'DriverInfo',
  // چون توی روتر props: true گذاشتی، slotId به‌صورت prop میاد (اختیاری)
  props: {
    slotId: { type: String, required: false },
  },
  setup(props) {
    const routeShown = ref(false)

    const driverInfo = reactive({
      plateNumber: '12 ب 451 43',
      parkingSlot: props.slotId || 'B48', // اگر با پارامتر اومد، از همون استفاده کن
      startTime: '۱۴۰۴/۰۶/۲۳ ۱۵:۰۰',
      estimatedArrivalTime: '۲ دقیقه',
      endTime: 'نامعلوم',
    })

    // پلاک رو به ۴ بخش تبدیل کنیم (همیشه ۴ آیتم برگرده)
    const plateParts = computed(() => {
      const parts = String(driverInfo.plateNumber).trim().split(/\s+/)
      while (parts.length < 4) parts.push('')
      return parts.slice(0, 4)
    })

    const showRoute = () => {
      routeShown.value = true
    }
    const arrived = () => {
      alert('رسیدم به پارکینگ')
    }

    return {
      routeShown,
      driverInfo,
      plateParts,
      showRoute,
      arrived,
      // اگر جایی خواستی مستقیم از slotId استفاده کنی:
      slotId: props.slotId,
    }
  },
})
</script>

<style scoped>
/* استایل‌های خودت ـ بدون تغییر */
.parking-navigation {
  width: 100%;
  background-color: #fff;
  justify-self: center;
  justify-items: center;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 100vh;
  direction: ltr;
  padding: 50px 0 100px;
  background-size: cover;
}
.logo {
  position: absolute;
  height: 60px;
  top: 40px;
  justify-self: center;
  transform: translateX(50%);
}
.parking-info {
  padding: 80px 10px 30px;
}
.parking-info,
.parking-map {
  justify-content: center;
  align-items: center;
  width: 90%;
  max-width: 500px;
  text-align: center;
  justify-self: center;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
.header {
  align-items: center;
  gap: 10px;
  justify-self: center;
  background-color: #f5f8fa;
  width: 200px;
  text-align: center;
  justify-content: center;
  color: #215a75;
  padding: 8px;
  border-radius: 16px;
  font-size: 15px;
  direction: rtl;
  align-self: center;
}
.info {
  margin-top: 40px;
  width: 100%;
}
.licence-plate,
.info-part {
  color: #215a75;
  font-size: 20px;
  margin: 10px;
  text-align: center;
  display: flex;
  direction: rtl;
  justify-content: center;
  gap: 10px;
  align-items: center;
  margin-bottom: 20px;
}
.time-part {
  text-align: right;
  direction: rtl;
  padding: 5px 35px;
  color: #215a75;
  font-size: 20px;
  margin-top: 30px;
}
.plate {
  display: flex;
  background-color: #ddeef8;
  border: 3px solid #68bdee;
  padding: 8px 20px;
  border-radius: 16px;
  font-size: 20px;
  font-weight: bold;
  color: #215a75;
  direction: ltr;
  align-items: center;
}
.plate-part {
  background-color: #ddeef8;
  border-bottom: 1px solid #6586b0;
  border-top: 1px solid #6586b0;
  padding: 5px 10px;
  font-size: 18px;
  font-weight: bold;
  color: #215a75;
}
.plate-part:first-child {
  border-left: 1px solid #6586b0;
}
.plate-part:last-child {
  border: 1px solid #6586b0;
}
.frame {
  align-items: center;
  gap: 10px;
  justify-self: center;
  background-color: #f5f8fa;
  width: 150px;
  text-align: center;
  justify-content: center;
  color: #215a75;
  padding: 13px;
  border-radius: 12px;
  font-size: 18px;
  direction: rtl;
}
button {
  position: absolute;
  background-color: #5f93fb;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 70%;
  font-size: 18px;
  bottom: -50px;
  left: 50%;
  transform: translateX(-50%);
  max-width: 400px;
  text-align: center;
}
button:hover {
  background-color: #7ca8ff;
}
</style>
