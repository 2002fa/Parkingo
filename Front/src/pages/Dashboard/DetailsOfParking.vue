<template>
  <div class="admins-page">
    <div class="header-title">
      <h1>پارکینگ عمومی طالقانی</h1>
    </div>
    <div class="card">
          <div class="details-container">

    <!-- آمارهای بالا -->
    <div class="stats-grid">
      <div class="stat-card">
        <span class="stat-value red">13 / 50</span>
        <span class="stat-label">ظرفیت پارکینگ</span>
      </div>
      <div class="stat-card">
        <span class="stat-value red">3 / 9</span>
        <span class="stat-label">تعداد خودروهای در انتظار ورود</span>
      </div>
      <div class="stat-card">
        <span class="stat-value">₹12656</span>
        <span class="stat-label">درآمد امروز</span>
      </div>
      <div class="stat-card">
        <span class="stat-value">3</span>
        <span class="stat-label">تعداد اپراتورهای حاضر</span>
      </div>
    </div>

    <!-- آمار مشتریان -->
    <div class="customer-stats">
      <div>
        <span class="stat-value">74</span>
        <span class="stat-label">تعداد خودروهای سواری امروز</span>
      </div>
      <div>
        <span class="stat-value">32</span>
        <span class="stat-label">تعداد موتورسیکلت‌ها</span>
      </div>
      <div>
        <span class="stat-value">456</span>
        <span class="stat-label">تعداد ورودی‌های این ماه </span>
      </div>
    </div>



    <!-- ظرفیت و جزئیات -->
    <div class="details-grid">
      <!-- ظرفیت پارکینگ -->
      <div class="capacity-section">
        <h2 class="section-title">ظرفیت پارکینگ</h2>
        <div
          v-for="(row, rowIndex) in parkingData"
          :key="rowIndex"
          class="row"
        >
          <span class="row-label">ردیف {{ rowIndex + 1 }}</span>
          <div class="row-icons">
            <img
              v-for="(slot, slotIndex) in row"
              :key="slotIndex"
              :src="slot === 1 ? BusOn : BusOff"
              class="bus-icon"
              alt="bus slot"
            />
          </div>
        </div>
      </div>

      <!-- آدرس و اطلاعات -->
      <div class="info-sections">
        <div class="info-card">
          <h2 class="section-title">آدرس پارکینگ</h2>
          <ul>
            <li>اصفهان، مارنان، خیابان وحید، خیابان خاقانی، خیابان هونس</li>
            <li>همه روزه از ساعت ۶ صبح الی ۱۲ شب</li>
          </ul>
        </div>

        <div class="info-card">
          <h2 class="section-title">اطلاعات پارکینگ</h2>
          <ul>
            <li>پارکینگ آسانسور دارد.</li>
            <li>پارکینگ خودروهای سواری، موتور سیکلت و خودروهای باری با ظرفیت ۳ تن</li>
            <li>پارکینگ سرویس بهداشتی ندارد.</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import BusOn from "@/assets/icons/Bus-on.svg";
import BusOff from "@/assets/icons/Bus-off.svg";

type ParkingRow = number[];
type ParkingData = ParkingRow[];

const parkingData = ref<ParkingData>([]);

// ===== شبیه‌ساز فرانت =====
onMounted(() => {
  parkingData.value = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
  ];
});
</script>

<style scoped>
.admins-page {
  direction: rtl;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 0;
  background: #E4F5ED;
}

.card {
  width: 950px;
  background: #CDECDE;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 4px 12px rgba(26, 38, 60, 0.06);
  margin-top: 20px;
}

.card-header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 14px;
}

.details-container {
  padding: 20px 40px;
  font-family: sans-serif;
  color: #222;
}

.header-title {
  text-align: center;
  margin-bottom: 20px;
}

.header-title h1 {
  font-size: 18px;
  margin: 0;
}
.header-title .subtitle {
  font-size: 12px;
  color: #6b7280;
  margin: 0;
}

.parking-title {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #333;
  text-align: right;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 16px;
}

.stat-card {
  background: #fff;
  border-radius: 10px;
  padding: 10px;
  text-align: center;
  border: 1px solid #eee;
}

.stat-value {
  display: block;
  font-size: 16px;
  font-weight: bold;
}

.stat-value.red {
  color: #d62828;
}

.stat-label {
  font-size: 12px;
  color: #666;
}

.customer-stats {
  display: flex;
  justify-content: space-between;
  border: 1px solid #eee;
  border-radius: 10px;
  margin-bottom: 20px;
  font-size: 13px;
  overflow: hidden; /* برای اینکه خطوط مرتب توی کادر باشن */
}

.customer-stats > div {
  flex: 1;
  padding: 10px;
  text-align: center;
  border-right: 1px solid #ccc; /* خط جداکننده بین آیتم‌ها */
}

.customer-stats .stat-value {
  display: block;
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 6px;
}

.customer-stats .stat-label {
  font-size: 12px;
  color: #555;
}

.details-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 16px;
}

.capacity-section {
  background: #fff;
  border: 1px solid #eee;
  border-radius: 10px;
  padding: 16px;
  width: 400px;
}

.section-title {
  font-size: 15px;
  margin-bottom: 10px;
  color: #333;
}

.row {
  display: flex;
  align-items: center;
  margin-bottom: 18px;
  margin-right: 50px;
}

.row-label {
  font-size: 12px;
  color: #444;
  margin-right: 8px;
  width: 50px;
  text-align: right;
}

.row-icons {
  display: flex;
  gap: 6px;
}

.bus-icon {
  width: 24px;
  height: 24px;
}

.info-sections {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.info-card {
  background: #fff;
  border: 1px solid #eee;
  border-radius: 10px;
  padding: 16px;
  font-size: 13px;
  width: 400px;
}

.info-card ul {
  padding-right: 16px;
  margin: 0;
}

.info-card li {
  margin-bottom: 6px;
  color: #444;
  font-size: 12px;
}
</style>