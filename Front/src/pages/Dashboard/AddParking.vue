<template>
  <div class="parkings-page">
    <div class="header-title">
      <h1>اضافه کردن پارکینگ جدید</h1>
    </div>
    <div class="card">
      <form class="form" @submit.prevent="submitForm">
        <div class="form-content">
          <!-- اطلاعات اصلی -->
          <div class="form-section">
            <h3>اطلاعات اصلی پارکینگ</h3>
            <div class="form-grid">
              <div class="form-row">
                <label>نام پارکینگ</label>
                <input type="text" v-model="form.name" required />
              </div>
              <div class="form-row">
                <label>آدرس پارکینگ</label>
                <input type="text" v-model="form.address" required />
              </div>
              <div class="form-row">
                <label>شماره شهرداری</label>
                <input type="text" v-model="form.code" required />
              </div>
              <div class="form-row">
                <label>نوع پارکینگ</label>
                <select v-model="form.type">
                  <option>شبانه‌روزی</option>
                  <option>روزانه</option>
                  <option>ساعتی</option>
                </select>
              </div>
              <div class="form-row">
                <label>دارای شارژ خودرو برقی</label>
                <select v-model="form.ev_charge">
                  <option :value="true">بله</option>
                  <option :value="false">خیر</option>
                </select>
              </div>
              <div class="form-row">
                <label>ظرفیت کل پارکینگ</label>
                <input type="number" v-model="form.total_capacity" />
              </div>
              <div class="form-row">
                <label>تعداد طبقات</label>
                <select v-model="floorsCount" @change="generateFloors">
                  <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
                </select>
              </div>
            </div>
          </div>

          <!-- طبقات -->
          <div v-for="(floor, index) in floors" :key="index" class="form-section floor-box">
            <h3>طبقه {{ index + 1 }}</h3>
            <div class="form-grid">
              <div class="form-row">
                <label>تعداد ستون‌ها</label>
                <select v-model="floor.columns">
                  <option v-for="n in 10" :key="n">{{ n }}</option>
                </select>
              </div>
              <div class="form-row">
                <label>تعداد ردیف در هر ستون</label>
                <select v-model="floor.rows">
                  <option v-for="n in 10" :key="n">{{ n }}</option>
                </select>
              </div>
              <div class="form-row">
                <label>تعداد جا پارک در هر ردیف</label>
                <select v-model="floor.slots">
                  <option v-for="n in 10" :key="n">{{ n }}</option>
                </select>
              </div>
              <div class="form-row">
                <label>تعداد ورودی</label>
                <select v-model="floor.entrances">
                  <option v-for="n in 5" :key="n">{{ n }}</option>
                </select>
              </div>
            </div>
          </div>

          <!-- اطلاعات مالک -->
          <div class="form-section">
            <h3>اطلاعات صاحب پارکینگ</h3>
            <div class="form-grid">
              <div class="form-row">
                <label>نام و نام خانوادگی</label>
                <input type="text" v-model="form.owner_name" required />
              </div>
              <div class="form-row">
                <label>کد ملی</label>
                <input type="text" v-model="form.owner_national_id" required />
              </div>
              <div class="form-row">
                <label>شماره موبایل</label>
                <input type="tel" v-model="form.owner_mobile" placeholder="+98..." required />
              </div>
              <div class="form-row">
                <label>نام کاربری</label>
                <input type="text" v-model="form.owner_username" required />
              </div>
              <div class="form-row">
                <label>رمز عبور</label>
                <input type="password" v-model="form.owner_password" required />
              </div>
            </div>
          </div>

          <!-- دکمه‌ها -->
          <div class="form-actions">
            <button type="button" class="cancel" @click="cancel">انصراف</button>
            <button type="submit" class="submit">اضافه کردن</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()

interface Floor {
  columns: number
  rows: number
  slots: number
  entrances: number
}

const floorsCount = ref(2)
const floors = ref<Floor[]>([])

function generateFloors() {
  floors.value = []
  for (let i = 0; i < floorsCount.value; i++) {
    floors.value.push({ columns: 3, rows: 3, slots: 2, entrances: 1 })
  }
}

const form = reactive({
  name: "",
  address: "",
  code: "",
  type: "شبانه‌روزی",
  ev_charge: false,
  total_capacity: 0,
  owner_name: "",
  owner_national_id: "",
  owner_mobile: "",
  owner_username: "",
  owner_password: ""
})

generateFloors()

async function submitForm() {
  try {
    const payload = {
      name: form.name,
      address: form.address,
      code: form.code, // اجباری و unique
      type: form.type || "شبانه‌روزی",
      ev_charge: form.ev_charge,
      total_capacity: Number(form.total_capacity) || 0,
      owner_name: form.owner_name || null,
      owner_national_id: form.owner_national_id || null,
      owner_mobile: form.owner_mobile || null,
      owner_username: form.owner_username || null,
      owner_password: form.owner_password || null
    }

    const headers = {
      Authorization: `Token ${auth.token}`,
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken") || undefined
    }

    const createRes = await axios.post(
      "http://127.0.0.1:8000/api/parkings/",
      payload,
      { headers, withCredentials: true }
    )

    const createdParking = createRes.data
    console.log("created parking:", createdParking)

    // ساخت اسپات‌ها مثل قبل
    const spotPromises: Promise<any>[] = []
    for (let fi = 0; fi < floors.value.length; fi++) {
      const floor = floors.value[fi]
      for (let c = 0; c < floor.columns; c++) {
        for (let r = 0; r < floor.rows; r++) {
          for (let s = 0; s < floor.slots; s++) {
            const number = `F${fi + 1}-C${c + 1}-R${r + 1}-S${s + 1}`
            const spotPayload = {
              parking: createdParking.id,
              number,
              floor: fi + 1,
              column: c + 1,
              row: r + 1,
              slot: s + 1,
              is_occupied: false
            }
            spotPromises.push(
              axios.post("http://127.0.0.1:8000/api/parking-spots/", spotPayload, { headers, withCredentials: true })
            )
          }
        }
      }
    }

    if (spotPromises.length) {
      await Promise.all(spotPromises)
    }

    alert("پارکینگ اضافه شد")
    router.push("/dashboard/parkings")
  } catch (err: any) {
    console.error("خطا:", err.response?.data)
    alert(JSON.stringify(err.response?.data) || "خطا در ذخیره‌سازی")
  }
}


// تابع کمکی برای گرفتن cookie
function getCookie(name: string) {
  const value = `; ${document.cookie || ""}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop()?.split(";").shift();
  return undefined;
}

function cancel() {
  router.push("/dashboard/parkings")
}
</script>

<style scoped>
.parkings-page {
  direction: rtl;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 0;
  background: #E4F5ED;
  min-height: 100vh;
}

.header-title {
  text-align: center;
  margin-bottom: 20px;
}

.header-title h1 {
  font-size: 18px;
  margin: 0;
  color: #333;
}

.card {
  width: 950px;
  /* background: #CDECDE;
  border-radius: 12px; */
  padding: 16px;
  /* box-shadow: 0 4px 12px rgba(26, 38, 60, 0.06); */
  margin-top: 20px;
}

.form-content {
  padding: 0 20px;
}

.form-section {
  /* background: #fff; */
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  background: #CDECDE;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.form-section h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 15px;
  color: #0a4ea3;
  border-bottom: 1px solid #eee;
  padding-bottom: 8px;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.form-row {
  display: flex;
  flex-direction: column;
}

.form-row label {
  font-size: 13px;
  margin-bottom: 5px;
  color: #555;
  font-weight: 500;
}

.form-row input, 
.form-row select {
  padding: 8px 10px;
  border: 1px solid #e6eef6;
  border-radius: 8px;
  font-size: 13px;
  background: #fff;
}

.form-row input:focus, 
.form-row select:focus {
  outline: none;
  border-color: #a0c5e3;
}

.floor-box {
  background: #e6f5ff;
}

.floor-btn {
    background: #007bff;
    color: #fff;
    padding: 6px 12px; /* کاهش padding برای کاهش ارتفاع دکمه */
    border: none;
    border-radius: 6px; /* کاهش شعاع حاشیه برای تناسب با ارتفاع کمتر */
    cursor: pointer;
    margin-top: 25px;
    font-size: 12px; /* کاهش سایز فونت */
    height: 37px; /* تعیین ارتفاع ثابت برای دکمه */
}

.floor-btn:hover {
    background: #0056b3;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 15px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #eee;
}

.cancel {
  background: #475a6c;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 13px;
}

.submit {
  background: #1d4ed8;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 13px;
}

.submit:hover {
  background: #1e40af;
}
</style>