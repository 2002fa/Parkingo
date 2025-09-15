<template>
  <div class="parking-map">
    <h2>محل جای پارک شما</h2>
    <div class="map-container">
      <!-- ورودی -->
      <svg width="100%" height="500" viewBox="0 0 1000 500">
        <!-- مسیر ورودی -->
        <circle cx="50" cy="250" r="10" fill="blue" />
        <path d="M 50 250 L 300 250" stroke="blue" stroke-width="3" />

        <!-- نمایش جای پارک‌ها -->
        <g v-for="(block, blockIndex) in parkingSlots" :key="blockIndex">
          <!-- هر بلوک A یا B -->
          <g v-for="(slot, slotIndex) in block" :key="slotIndex">
            <rect
              :x="50 + slotIndex * 60"
              :y="100 + blockIndex * 70"
              width="50"
              height="50"
              :fill="slot.isOccupied ? 'gray' : 'lightblue'"
              :stroke="slot.isOccupied ? 'gray' : 'blue'"
            />
            <!-- جایگاه پارک به عنوان ماشین -->
            <image
              :x="50 + slotIndex * 60 + 10"
              :y="100 + blockIndex * 70 + 10"
              width="30"
              height="30"
              href="@/assets/icons/left-car.svg"
              v-if="!slot.isOccupied"
            />
            <text
              :x="50 + slotIndex * 60 + 20"
              :y="100 + blockIndex * 70 + 25"
              text-anchor="middle"
              fill="black"
              font-size="12px"
              font-family="Arial"
            >
              {{ slot.slotId }}
            </text>
          </g>
        </g>
      </svg>
    </div>

    <div class="floors">
      <button @click="switchFloor('A')">طبقه اول</button>
      <button @click="switchFloor('B')">طبقه دوم</button>
      <button @click="switchFloor('C')">طبقه سوم</button>
      <button @click="switchFloor('D')">طبقه چهارم</button>
    </div>

    <button @click="arrived">رسیدم!</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, reactive } from 'vue';

export default defineComponent({
  setup() {
    // داده‌های پارکینگ
    const parkingSlots = ref([
      // بلوک A و B با ۱۰ جای پارک در هر بلوک و ۵ ردیف
      [
        { slotId: 'A1', isOccupied: false },
        { slotId: 'A2', isOccupied: false },
        { slotId: 'A3', isOccupied: true },  // جای پارک پر
        { slotId: 'A4', isOccupied: false },
        { slotId: 'A5', isOccupied: false },
        { slotId: 'A6', isOccupied: false },
        { slotId: 'A7', isOccupied: true },
        { slotId: 'A8', isOccupied: false },
        { slotId: 'A9', isOccupied: false },
        { slotId: 'A10', isOccupied: false },
      ],
      [
        { slotId: 'B1', isOccupied: false },
        { slotId: 'B2', isOccupied: false },
        { slotId: 'B3', isOccupied: false },
        { slotId: 'B4', isOccupied: true },  // جای پارک پر
        { slotId: 'B5', isOccupied: false },
        { slotId: 'B6', isOccupied: false },
        { slotId: 'B7', isOccupied: false },
        { slotId: 'B8', isOccupied: false },
        { slotId: 'B9', isOccupied: false },
        { slotId: 'B10', isOccupied: false },
      ],
      // ادامه همینطور برای سایر بلوک‌ها
    ]);

    // متدها
    const switchFloor = (floor: string) => {
      // منطق برای جابجایی طبقات
      alert(`شما به طبقه ${floor} رفتید.`);
    };

    const arrived = () => {
      alert('رسیدم به پارکینگ');
    };

    return {
      parkingSlots,
      switchFloor,
      arrived,
    };
  },
});
</script>

<style scoped>
.parking-map {
  text-align: center;
  margin: 20px;
}

.map-container svg {
  margin-top: 20px;
}

.floors button {
  margin-right: 10px;
  padding: 10px 20px;
  background-color: #5f93fb;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.floors button:hover {
  background-color: #7ca8ff;
}

button {
  background-color: #5f93fb;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #7ca8ff;
}
</style>
