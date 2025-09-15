<template>
  <div class="reports" dir="rtl">
    <main class="container">
      <h1 class="title">آمار و گزارش‌های عملکرد</h1>

      <!-- کارت‌های خلاصه -->
      <section class="stats">
        <article class="stat">
          <div class="stat-value">{{ asCurrency(todayRevenue) }}</div>
          <div class="stat-label">درآمد امروز</div>
        </article>
        <article class="stat">
          <div class="stat-value">{{ asCurrency(weekRevenue) }}</div>
          <div class="stat-label">درآمد این هفته</div>
        </article>
        <article class="stat">
          <div class="stat-value">{{ asCurrency(lastMonthRevenue) }}</div>
          <div class="stat-label">درآمد ماه گذشته(تخـمینی)</div>
        </article>
        <article class="stat">
          <div class="stat-value red">{{ asCurrency(lastYearRevenue) }}</div>
          <div class="stat-label muted">درآمد یک سال (۱۲ ماه گذشته)</div>
        </article>
      </section>

      <!-- ظرفیت ۱۲ ماه اخیر -->
      <section class="panel">
        <header class="panel-head">
          <span>آمار پُر شدن ظرفیت پارکینگ‌ها در ۱۲ ماه گذشته</span>
        </header>
        <div class="panel-body">
          <canvas ref="capLineEl" height="120"></canvas>
        </div>
      </section>

      <!-- دو نمودار پایین -->
      <section class="grid-2">
        <article class="panel">
          <header class="panel-head">
            <span>آمار خودروهای ورودی به پارکینگ‌ها</span>
          </header>
          <div class="panel-body center">
            <canvas class="circle-canva" ref="pieEl" height="200"></canvas>
          </div>
        </article>

        <article class="panel">
          <header class="panel-head">
            <span>میانگین مدت زمان توقف خودروها در پارکینگ‌ها (۱۰ ماه گذشته)</span>
          </header>
          <div class="panel-body">
            <canvas ref="barEl" height="200"></canvas>
          </div>
        </article>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import Chart from 'chart.js/auto'

/* داده‌های نمونه – بعداً با API جایگزین شود */
const operatorName = 'Abolfazle_A'

const todayRevenue = 126
const weekRevenue = 11126
const lastMonthRevenue = 1280
const lastYearRevenue = 135600

const monthsFa = [
  'Jun',
  'Jul',
  'Aug',
  'Sep',
  'Oct',
  'Nov',
  'Dec',
  'Jan',
  'Feb',
  'Mar',
  'Apr',
  'May',
]
const capacityPercent = [60, 52, 25, 25, 70, 63, 92, 74, 73, 28, 66, 72]

const vehicleShareLabels = ['خودروهای سبک', 'موتورسیکلت', 'خودروهای سنگین']
const vehicleShare = [62, 20, 18]

const avgStayMonths = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']
const avgStayMins = [980, 520, 770, 1050, 1260, 540, 290, 170, 320, 610]

/* قالب پول */
function asCurrency(val: number) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  }).format(val)
}

/* رفرنس‌های بوم */
const capLineEl = ref<HTMLCanvasElement | null>(null)
const pieEl = ref<HTMLCanvasElement | null>(null)
const barEl = ref<HTMLCanvasElement | null>(null)

/* نمونه‌های چارت برای destroy */
let lineChart: Chart | null = null
let pieChart: Chart | null = null
let barChart: Chart | null = null

onMounted(() => {
  // Line
  lineChart = new Chart(capLineEl.value as HTMLCanvasElement, {
    type: 'line',
    data: {
      labels: monthsFa,
      datasets: [
        {
          label: 'ظرفیت پرشده (%)',
          data: capacityPercent,
          borderColor: '#6d28d9',
          backgroundColor: 'rgba(109,40,217,.15)',
          borderWidth: 3,
          tension: 0.35,
          pointRadius: 4,
          pointBackgroundColor: '#6d28d9',
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: { beginAtZero: true, max: 100, ticks: { callback: (v) => v + '%' } },
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label(ctx) {
              return ` ${ctx.parsed.y}%`
            },
          },
        },
      },
    },
  })

  // Pie
  pieChart = new Chart(pieEl.value as HTMLCanvasElement, {
    type: 'pie',
    data: {
      labels: vehicleShareLabels,
      datasets: [
        {
          data: vehicleShare,
          backgroundColor: ['#2563eb', '#10b981', '#f59e0b'],
          borderWidth: 0,
        },
      ],
    },
    options: {
      plugins: {
        legend: { position: 'bottom', labels: { boxWidth: 12 } },
        tooltip: {
          callbacks: {
            label(ctx) {
              const total = vehicleShare.reduce((a, b) => a + b, 0)
              const val = ctx.parsed
              const p = Math.round((val / total) * 100)
              return ` ${ctx.label}: ${val} (${p}%)`
            },
          },
        },
      },
    },
  })

  // Bar
  barChart = new Chart(barEl.value as HTMLCanvasElement, {
    type: 'bar',
    data: {
      labels: avgStayMonths,
      datasets: [
        {
          label: 'میانگین دقیقه',
          data: avgStayMins,
          backgroundColor: 'rgba(16,185,129,.9)',
          borderRadius: 6,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: { beginAtZero: true, ticks: { stepSize: 200 } },
      },
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: (ctx) => ` ${ctx.parsed.y} دقیقه`,
          },
        },
      },
    },
  })

  // ریدراو روی ریزایز (برای ارتفاع‌های منعطف پنل)
  const onResize = () => {
    lineChart?.resize()
    pieChart?.resize()
    barChart?.resize()
  }
  window.addEventListener('resize', onResize)
  // ذخیره در نمونه برای پاکسازی:
  ;(lineChart as any)._onResize = onResize
})

onBeforeUnmount(() => {
  if ((lineChart as any)?._onResize)
    window.removeEventListener('resize', (lineChart as any)._onResize)
  lineChart?.destroy()
  pieChart?.destroy()
  barChart?.destroy()
})
</script>

<style scoped>
.reports {
  --bg: #f7fafc;
  --panel: #ffffff;
  --border: #e6ebef;
  --muted: #6b7280;
  --title: #334155;

  min-height: 100vh;
  background: var(--bg);
}

.page-top {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: linear-gradient(90deg, #0ea5e9, #14b8a6);
  border-bottom-left-radius: 22px;
  border-bottom-right-radius: 22px;
  box-shadow: 0 2px 10px rgba(2, 119, 189, 0.15);
}
.avatar {
  width: 42px;
  height: 42px;
  background: #e2f6ff;
  border-radius: 999px;
  display: grid;
  place-items: center;
  border: 2px solid rgba(255, 255, 255, 0.7);
}
.avatar .dot {
  width: 14px;
  height: 14px;
  border-radius: 999px;
  background: #10b981;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.18);
}
.profile .name {
  color: #fff;
  font-size: 18px;
}
.brand {
  height: 28px;
}

.container {
  max-width: 1120px;
  margin: 18px auto 32px;
  padding: 0 12px;
}
.title {
  color: #413b89;
  font-size: 25px;
  margin: 30px 0 30px;
  font-weight: 800;
}

/* کارت‌های خلاصه */
.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 16px;
}
.stat {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 14px;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.02);
  text-align: center;
}
.stat-value {
  font-weight: 800;
  color: #111827;
}
.stat-value.red {
  color: #ef4444;
}
.stat-label {
  margin-top: 6px;
  color: #413b89;
  font-size: 12px;
}
.stat-label.muted {
  color: var(--muted);
}

/* پنل نمودارها */
.panel {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 14px;
  margin-top: 14px;
  overflow: hidden;
}
.panel-head {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  color: #6b7280;
  font-size: 13px;
}
.panel-body {
  padding: 10px 12px 16px;
  min-height: 260px;
  justify-content: center;
}
.panel-body.center {
  display: grid;
  place-items: center;
  justify-self: center;
}
.panel-body canvas {
  font-family: 'Vazirmatn';
}

/* گرید پایین */
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.chartjs-legend ul {
  display: flex;
  gap: 20px;
  justify-content: center;
  padding: 0;
  margin: 10px 0 0 0;
}

.chartjs-legend li {
  font-family: 'Vazirmatn';
  font-size: 14px;
  color: #374151;
  list-style: none;
  display: flex;
  align-items: center;
  gap: 6px;
  font-weight: 500;
}

.chartjs-legend li span {
  width: 14px;
  height: 14px;
  margin-left: 6px;
  border-radius: 3px;
}

.circle-canva {
  max-width: 700px;
  max-height: 700px;
}

/* ریسپانسیو */
@media (max-width: 980px) {
  .stats {
    grid-template-columns: repeat(2, 1fr);
  }
  .grid-2 {
    grid-template-columns: 1fr;
  }
  .circle-canva {
    max-width: 5500px;
    max-height: 550px;
  }
}
@media (max-width: 520px) {
  .page-top {
    grid-template-columns: auto auto 1fr;
  }
  .brand {
    height: 24px;
  }
}
</style>
