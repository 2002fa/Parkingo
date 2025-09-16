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
          <strong style="text-align: right; direction: rtl; b">زمان اختصاص:</strong>
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

      <button @click="showRoute">مسیر رو نشونم بده</button>
    </div>

    <!-- صفحه دوم - مسیریابی پارکینگ -->
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
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, reactive } from 'vue'


export default defineComponent({
  setup() {
    // داده‌ها
    const routeShown = ref(false) // برای نمایش یا مخفی کردن بخش مسیریابی

    const driverInfo = reactive({
      plateNumber: '12 ب 451 43', // شماره پلاک
      parkingSlot: 'B48',
      startTime: '۱۴۰۴/۰۶/۲۳ ۱۵:۰۰',
      estimatedArrivalTime: '۲ دقیقه',
      endTime: 'نامعلوم',
    })

    // تقسیم شماره پلاک به بخش‌ها
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
})
</script>

<style scoped>
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

.floors button {
  margin-right: 10px;
}

.map-container svg {
  margin-top: 20px;
}

@media (min-width: 200px) {
  .logo {
    margin-right: 300px;
  }
}


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










<!-- __________________________ -->

<script setup lang="ts">
import { ref, nextTick, onMounted, onBeforeUnmount, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import carIcon from '@/assets/icons/car.svg'

const router = useRouter()


type SectionKey = 'A' | 'B'
interface Slot {
  slotId: string
  isOccupied: boolean
}

function makeSlots(section: SectionKey): Slot[] {
  return Array.from({ length: 50 }, (_, i) => {
    const n = i.toString().padStart(2, '0')
    return { slotId: `${section}${n}`, isOccupied: Math.random() < 0.25 }
  })
}



function getRowSlice(sectionArr: Slot[], rowIndex: number) {
  const start = (rowIndex - 1) * 10
  return sectionArr.slice(start, start + 10)
}

// const parkingSlots = ref<Record<SectionKey, Slot[]>>({
//   A: makeSlots('A'),
//   B: makeSlots('B'),
// })






const selectedSlot = ref<Slot | null>(null)






function selectSlot(_slot: Slot) {
  // ❌ راننده اجازه تغییر انتخاب ندارد
}



function getRowSlots(section: SectionKey, rowIndex: number, pos: 'top' | 'bottom'): Slot[] {
  const ten = getRowSlice(parkingSlots.value[section], rowIndex)
  const half = pos === 'top' ? ten.slice(0, 5) : ten.slice(5, 10)
  return section === 'B' ? [...half].reverse() : half
}

// function selectSlot(slot: Slot) {
//   selectedSlot.value = slot
// }

const mapEl = ref<HTMLElement | null>(null)
const roadEl = ref<HTMLElement | null>(null)
const entranceEl = ref<HTMLElement | null>(null)
const routeSvg = ref<SVGSVGElement | null>(null)
const slotElMap = new Map<string, HTMLElement>()
const routePoints = ref<string>('')

function setSlotRef(id: string, el: HTMLElement | null) {
  if (!el) {
    slotElMap.delete(id)
    return
  }
  slotElMap.set(id, el)
}
function centerOf(el: Element, root: Element) {
  const r = el.getBoundingClientRect()
  const rRoot = root.getBoundingClientRect()
  return { x: r.left - rRoot.left + r.width / 2, y: r.top - rRoot.top + r.height / 2 }
}
function updateRoute() {
  if (!mapEl.value || !entranceEl.value || !selectedSlot.value) {
    routePoints.value = ''
    return
  }
  const root = mapEl.value
  const start = centerOf(entranceEl.value, root)
  const slotEl = slotElMap.get(selectedSlot.value.slotId)
  if (!slotEl) {
    routePoints.value = ''
    return
  }
  const target = centerOf(slotEl, root)
  const mid = { x: start.x, y: target.y }
  routePoints.value = `${start.x},${start.y} ${mid.x},${mid.y} ${target.x},${target.y}`
}

/* نرمال‌سازی slotId ورودی: A5 -> A05 */
function normalizeId(id: string | undefined): string | undefined {
  if (!id) return undefined
  const m = String(id).match(/^([AB])(\d{1,2})$/i)
  if (!m) return id
  const [, s, n] = m
  return s.toUpperCase() + n.padStart(2, '0')
}

const resizeHandler = () => {
  updateRoute()
  centerScrollToRoad()
}

watch(selectedSlot, async () => {
  await nextTick()
  updateRoute()
})




// ✅ 10 اسلات اشغال‌شده (دستی)
const OCCUPIED = new Set<string>([
  'A03','A07','A12','A28','A44',
  'B01','B10','B17','B33','B45',
])

// اسلات انتخابی از QR/Route
const route = useRoute()
const preselectedId = normalizeId((route.query.slotId || route.params.slotId) as string | undefined)



function findSlotById(id: string | undefined): Slot | null {
  if (!id) return null
  return (
    parkingSlots.value.A.find((s) => s.slotId === id) ??
    parkingSlots.value.B.find((s) => s.slotId === id) ??
    null
  )
}

// قفل روی اسلات QR:
selectedSlot.value = findSlotById(preselectedId)


// ساخت آرایه‌ی نهایی
const parkingSlots = ref<Record<SectionKey, Slot[]>>({
  A: buildSlots('A'),
  B: buildSlots('B'),
})

// اگر به هر دلیل layout تغییر کرد، مسیر را آپدیت نگه دار
watch([parkingSlots], async () => {
  await nextTick()
  selectedSlot.value = findSlotById(preselectedId)
  updateRoute()
})


const props = defineProps<{ slotId?: string }>()   // اختیاری، چون :slotId? گذاشتیم
const slotId = props.slotId ?? ''                  // رشتهٔ خالی اگر نبود



// اگر اسلات انتخابی جزء OCCUPIED باشد، باید «به‌عنوان آزاد» رندر شود تا آبی بماند
function buildSlots(section: SectionKey): Slot[] {
  return Array.from({ length: 50 }, (_, i) => {
    const id = `${section}${String(i).padStart(2, '0')}`
    const isAssigned = id === preselectedId
    const isOcc = OCCUPIED.has(id)
    return { slotId: id, isOccupied: isAssigned ? false : isOcc }
  })
}


// const route = useRoute()

// const preselectedId = normalizeId((route.query.slotId || route.params.slotId) as string | undefined)

// function findSlotById(id: string | undefined): Slot | null {
//   if (!id) return null
//   return (
//     parkingSlots.value.A.find((s) => s.slotId === id) ??
//     parkingSlots.value.B.find((s) => s.slotId === id) ??
//     null
//   )
// }

onMounted(async () => {
  const init = findSlotById(preselectedId)
  if (init) selectedSlot.value = init // هایلایت انتخاب اولیه
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
  // TODO: هر کار تمیزکاری/پینگ API/اتمام نشست را اینجا انجام بده

  const id = selectedSlot.value?.slotId || preselectedId
  router.push({
    name: 'DriverDone', // ← نام روت مقصد خودت
    query: { slotId: id || '', t: Date.now().toString() },
  })
}

</script>
