<template>
  <div class="parking-navigation">
    <!-- هدر استیکی -->
    <div class="header">
      <button class="back" type="button" @click="handleBack" aria-label="بازگشت">
        <img src="@/assets/icons/back.svg" alt="" />
      </button>
      <h1>محل جای پارک شما:</h1>
    </div>

    <!-- نقشه -->
    <div class="map" ref="mapEl" dir="rtl">
      <!-- خیابان افقی سرتاسری بالا -->
      <div class="h-road-global top">
        <div class="h-centerline"></div>
      </div>

      <!-- ستون چپ: B -->
      <div class="section section-b">
        <h4 class="section-title">B</h4>

        <template v-for="rowIndex in 5" :key="'B-' + rowIndex">
          <div class="block">
            <div class="row">
              <button
                v-for="slot in getRowSlots('B', rowIndex, 'top')"
                :key="slot.slotId"
                class="slot"
                :class="{
                  occupied: slot.isOccupied,
                  selected: selectedSlot?.slotId === slot.slotId,
                  target: slot.slotId === targetId,
                }"
                :disabled="true"
                @click="selectSlot(slot)"
                :ref="(el: any) => setSlotRef(slot.slotId, el)"
                :title="slot.slotId"
              >
                <!-- اگر اشغال و منتخب نیست → ماشین، وگرنه → برچسب -->
                <template v-if="slot.isOccupied && selectedSlot?.slotId !== slot.slotId">
                  <img :src="carIcon" alt="car" class="car-icon" />
                </template>
                <template v-else>
                  <span class="slot-label">{{ slot.slotId }}</span>
                </template>
              </button>
            </div>
            <div class="row">
              <button
                v-for="slot in getRowSlots('B', rowIndex, 'bottom')"
                :key="slot.slotId"
                class="slot"
                :class="{
                  occupied: slot.isOccupied,
                  selected: selectedSlot?.slotId === slot.slotId,
                  target: slot.slotId === targetId,
                }"
                :disabled="true"
                @click="selectSlot(slot)"
                :ref="(el: any) => setSlotRef(slot.slotId, el)"
                :title="slot.slotId"
              >
                <template v-if="slot.isOccupied && selectedSlot?.slotId !== slot.slotId">
                  <img :src="carIcon" alt="car" class="car-icon" />
                </template>
                <template v-else>
                  <span class="slot-label">{{ slot.slotId }}</span>
                </template>
              </button>
            </div>
          </div>

          <div v-if="rowIndex < 5" class="h-road">
            <div class="h-centerline"></div>
          </div>
        </template>
      </div>

      <!-- راهرو عمودی وسط -->
      <div class="road" ref="roadEl">
        <div class="road-centerline"></div>
        <div class="exit" ref="exitEl">خروجی</div>
        <div class="entrance" ref="entranceEl">ورودی</div>
      </div>

      <!-- ستون راست: A -->
      <div class="section section-a">
        <h4 class="section-title">A</h4>

        <template v-for="rowIndex in 5" :key="'A-' + rowIndex">
          <div class="block">
            <div class="row">
              <button
                v-for="slot in getRowSlots('A', rowIndex, 'top')"
                :key="slot.slotId"
                class="slot"
                :class="{
                  occupied: slot.isOccupied,
                  selected: selectedSlot?.slotId === slot.slotId,
                  target: slot.slotId === targetId,
                }"
                :disabled="true"
                @click="selectSlot(slot)"
                :ref="(el: any) => setSlotRef(slot.slotId, el)"
                :title="slot.slotId"
              >
                <template v-if="slot.isOccupied && selectedSlot?.slotId !== slot.slotId">
                  <img :src="carIcon" alt="car" class="car-icon" />
                </template>
                <template v-else>
                  <span class="slot-label">{{ slot.slotId }}</span>
                </template>
              </button>
            </div>
            <div class="row">
              <button
                v-for="slot in getRowSlots('A', rowIndex, 'bottom')"
                :key="slot.slotId"
                class="slot"
                :class="{
                  occupied: slot.isOccupied,
                  selected: selectedSlot?.slotId === slot.slotId,
                  target: slot.slotId === targetId,
                }"
                :disabled="true"
                @click="selectSlot(slot)"
                :ref="(el: any) => setSlotRef(slot.slotId, el)"
                :title="slot.slotId"
              >
                <template v-if="slot.isOccupied && selectedSlot?.slotId !== slot.slotId">
                  <img :src="carIcon" alt="car" class="car-icon" />
                </template>
                <template v-else>
                  <span class="slot-label">{{ slot.slotId }}</span>
                </template>
              </button>
            </div>
          </div>

          <div v-if="rowIndex < 5" class="h-road">
            <div class="h-centerline"></div>
          </div>
        </template>
      </div>

      <!-- خیابان افقی سرتاسری پایین -->
      <div class="h-road-global bottom">
        <div class="h-centerline"></div>
      </div>

      <!-- مسیر (فلش آبی) -->
      <svg
        class="route-svg"
        ref="routeSvg"
        :width="mapEl?.clientWidth || '100%'"
        :height="mapEl?.clientHeight || '100%'"
      >
        <defs>
          <marker
            id="arrow"
            markerWidth="10"
            markerHeight="10"
            refX="8"
            refY="3"
            orient="auto"
            markerUnits="strokeWidth"
          >
            <path d="M0,0 L0,6 L9,3 z" fill="#2563eb"></path>
          </marker>
        </defs>
        <polyline
          v-if="routePoints"
          :points="routePoints"
          fill="none"
          stroke="#2563eb"
          stroke-width="4"
          stroke-linejoin="round"
          stroke-linecap="round"
          marker-end="url(#arrow)"
        />
      </svg>
    </div>

    <!-- فوتر استیکی -->
    <div class="footer">
      <button class="button-finish" type="button" @click="handleFinish">رسیدم!</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, onMounted, onBeforeUnmount, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import carIcon from '@/assets/icons/car.svg'

const router = useRouter()
const route = useRoute()

type SectionKey = 'A' | 'B'
interface Slot {
  slotId: string
  isOccupied: boolean
}

/* نرمال‌سازی A5 → A05 */
function normalizeId(id: string | undefined): string | undefined {
  if (!id) return undefined
  const m = String(id).match(/^([AB])(\d{1,2})$/i)
  if (!m) return id
  const [, s, n] = m
  return s.toUpperCase() + n.padStart(2, '0')
}

/* اگر props هم داری، مشکلی نیست */
const props = defineProps<{ slotId?: string }>()
const paramSlotId = (route.params.slotId as string | undefined) ?? props.slotId
const querySlotId = route.query.slotId as string | undefined
const preselectedId = normalizeId(querySlotId ?? paramSlotId)

// 10 اسلات اشغال‌شده نمونه (دستی)
const OCCUPIED = new Set<string>([
  'A03',
  'A07',
  'A12',
  'A28',
  'A44',
  'B01',
  'B10',
  'B17',
  'B33',
  'B45',
])

function buildSlots(section: SectionKey): Slot[] {
  return Array.from({ length: 50 }, (_, i) => {
    const id = `${section}${String(i).padStart(2, '0')}`
    const isAssigned = id === preselectedId
    const isOcc = OCCUPIED.has(id)
    // اگر همین اسلاتِ QR باشد، به‌صورت آزاد رندر شود تا target آبی دیده شود
    return { slotId: id, isOccupied: isAssigned ? false : isOcc }
  })
}

// ⚠️ حتماً قبل از هر استفاده ساخته شود
const parkingSlots = ref<Record<SectionKey, Slot[]>>({
  A: buildSlots('A'),
  B: buildSlots('B'),
})

const selectedSlot = ref<Slot | null>(null)

function findSlotById(id: string | undefined): Slot | null {
  if (!id) return null
  return (
    parkingSlots.value.A.find((s) => s.slotId === id) ??
    parkingSlots.value.B.find((s) => s.slotId === id) ??
    null
  )
}

// برای چراغ آبی در template:
const targetId = computed(() => selectedSlot.value?.slotId ?? preselectedId ?? '')

function getRowSlice(sectionArr: Slot[], rowIndex: number) {
  const start = (rowIndex - 1) * 10
  return sectionArr.slice(start, start + 10)
}

function getRowSlots(section: SectionKey, rowIndex: number, pos: 'top' | 'bottom'): Slot[] {
  const ten = getRowSlice(parkingSlots.value[section], rowIndex)
  const half = pos === 'top' ? ten.slice(0, 5) : ten.slice(5, 10)
  return section === 'A' ? [...half].reverse() : half
}

function selectSlot(_slot: Slot) {
  // راننده اجازه تغییر ندارد
}

const mapEl = ref<HTMLElement | null>(null)
const roadEl = ref<HTMLElement | null>(null)
const entranceEl = ref<HTMLElement | null>(null)
const exitEl = ref<HTMLElement | null>(null)
const routeSvg = ref<SVGSVGElement | null>(null)
const slotElMap = new Map<string, HTMLElement>()
const routePoints = ref<string>('')

function setSlotRef(id: string, el: HTMLElement | null) {
  if (!el) {
    slotElMap.delete(id)
    return
  }
  slotElMap.set(id, el)
  // وقتی اسلات هدف همین بود، بعد از رندر آپدیت کن
  if (id === targetId.value) {
    requestAnimationFrame(() => updateRoute())
  }
}

function centerOf(el: Element, root: HTMLElement) {
  const r = el.getBoundingClientRect()
  const rr = root.getBoundingClientRect()
  // مختصات محتوامحور = اختلاف رکت‌ها + اسکرول
  const x = r.left - rr.left + root.scrollLeft + r.width / 2
  const y = r.top - rr.top + root.scrollTop + r.height / 2
  return { x, y }
}

function updateRoute() {
  if (!mapEl.value || !entranceEl.value) {
    routePoints.value = ''
    return
  }
  const root = mapEl.value
  const start = centerOf(entranceEl.value, root)
  const targetEl = slotElMap.get(targetId.value)
  if (!targetEl) {
    routePoints.value = ''
    return
  }
  const target = centerOf(targetEl, root)
  const mid = { x: start.x, y: target.y }
  routePoints.value = `${start.x},${start.y} ${mid.x},${mid.y} ${target.x},${target.y}`
}


watch(selectedSlot, async () => {
  await nextTick()
  updateRoute()
})
watch(parkingSlots, async () => {
  await nextTick()
  updateRoute()
})
watch(targetId, async () => {
  await nextTick()
  updateRoute()
})

onMounted(async () => {
  const init = findSlotById(preselectedId)
  if (init) selectedSlot.value = init

  await nextTick()
  updateRoute()
  centerScrollToRoad()
  window.addEventListener('resize', resizeHandler, { passive: true })
})

onBeforeUnmount(() => window.removeEventListener('resize', resizeHandler))

function centerScrollToRoad() {
  const wrap = mapEl.value,
    road = roadEl.value
  if (!wrap || !road) return
  if (window.matchMedia('(max-width: 500px)').matches) {
    const doCenter = () => {
      const centerX = road.offsetLeft + road.clientWidth / 2
      wrap.scrollLeft = Math.max(0, centerX - wrap.clientWidth / 2)
    }
    requestAnimationFrame(() => requestAnimationFrame(doCenter))
  } else {
    wrap.scrollLeft = 0
  }
}

function handleBack() {
  if (window.history.length > 1) router.back()
  else router.push({ name: 'dashboard' })
}

function handleFinish() {
  const id = selectedSlot.value?.slotId ?? preselectedId ?? ''
  router.push({ name: 'dashboard', query: { slotId: id, t: Date.now().toString() } })
}

// اندازهٔ ریسپانسیو SVG (برحسب پیکسل همان mapEl)
const svgW = ref(0)
const svgH = ref(0)

// ضخامت خط برحسب اندازهٔ نقشه (clamp بین 3 و 6 px)
const strokeW = computed(() => {
  const base = Math.max(svgW.value, svgH.value)
  return Math.min(6, Math.max(3, base / 300)) // 3px..6px
})

// نوک فلش متناسب با stroke
const markerW = computed(() => strokeW.value * 2) // پهنا
const markerH = computed(() => strokeW.value * 2) // ارتفاع
const markerRefX = computed(() => markerW.value * 0.9)

// همگام‌سازی اندازهٔ SVG با mapEl
function updateSvgSize() {
  if (!mapEl.value) return
  // از boundingClientRect استفاده می‌کنیم تا padding/zoom هم لحاظ شود
  const r = mapEl.value.getBoundingClientRect()
  svgW.value = Math.max(1, Math.round(r.width))
  svgH.value = Math.max(1, Math.round(r.height))
}

let ro: ResizeObserver | null = null
function handleScroll() {
  // با اسکرول داخلی نقشه، مختصات بصری تغییر می‌کند
  updateRoute()
}

onMounted(async () => {
  // ... کدهای فعلی تو ...

  // اندازهٔ اولیه
  updateSvgSize()
  updateRoute()

  // رصد تغییر اندازهٔ واقعی mapEl (نه‌فقط window.resize)
  if ('ResizeObserver' in window) {
    ro = new ResizeObserver(() => {
      updateSvgSize()
      // بعد از تغییر اندازه، دوباره نقاط محاسبه شوند
      requestAnimationFrame(() => updateRoute())
    })
    if (mapEl.value) ro.observe(mapEl.value)
  }

  // روی اسکرول افقی/عمودی کانتینر هم به‌روز شو
  mapEl.value?.addEventListener('scroll', handleScroll, { passive: true })
})

onBeforeUnmount(() => {
  if (ro && mapEl.value) ro.unobserve(mapEl.value)
  ro = null
  mapEl.value?.removeEventListener('scroll', handleScroll)
})

const resizeHandler = () => {
  updateSvgSize()
  updateRoute()
  centerScrollToRoad()
}
</script>

<style scoped>
.parking-navigation {
  width: 100%;
  background-color: #fff;
  justify-self: center;
  justify-items: center;
  align-items: center;
  text-align: center;
  min-height: 100vh;
  direction: ltr;
  padding: 0px 0 50px;
  background-size: cover;
  justify-content: center;
  display: flex;
  flex-direction: column;
  overflow: visible;
  scroll-behavior: smooth;
  width: 100%;
}

/* هدر استیکی */
.header {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 20px 16px;
  background: #fff;
  border-bottom: 1px solid #f2f2f2;
  direction: rtl;
  width: 100vw;
}

.header h1 {
  color: #333;
  font-size: 20px;
  margin: 0;
}
.back {
  position: absolute;
  left: 20px;
  top: 50%;
  transform: translateY(-50%);
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  background: #f6f5ff;
  border-radius: 999px;
  border: none;
  padding: 0;
}
.back img {
  width: 18px;
  height: 18px;
  display: block;
}

.header h1 {
  color: #333333;
  font-size: 20px;
}

.map {
  position: relative;
  display: grid;
  grid-template-columns: minmax(260px, 1fr) 84px minmax(260px, 1fr);
  grid-auto-rows: auto;
  padding: 0px 16px;
  min-height: 80vh;
  background: #fff;
  overflow: visible;
  scroll-behavior: smooth;
  width: 100%;
  box-sizing: border-box;
}

/* راهرو افقیِ سرتاسری بالا/پایین */
.h-road-global {
  grid-column: 1 / -1;
  height: 28px;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 0px;
  margin: 0px;
  position: relative;
}
.h-road-global.bottom {
  margin: 0px 0 4px;
}
.h-road-global .h-centerline {
  position: absolute;
  left: 8px;
  right: 8px;
  top: 50%;
  height: 2px;
  transform: translateY(-50%);
  background: repeating-linear-gradient(
    to right,
    transparent 0 16px,
    rgba(148, 163, 184, 0.6) 16px 24px
  );
}

/* راهرو عمودی وسط */
.road {
  position: relative;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
}
.road-centerline {
  position: absolute;
  inset: 0;
  width: 2px;
  margin: 0 auto;
  background: repeating-linear-gradient(
    to bottom,
    transparent 0 16px,
    rgba(148, 163, 184, 0.6) 16px 24px
  );
}
.entrance {
  position: absolute;
  bottom: 8px;
  left: 50%;
  transform: translateX(-50%);
  background: #e0e7ff;
  color: #1e3a8a;
  border: 1px solid #c7d2fe;
  border-radius: 10px;
  padding: 4px 10px;
  font-size: 15px;
}
.exit {
  position: absolute;
  top: 8px;
  left: 50%;
  transform: translateX(-50%);
  background: #fee2e2;
  color: #991b1b;
  border: 1px solid #fecaca;
  border-radius: 10px;
  padding: 4px 10px;
  font-size: 15px;
}

/* ستون‌های A/B */
.section {
  background: #fff;
  border-radius: 14px;
  min-width: 0;
}
.section-title {
  margin: 0 0 8px;
  font-weight: 700;
  font-size: 16px;
  color: #5f93fb;
  width: fit-content;
  padding: 10px 20px;
  background-color: #5f93fb4c;
  justify-self: center;
  border-radius: 6px;
  margin: 5px;
}

/* بلاک ۱۰تایی (دو ردیف ۵تایی) */
.block {
  border: 1px dashed #cbd5e1;
  border-radius: 12px;
  padding: 8px;
  margin: 10px;
  margin-bottom: 10px;

  min-width: 0;
}
.row {
  display: grid;
  gap: 8px;
  margin-bottom: 8px;
  grid-template-columns: repeat(5, minmax(0, 1fr));
}
.block .row + .row {
  position: relative;
  padding-top: 10px;
  margin-top: 10px;
}
.block .row + .row::before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  height: 1px;
  background: #e5e7eb;
}

/* خیابان افقی بین ردیف‌ها (داخل هر بلوک) */
.h-road {
  height: 26px;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 0px;
  margin: 8px 0 12px;
  position: relative;
}
.h-centerline {
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  height: 2px;
  transform: translateY(-50%);
  background: repeating-linear-gradient(
    to right,
    transparent 0 16px,
    rgba(148, 163, 184, 0.6) 16px 24px
  );
}

/* اسلات */
.slot {
  border: 1px solid #d1d5db;
  border-radius: 12px;
  background: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition:
    box-shadow 0.2s,
    outline-color 0.2s,
    background 0.2s;
  height: clamp(48px, 14vw, 64px);
  padding: 0 clamp(10px, 3.5vw, 14px);
  font-size: clamp(11px, 3.2vw, 13px);
  width: 100%;
  max-width: 100%;
  min-width: 0;
  box-sizing: border-box;
  padding-inline: clamp(5px, 2.5vw, 14px);
}
.slot.selected {
  outline: 3px solid #2563eb;
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15);
  background: #eff6ff;
}
.slot.occupied {
  background: #729cf089;
  color: #64748b;
  cursor: not-allowed;
}

/* آیکن ماشین: بزرگ و ریسپانسیو */
.car-icon {
  width: clamp(24px, 6.5vw, 34px);
  height: auto;
  display: block;
  height: auto;
  display: block;
}

/* برچسب داخل اسلات */
.slot-label {
  line-height: 1;
}

/* SVG مسیر */
.route-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 92%;
  margin-top: 10px;
  pointer-events: none;
  z-index: 10;
}

.button-finish {
  position: absolute;
  background-color: #5f93fb;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  /* width: 70%; */
  font-size: 18px;
  /* bottom: -50px; */
  left: 50%;
  transform: translateX(-50%);
  max-width: 400px;
  text-align: center;
  width: 300px;
  font-size: 18px;
  direction: rtl;
}

.button-finish:hover {
  background-color: #7ca8ff;
}

/* فوتر استیکی */
.footer {
  position: sticky;
  bottom: 0;
  z-index: 20;
  background: none;
  border-top: 1px solid #f2f2f2;
  padding: 12px 16px;
  display: flex;
  justify-content: center;
  height: 60px;
}

.slot.target {
  background: #e0f2fe;
  border-color: #0284c7;
  outline: 2px solid #38bdf8;
  color: #075985;
}

.slot.target:hover {
  background: #bae6fd;
}

@media (max-width: 620px) {
  .map {
    grid-template-columns: 360px 84px 360px;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    padding: 8px 12px;
  }

  .header {
    width: 95%;
  }
}

@media (max-width: 420px) {
  .parking-navigation {
    width: 130%;
    padding-right: 30px;
  }
}
</style>
