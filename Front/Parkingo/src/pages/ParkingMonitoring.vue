<template>
  <div class="opdash" dir="rtl">
    <div class="qr-btn-wrap">
      <div class="financial">
        <router-link :to="{ name: 'financialReports' }" class="btn btn-primary">
          گزارشات مالی
        </router-link>
      </div>

      <!-- دکمه نمایش QR -->
      <button
        class="btn btn-primary"
        :class="{ 'is-disabled': !selected }"
        :disabled="!selected"
        @click="
          $router.push({ name: 'qr', params: { slotId: selected }, query: { t: Date.now() } })
        "
        :aria-disabled="!selected"
        title="ابتدا یک جایگاه را انتخاب کنید"
      >
        نمایش QR
      </button>
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
                  :class="[
                    'stall',
                    {
                      busy: isBusy(stallId('A', row, n - 1)),
                      selected: isSelected(stallId('A', row, n - 1)),
                    },
                  ]"
                  :title="stallId('A', row, n - 1)"
                  @click="onSlotClick(stallId('A', row, n - 1))"
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
                  :class="[
                    'stall',
                    {
                      busy: isBusy(stallId('A', row, 5 + (n - 1))),
                      selected: isSelected(stallId('A', row, 5 + (n - 1))),
                    },
                  ]"
                  :title="stallId('A', row, 5 + (n - 1))"
                  @click="onSlotClick(stallId('A', row, 5 + (n - 1)))"
                >
                  {{ stallId('A', row, 5 + (n - 1)) }}
                </button>
              </div>
            </div>
          </div>
        </section>

        <!-- ===== Block B ===== -->
        <section class="block block--B">
          <div v-for="row in rows" :key="'B' + row" class="lane lane-left">
            <div class="stalls">
              <div class="subrow">
                <button
                  v-for="n in 5"
                  :key="`B-${row}-r1-${n}`"
                  :class="[
                    'stall',
                    {
                      busy: isBusy(stallId('B', row, n - 1)),
                      selected: isSelected(stallId('B', row, n - 1)),
                    },
                  ]"
                  :title="stallId('B', row, n - 1)"
                  @click="onSlotClick(stallId('B', row, n - 1))"
                >
                  {{ stallId('B', row, n - 1) }}
                </button>
              </div>

              <div class="divider"></div>

              <div class="subrow">
                <button
                  v-for="n in 5"
                  :key="`B-${row}-r2-${n}`"
                  :class="[
                    'stall',
                    {
                      busy: isBusy(stallId('B', row, 5 + (n - 1))),
                      selected: isSelected(stallId('B', row, 5 + (n - 1))),
                    },
                  ]"
                  :title="stallId('B', row, 5 + (n - 1))"
                  @click="onSlotClick(stallId('B', row, 5 + (n - 1)))"
                >
                  {{ stallId('B', row, 5 + (n - 1)) }}
                </button>
              </div>
            </div>
            <div class="lane-tag">B{{ row }}</div>
          </div>
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

    <!-- ===================== MODAL ===================== -->
    <div v-if="modal.open" class="modal-backdrop" @click.self="closeModal">
      <div class="modal">
        <!-- حالت اسلات پر (اشغال) -->
        <template v-if="modal.mode === 'occupied'">
          <div class="slot-line">
            <strong>جایگاه:</strong>
            <span class="tag">{{ modal.slotId }}</span>
          </div>

          <div class="info">
            <div class="info-part">
              <strong>وضعیت:</strong>
              <div class="full">اشغال‌شده</div>
            </div>

            <div class="licence-plate">
              <strong>شماره پلاک:</strong>
              <div class="plate">
                <span class="plate-part">{{ showPlateParts[0] }}</span>
                <span class="plate-part">{{ showPlateParts[1] }}</span>
                <span class="plate-part">{{ showPlateParts[2] }}</span>
                <span class="plate-part">{{ showPlateParts[3] }}</span>
              </div>
            </div>

            <div class="info-part">
              <strong>زمان شروع:</strong>
              <div class="frame">{{ detailsForModal.startTime || 'نامشخص' }}</div>
            </div>

            <div class="info-part">
              <strong>زمان پایان:</strong>
              <div class="frame">{{ detailsForModal.endTime || 'نامشخص' }}</div>
            </div>

            <div class="info-part">
              <strong>زمان تقریبی رسیدن:</strong>
              <div class="frame">{{ detailsForModal.eta || '—' }}</div>
            </div>
          </div>

          <div class="modal-actions">
            <button class="btn btn-secondary" @click="closeModal">لغو</button>
            <button class="btn btn-warning" @click="makeEmpty(modal.slotId!)">
              تغییر به وضعیت خالی
            </button>
            <button class="btn btn-primary" @click="goRouting(modal.slotId!)">
              تأیید و مسیریابی
            </button>
          </div>
        </template>

        <!-- حالت اسلات خالی -->
        <template v-else>
          <div class="slot-line">
            <strong>جایگاه:</strong>
            <span class="tag">{{ modal.slotId }}</span>
          </div>

          <div class="info-part" style="background-color: #fff; padding: 10px">
            <strong>وضعیت:</strong>
            <div class="btn btn-warning">اشغال‌شده</div>
          </div>
          <!-- فرم ورود اطلاعات -->
          <form @submit.prevent="submitOccupy">
            <h3 class="modal-title">اختصاص جایگاه</h3>

            <div class="form-row">
              <label>شماره پلاک (۴ بخش):</label>
              <div class="plate-inputs">
                <input v-model.trim="form.plateParts[0]" maxlength="2" inputmode="numeric" />
                <input v-model.trim="form.plateParts[1]" maxlength="1" />
                <input v-model.trim="form.plateParts[2]" maxlength="3" inputmode="numeric" />
                <input v-model.trim="form.plateParts[3]" maxlength="2" inputmode="numeric" />
              </div>
              <small class="hint">مثال: <b>12 | ب | 451 | 43</b></small>
            </div>

            <div class="form-row time-row">
              <label>زمان شروع:</label>
              <input
                class="time"
                type="datetime-local"
                v-model="form.startTime"
              />
            </div>

            <div class="form-row time-row">
              <label>زمان پایان (اختیاری):</label>
              <input class="time" type="datetime-local" v-model="form.endTime" />
            </div>

            <div class="form-row time-row">
              <label>زمان تقریبی رسیدن:</label>
              <input class="time" type="text" v-model.trim="form.eta" placeholder="مثلاً ۵ دقیقه" />
            </div>

            <div v-if="errors.length" class="errors">
              <ul>
                <li v-for="(e, i) in errors" :key="i">{{ e }}</li>
              </ul>
            </div>

            <div class="modal-actions">
              <button type="button" class="btn btn-secondary" @click="closeModal">لغو</button>
              <button type="submit" class="btn btn-primary">تغییر به وضعیت پر و مسیریابی</button>
            </div>
          </form>
        </template>
      </div>
    </div>
    <!-- =================== /MODAL ====================== -->
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const selected = ref<string | null>(null)

/** تنظیمات کلی */
const rows = [0, 1, 2, 3, 4] // A0..A4 و B0..B4
const perRow = 10 // هر ردیف ۱۰ جایگاه

/** وضعیت اشغال‌شده‌ها + جزئیات */
type SlotDetails = {
  plateNumber: string
  startTime?: string
  endTime?: string
  eta?: string
}
const occupied = ref<Set<string>>(new Set(['A45', 'B41', 'B40', 'B44', 'B49']))

// جزئیات نمونه‌ی اولیه برای دمو
const detailsMap = reactive<Record<string, SlotDetails>>({
  A45: {
    plateNumber: '12 ب 451 43',
    startTime: '1404/06/23 15:00',
    endTime: 'نامعلوم',
    eta: '۲ دقیقه',
  },
  B41: { plateNumber: '21 ج 318 54', startTime: '1404/06/23 15:30', endTime: '—', eta: '۵ دقیقه' },
  B40: {
    plateNumber: '45 الف 123 11',
    startTime: '1404/06/23 16:10',
    endTime: '—',
    eta: '۳ دقیقه',
  },
  B44: { plateNumber: '31 د 777 77', startTime: '1404/06/23 14:20', endTime: '—', eta: '—' },
  B49: { plateNumber: '10 ب 222 45', startTime: '1404/06/23 13:45', endTime: '—', eta: '—' },
})

/** ابزارهای نمایش */
function stallId(block: 'A' | 'B', row: number, idx0: number) {
  const num = row * perRow + idx0 // 0..49
  const nn = String(num).padStart(2, '0') // 00..49
  return `${block}${nn}`
}
const isBusy = (id: string) => occupied.value.has(id)
const isSelected = (id: string) => selected.value === id

/** مدیریت کلیک روی اسلات */
function onSlotClick(id: string) {
  selected.value = id
  // باز کردن مودال با توجه به وضعیت اسلات
  openModal(isBusy(id) ? 'occupied' : 'empty', id)
}

/** Modal State */
const modal = reactive<{ open: boolean; mode: 'occupied' | 'empty'; slotId: string | null }>({
  open: false,
  mode: 'empty',
  slotId: null,
})

function openModal(mode: 'occupied' | 'empty', slotId: string) {
  modal.open = true
  modal.mode = mode
  modal.slotId = slotId

  // اگر حالت empty است، فرم را ریست کنیم
  if (mode === 'empty') {
    form.plateParts = ['', '', '', '']
    form.startTime = ''
    form.endTime = ''
    form.eta = ''
    errors.value = []
  }
}

function closeModal() {
  modal.open = false
}

/** جزئیات برای نمایش در مودال اشغال */
const detailsForModal = computed<SlotDetails>(() => {
  const id = modal.slotId || ''
  return detailsMap[id] || { plateNumber: '', startTime: '', endTime: '', eta: '' }
})

/** نمایش چهار بخش پلاک برای مودال اشغال */
const showPlateParts = computed(() => splitPlate(detailsForModal.value.plateNumber))

/** Helpers */
function splitPlate(plate: string): [string, string, string, string] {
  const parts = String(plate).trim().split(/\s+/)
  while (parts.length < 4) parts.push('')
  return [parts[0] || '', parts[1] || '', parts[2] || '', parts[3] || '']
}
function joinPlate(parts: string[]) {
  const p = [...parts]
  while (p.length < 4) p.push('')
  return `${p[0]} ${p[1]} ${p[2]} ${p[3]}`.trim()
}

/** دکمۀ تغییر به خالی (در مودال occupied) */
function makeEmpty(id: string) {
  occupied.value.delete(id)
  delete detailsMap[id]
  closeModal()
}

/** رفتن به صفحه‌ی مسیریابی */
function goRouting(id: string) {
  closeModal()
  router.push({
    name: 'qr', // اگر نام روت چیز دیگری است، این را مطابق پروژه‌ات تغییر بده
    params: { slotId: id },
    query: { t: Date.now() },
  })
}

/** فرم برای حالت empty → پر */
const form = reactive<{
  plateParts: string[]
  startTime: string
  endTime: string
  eta: string
}>({
  plateParts: ['', '', '', ''],
  startTime: '',
  endTime: '',
  eta: '',
})

const errors = ref<string[]>([])

function validateForm() {
  const errs: string[] = []

  // اعتبارسنجی ساده‌ی پلاک: 4 بخش پر باشد، 1 و 3 و 4 عددی باشند
  const [p0, p1, p2, p3] = form.plateParts.map((s) => s.trim())
  if (!p0 || !p1 || !p2 || !p3) errs.push('همه بخش‌های پلاک را وارد کنید.')
  if (!/^\d{1,3}$/.test(p0)) errs.push('بخش اول پلاک باید عددی (۱ تا ۳ رقم) باشد.')
  if (!/^[آابپتثجچحخدذرزسشصضطظعغفقکگلمنوهی]{1,2}$/.test(p1))
    errs.push('بخش دوم پلاک باید حروف فارسی (۱–۲ کاراکتر) باشد.')
  if (!/^\d{1,3}$/.test(p2)) errs.push('بخش سوم پلاک باید عددی (۱ تا ۳ رقم) باشد.')
  if (!/^\d{1,2}$/.test(p3)) errs.push('بخش چهارم پلاک باید عددی (۱ تا ۲ رقم) باشد.')

  if (!form.startTime) errs.push('زمان شروع را وارد کنید.')
  // در صورت پر بودن پایان، بررسی ترتیب
  if (form.endTime && form.startTime && new Date(form.endTime) < new Date(form.startTime)) {
    errs.push('زمان پایان نمی‌تواند قبل از زمان شروع باشد.')
  }

  errors.value = errs
  return errs.length === 0
}

function submitOccupy() {
  if (!modal.slotId) return
  if (!validateForm()) return

  const plateNumber = joinPlate(form.plateParts)
  // ذخیره‌ی وضعیت به پر
  occupied.value.add(modal.slotId)
  detailsMap[modal.slotId] = {
    plateNumber,
    startTime: toReadable(form.startTime),
    endTime: form.endTime ? toReadable(form.endTime) : 'نامعلوم',
    eta: form.eta || '—',
  }

  // بستن مودال و هدایت
  closeModal()
  goRouting(modal.slotId)
}

function toReadable(dtLocal: string) {
  // dtLocal مثل 2025-09-16T15:30 است؛ برای نمایش ساده تبدیل می‌کنیم
  // (در صورت نیاز بعداً می‌توانی به فرمت جلالی/فارسی تغییر دهی)
  if (!dtLocal) return ''
  const d = new Date(dtLocal)
  const yyyy = d.getFullYear()
  const mm = String(d.getMonth() + 1).padStart(2, '0')
  const dd = String(d.getDate()).padStart(2, '0')
  const hh = String(d.getHours()).padStart(2, '0')
  const mi = String(d.getMinutes()).padStart(2, '0')
  return `${yyyy}/${mm}/${dd} ${hh}:${mi}`
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
  overflow: auto;
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
  grid-template-columns: 28px 1fr;
  align-items: center;
  background: #f1fffc;
  border-radius: 14px;
  padding: 0px;
  max-height: 230px;
}

.lane-left {
  grid-template-columns: 1fr 28px;
}

.lane-tag {
  writing-mode: vertical-rl;
  background: var(--lane-tag);
  color: #fff;
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
  gap: 20px;
}

.divider {
  height: 2px;
  width: calc(100% - 24px);
  background: #000000a5;
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

.stall.selected {
  border: 3px solid #0277bd !important;
  box-shadow: 0 0 0 3px rgba(2, 119, 189, 0.18);
  background: #c6e1ed;
  transform: translateY(-1px);
}
.stall.busy.selected {
  border: 3px solid #0277bd !important;
  background: #ef826a;
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

/* پایه‌ی دکمه‌ها */
.btn {
  display: inline-block;
  padding: 10px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 400;
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
  background: #0f6ea1;
}
.btn-primary.is-disabled,
.btn-primary:disabled {
  background: #9db2bd;
  color: #eef5f8;
  cursor: not-allowed;
  opacity: 0.85;
  box-shadow: none;
}

.btn-secondary {
  background: #eceff1;
  color: #29434e;
}
.btn-secondary:hover {
  background: #e2e6ea;
}

.btn-warning {
  background: #19fa64;
  color: #215a75;
}
.btn-warning:hover {
  filter: brightness(1.05);
}

.financial,
.qr-btn-wrap {
  width: fit-content;
  text-align: center;
  display: flex;
  gap: 50px;
  justify-content: center;
  align-items: center;
  justify-self: center;
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

/* ====== MODAL styles ====== */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(231, 232, 236, 0.599);
  display: grid;
  place-items: center;
  z-index: 50;
}
.modal {
  width: min(75vw, 600px);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 15px 50px rgba(109, 89, 89, 0.25);
  direction: rtl;
  height: fit-content;
  max-height: 80vh;
  background: rgba(15, 23, 42, 0.30);
  backdrop-filter: blur(8px) saturate(120%);
  -webkit-backdrop-filter: blur(8px) saturate(120%);
}

form {
  background-color: #fff;
  padding-top: 10px;
  gap: 10px;
  max-height: 70vh;
  border-radius: 10px;
  overflow: hidden;
}

.modal-title {
  margin: 0 0 10px 0;
  font-size: 20px;
  color: #215a75;
  font-weight: 800;
  justify-content: center;
  text-align: center;
  align-items: center;
  background-color: #fff;
}
.slot-line {
  align-items: center;
  gap: 10px;
  margin: 4px 0 8px;
  background-color: #f5f8fa;
  justify-self: center;
  width: 100%;
  text-align: center;
  height: fit-content;
  padding: 10px;
  font-size: 18px;
  color: #215a75;
  border-radius: 10px;

}
.tag {
  background: #f1f5f9;
  color: #0f172a;
  border-radius: 10px;
  padding: 6px 10px;
  font-weight: 700;
  font-size: 16px;
  color: #215a75;
}

.modal-actions {
  display: flex;
  gap: 20px;
  justify-content: flex-end;
  padding: 10px 0 5px;
  background-color: #fff;
  justify-content: center;
}

.info {
  margin-top: 10px;
  width: 100%;
  background-color: #fff;
  padding: 10px 0;
}
.licence-plate,
.info-part {
  color: #215a75;
  font-size: 16px;
  margin: 5px;
  text-align: center;
  display: flex;
  direction: rtl;
  justify-content: center;
  gap: 20px;
  align-items: center;
  margin-bottom: 5px;
  margin-top: 5px;
}
.plate {
  display: flex;
  background-color: #ddeef8;
  border: 3px solid #68bdee;
  padding: 5px 16px;
  border-radius: 16px;
  font-size: 14px;
  font-weight: bold;
  color: #215a75;
  direction: ltr;
  align-items: center;
}
.plate-part {
  background-color: #ddeef8;
  border-bottom: 1px solid #6586b0;
  border-top: 1px solid #6586b0;
  padding: 4px 5px;
  font-size: 14px;
  font-weight: bold;
  color: #215a75;
}
.plate-part:first-child {
  border-left: 1px solid #6586b0;
}
.plate-part:last-child {
  border: 1px solid #6586b0;
}

.full {
  background-color: red;
  padding: 10px;
  border-radius: 16px;
  color: #fff;
}

.frame {
  background-color: #f5f8fa;
  min-width: 150px;
  text-align: center;
  color: #215a75;
  padding: 5px 12px;
  border-radius: 12px;
  font-size: 14px;
}

/* فرم حالت اسلات خالی */
.form-row {
  display: grid;
  gap: 6px;
  margin: 0px 0 10px;
  font-size: 14px;
  padding: 0 10px;
  background-color: #fff;
}
.form-row label {
  font-size: 16px;
  color: #215a75;
}

.time-row {
  display: flex;
  margin: 20px 0 10;
  gap: 40px;
}

.time {
  width: fit-content
}

.plate-inputs {
  display: grid;
  grid-template-columns: repeat(4, 0.2fr);
  /* display: flex; */
  gap: 2px;
  direction: ltr;
  text-align: right;
  box-sizing: border-box;
  padding: 5px 10px;
  justify-content: center;
  background-color: #ddeef8;
  border: 2px solid #68bdee;
  border-radius: 13px;
}
.plate-inputs input {
  border: 1px solid #6586B0;
  border-radius: 8px;
  padding: 8px 10px;
  /* font-size: 14px; */
  max-width: 80px;
  width: 10vw;
  background-color: #DDEEF8;
}
.form-row input[type='datetime-local'],
.form-row input[type='text'] {
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 8px 10px;
  font-size: 14px;
}
.hint {
  color: #64748b;
}

.errors {
  background: #fef2f2;
  border: 1px solid #fecaca;
  color: #b91c1c;
  padding: 10px 12px;
  border-radius: 12px;
  margin-top: 6px;
  font-size: 12px;
}
.errors ul {
  margin: 0;
  padding-inline-start: 10px;
}


@media(max-width: 460px){
  .modal-title{
    font-size: 15px;
  }

  .form-row label {
    font-size: 12px;
  }

  .btn{
    font-size: 12px;
  }

  .time-row {
    gap: 10px;
  }

  .time-row input {
    font-size: 10px;
    max-width: 100px;
  }

  .plate-inputs {
    max-width: 230px;
    justify-self: center;
  }

  .plate-inputs input {
    max-width: 30px;
  }
}
</style>
