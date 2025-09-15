<template>
  <div class="opdash" dir="rtl">
    <div class="financial">
      <router-link :to="{ name: 'financialReports' }" class="btn-report">
        گزارشات مالی
      </router-link>
    </div>

    <main class="lot">
      <header class="top" style="display: flex">
        <div class="badges">
          <span class="badge">Block A</span>
        </div>
        <div class="badges">
          <span class="badge">Block B</span>
        </div>
      </header>

      <!-- خروجی بالا سمت چپ بلوک A -->
      <div class="out">
        <button class="gate gate--out">خروجی</button>
      </div>

      <div class="block-container">
        <!-- ===== Block A ===== -->
        <section class="block block--A">
          <div v-for="row in rows" :key="'A' + row" class="lane lane-right">
            <div class="lane-tag">A{{ row }}</div>

            <div class="stalls">
              <!-- سطر اول ۵تایی -->
              <div class="subrow">
                <button
                  v-for="n in 5"
                  :key="`A-${row}-r1-${n}`"
                  :class="['stall', { busy: isBusy(stallId('A', row, n - 1)) }]"
                  :title="stallId('A', row, n - 1)"
                  @click="onSelect(stallId('A', row, n - 1))"
                >
                  {{ stallId('A', row, n - 1) }}
                </button>
              </div>

              <div class="divider"></div>

              <!-- سطر دوم ۵تایی -->
              <div class="subrow">
                <button
                  v-for="n in 5"
                  :key="`A-${row}-r2-${n}`"
                  :class="['stall', { busy: isBusy(stallId('A', row, 5 + (n - 1))) }]"
                  :title="stallId('A', row, 5 + (n - 1))"
                  @click="onSelect(stallId('A', row, 5 + (n - 1)))"
                >
                  {{ stallId('A', row, 5 + (n - 1)) }}
                </button>
              </div>
            </div>
          </div>
        </section>

        <!-- <div class="mid-divider"> </div> -->

        <!-- ===== Block B ===== -->
        <section class="block block--B">
          <div v-for="row in rows" :key="'B' + row" class="lane lane-left">
            <div class="stalls">
              <div class="subrow">
                <button
                  v-for="n in 5"
                  :key="`B-${row}-r1-${n}`"
                  :class="['stall', { busy: isBusy(stallId('B', row, n - 1)) }]"
                  :title="stallId('B', row, n - 1)"
                  @click="onSelect(stallId('B', row, n - 1))"
                >
                  {{ stallId('B', row, n - 1) }}
                </button>
              </div>

              <div class="divider"></div>

              <div class="subrow">
                <button
                  v-for="n in 5"
                  :key="`B-${row}-r2-${n}`"
                  :class="['stall', { busy: isBusy(stallId('B', row, 5 + (n - 1))) }]"
                  :title="stallId('B', row, 5 + (n - 1))"
                  @click="onSelect(stallId('B', row, 5 + (n - 1)))"
                >
                  {{ stallId('B', row, 5 + (n - 1)) }}
                </button>
              </div>
            </div>
            <div class="lane-tag">B{{ row }}</div>
          </div>
          <!-- <div class="divider" style="margin-top: 20px;"></div> -->
        </section>
      </div>
      <!-- ورودی پایین سمت راست بلوک B -->
      <div class="in">
        <button class="gate gate--in">ورودی</button>
      </div>
    </main>

    <!-- لِـژان پایین -->
    <footer class="legend">
      <span class="chip chip--red"></span><small>پر</small> <span class="chip chip--gray"></span
      ><small>خالی</small>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

/** تنظیمات کلی */
const rows = [0, 1, 2, 3, 4] // A0..A4 و B0..B4
const perRow = 10 // هر ردیف ۱۰ جایگاه

/** نمونهٔ وضعیت اشغال‌شده‌ها برای دمو */
const occupied = ref<Set<string>>(new Set(['A45', 'B41', 'B40', 'B44', 'B49']))

/** ابزارهای نمایش */
function stallId(block: 'A' | 'B', row: number, idx0: number) {
  // idx0 بین 0..9 است
  const num = row * perRow + idx0 // 0..49
  const nn = String(num).padStart(2, '0') // 00..49
  return `${block}${nn}`
}

function isBusy(id: string) {
  return occupied.value.has(id)
}
function onSelect(id: string) {
  // اینجا باید پاپ‌آپ باز شود
  console.log('stall selected:', id)
}
</script>

<style scoped>
/* ریشه */
.opdash {
  --bg: #fff;
  --panel: #cfd8dc;
  --stall: #cfd8dc;
  --stall-border: #cfdcd8;
  --lane-tag: #0f6ea1;
  --busy: #ef4444;
  --busy-border: #ef4444;

  min-height: 100vh;
  height: fit-content;
  background: var(--bg);
  direction: ltr;
  overflow: auto;
  padding: 40px 24px 60px;
  background: var(--bg);
}

.lot {
  justify-self: center;
  max-width: 1200px;
  margin: 0 auto 200px;
  background: transparent;
  position: relative;
  overflow: auto; /* اسکرول افقی/عمودی در عرض‌های کم */
}

.block-container {
  display: flex;
  gap: 72px;
  padding: 100px 20px;
  background: #cfd8dc;
  border-radius: 12px;
  justify-content: center;
  max-width: 1000px;
  min-width: 980px;
}

.top {
  display: grid !important;
  grid-template-columns: 1fr 1fr;
  align-items: end;
  gap: 24px;
  max-width: 980px;
  justify-content: center;
  height: 100px;
}

.badges {
  background: transparent;
  justify-content: center;
  justify-self: center;
  height: fit-content;
}
.badge {
  background: #26a69a;
  width: fit-content;
  height: fit-content;
  color: #fff;
  padding: 10px;
  font-size: 20px;
  border-radius: 10px 10px 0 0;
  box-shadow: 2px 0px 4px rgba(0, 0, 0, 0.08);
}

.gate {
  position: absolute;
  z-index: 3;
  background: #215a75;
  color: #fff;
  font-size: 14px;
  padding: 10px 25px;
  border: 0;
  font-size: 18px;
}
.out {
  position: relative;
}
.gate--out {
  top: 20px;
  left: 0px;
  border-radius: 0 10px 10px 0;
}
.in {
  position: relative;
}
.gate--in {
  bottom: 20px;
  right: 0px;
  border-radius: 10px 0 0 10px;
}

.block {
  background: var(--panel);
  border-radius: 12px;
  display: grid;
  gap: 70px;
  padding: 8px 14px;
}

.lane {
  display: grid;
  grid-template-columns: 28px 1fr; /* A: برچسب چپ */
  align-items: center;
  background: #f1fffc;
  border-radius: 14px;
  padding: 0px;
  max-height: 230px;
}

.lane-left {
  /* B: برچسب راست */
  grid-template-columns: 1fr 28px;
}

.lane-tag {
  writing-mode: vertical-rl;
  background: var(--lane-tag);
  color: #fff;
  padding: 8px 0;
  text-align: center;
  font-weight: 700;
  font-size: 18px;
  height: 100%;
  padding: 0px 0px;
}

.stalls {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  position: relative;
}

.subrow {
  display: flex;
  padding: 8px 15px;
  flex-wrap: nowrap; /* همیشه ۵تایی کنار هم */
  gap: 20px; /* فاصله بین جایگاه‌ها */
}

.divider {
  height: 2px;
  width: calc(100% - 24px); /* دقیقاً وسط ستون، نه کل lane */
  background: #000000a5;
  opacity: 0.6;
  border-radius: 2px;
  align-self: center;
}

.mid-divider {
  height: calc(100vw -20px);
  width: 2px;
  background: #010101;
  opacity: 0.6;
  border-radius: 2px;
  align-self: center;
}

.block--B .subrow {
  flex-direction: row-reverse;
}

.stall {
  width: 55px;
  height: 68px;
  background: #cfd8dc;
  border: 1px solid #d7e1e5;
  border-radius: 10px;
  color: #334155;
  font-size: 16px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  cursor: pointer;
  transition:
    transform 0.06s ease,
    box-shadow 0.12s ease,
    background 0.12s ease;
}
.stall:hover {
  background: #c6e1ed;
  box-shadow: 0 0 0 3px rgba(2, 119, 189, 0.08);
  transform: translateY(-1px);
}
.stall.busy {
  background: var(--busy);
  color: #fff;
  border-color: var(--busy-border);
  box-shadow: none;
}

.stall.busy:hover {
  filter: brightness(0.95);
}

.stall.has-line {
  position: relative;
}
.stall.has-line::before {
  content: '';
  position: absolute;
  left: 6px;
  right: 6px;
  top: 50%;
  height: 2px;
  background: #2b3c46;
  opacity: 0.5;
  border-radius: 2px;
  transform: translateY(-50%);
}

/* لژان پایین */
.legend {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 10px 100px 0;
  color: #455a64;
}
.legend small {
  margin-inline-end: 18px;
  font-size: 22px;
}
.chip {
  display: inline-block;
  width: 40px;
  height: 52px;
  border-radius: 6px;
  margin-inline-end: 6px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.4);
}
.chip--red {
  background: #ef4444;
}
.chip--gray {
  background: #cfd8dc;
  border: 1px solid #cfd8dc;
}

.financial {
  width: 100%;
  text-align: center;
}

.btn-report {
  display: inline-block;
  background: #215a75;
  color: #fff;
  padding: 10px 18px;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: background 0.2s ease;
  justify-self: center;
}
.btn-report:hover {
  background: #0f6ea1;
}

@media (max-width: 1080px) {
  .block-container {
    min-width: 900px;
  }
}
@media (max-width: 860px) {
  .lot {
    overflow: auto;
  }
  .block-container {
    min-width: 860px;
  }
}
@media (max-width: 480px) {
  .lane {
    gap: 8px;
  }
  .subrow {
    gap: 10px;
  }
}
</style>
