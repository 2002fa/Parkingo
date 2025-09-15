<template>
  <div class="parkings-page">
    <div class="header-title">
      <h1>اضافه کردن اطلاعات پارکینگ جدید</h1>
    </div>
    <div class="card">
      <!-- Form -->
      <form class="form">
        <div class="form-content">
          <div class="form-section">
            <h3>اطلاعات اصلی پارکینگ</h3>
            <div class="form-grid">
              <div class="form-row">
                <label>نام پارکینگ</label>
                <input type="text" v-model="form.name" />
              </div>

              <div class="form-row">
                <label>آدرس پارکینگ</label>
                <input type="text" v-model="form.address" />
              </div>

              <div class="form-row">
                <label>شماره شهرداری</label>
                <input type="text" v-model="form.code" />
              </div>

              <div class="form-row">
                <label>تصویر مجوز پارکینگ</label>
                <input type="file" />
              </div>

              <div class="form-row">
                <label>تاریخ عضویت</label>
                <input type="datetime-local" v-model="form.date" />
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
                <label>تعداد طبقات</label>
                <select v-model="floorsCount" @change="generateFloors">
                  <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
                </select>
              </div>

              <div class="form-row">
                <label>دارای محل شارژ خودروهای برقی</label>
                <select v-model="form.evCharge">
                  <option>بله</option>
                  <option>خیر</option>
                </select>
              </div>

              <div class="form-row">
                <label>ظرفیت کل پارکینگ</label>
                <input type="text" v-model="form.totalCapacity" />
              </div>
            </div>
          </div>

          <!-- Dynamic Floors -->
          <div v-for="(floor, index) in floors" :key="index" class="form-section floor-box">
            <h3>طبقه {{ index + 1 }}</h3>

            <div class="form-grid">
              <div class="form-row">
                <label>تعداد ستون‌ها در هر طبقه</label>
                <select v-model="floor.columns">
                  <option v-for="n in 10" :key="n">{{ n }}</option>
                </select>
              </div>

              <div class="form-row">
                <label>تعداد ردیف‌ها در هر ستون</label>
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

              <div class="form-row">
                <label>ظرفیت کل طبقه</label>
                <input type="text" v-model="floor.capacity" />
              </div>
                <button type="button" class="floor-btn">مشاهده گرافیک طبقه</button>
            </div>
          </div>

          <!-- Owner Info -->
          <div class="form-section">
            <h3>اطلاعات صاحب پارکینگ</h3>
            <div class="form-grid">
              <div class="form-row">
                <label>نام و نام خانوادگی صاحب پارکینگ</label>
                <input type="text" v-model="form.owner" />
              </div>

              <div class="form-row">
                <label>کد ملی</label>
                <input type="text" v-model="form.nationalId" />
              </div>

              <div class="form-row">
                <label>شماره موبایل</label>
                <input type="tel" v-model="form.mobile" placeholder="+98..." />
              </div>

              <div class="form-row">
                <label>نام کاربری</label>
                <input type="text" v-model="form.username" />
              </div>

              <div class="form-row">
                <label>رمز عبور</label>
                <input type="password" v-model="form.password" />
              </div>
            </div>
          </div>

          <!-- Buttons -->
          <div class="form-actions">
            <button type="button" class="cancel">انصراف</button>
            <button type="submit" class="submit">اضافه کردن</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";

interface Floor {
  columns: number;
  rows: number;
  slots: number;
  entrances: number;
  capacity: string;
}

interface Form {
  name: string;
  address: string;
  code: string;
  date: string;
  type: "شبانه‌روزی" | "ساعتی" | "هردو";
  evCharge: "بله" | "خیر";
  totalCapacity: string;
  owner: string;
  nationalId: string;
  mobile: string;
  username: string;
  password: string;
}

const form = reactive<Form>({
  name: "",
  address: "",
  code: "",
  date: "",
  type: "شبانه‌روزی",
  evCharge: "خیر",
  totalCapacity: "",
  owner: "",
  nationalId: "",
  mobile: "",
  username: "",
  password: "",
});

const floorsCount = ref<number>(2);
const floors = ref<Floor[]>([]);

function generateFloors(): void {
  floors.value = [];
  for (let i = 0; i < floorsCount.value; i++) {
    floors.value.push({
      columns: 3,
      rows: 6,
      slots: 5,
      entrances: 1,
      capacity: "",
    });
  }
}

generateFloors();
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