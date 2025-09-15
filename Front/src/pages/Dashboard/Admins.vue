<template>
  <div class="admins-page">
    <div class="header-title">
      <h1>ادمین‌ها</h1>
      <p class="subtitle">مدیریت ادمین‌ها و اپراتورها</p>
    </div>
    <div class="card">
      <!-- header -->
      <div class="card-header">
        <div class="header-controls">
          <!-- search -->
          <div class="search-wrap">
            <img src="@/assets/icons/search.svg" class="icon-search" alt="search" />
            <input
              v-model="searchQuery"
              @input="onSearchInput"
              type="text"
              placeholder="جستجو..."
              class="search-input"
            />
            <button v-if="searchQuery" class="clear-btn" @click="searchQuery=''">
              ✕
            </button>
          </div>
          
          <!-- add admin -->
          <button class="btn-add" @click="goToAddAdmin">
            <span class="plus">+</span> اضافه کردن
          </button>
        </div>
      </div>

      <!-- table -->
      <div class="table-wrap">
        <table class="admins-table">
          <thead>
            <tr>
              <th>نام پارکینگ</th>
              <th>نام و نام خانوادگی</th>
              <th>شماره تلفن</th>
              <th>تاریخ عضویت</th>
              <th>جزئیات</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="a in paginatedAdmins" :key="a.id">
              <td>{{ a.parking }}</td>
              <td>
                <div class="admin-name">{{ a.name }}</div>
                <div class="admin-role" v-if="a.role">{{ a.role }}</div>
              </td>
              <td>{{ a.phone }}</td>
              <td>{{ a.joinDate }}</td>
              <td>
                <button class="btn-details" @click="goToDetails(a)">
                  مشاهده جزئیات
                </button>
              </td>
            </tr>
            <tr v-if="paginatedAdmins.length === 0">
              <td colspan="5" class="no-results">هیچ نتیجه‌ای یافت نشد.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- pagination -->
      <div class="pagination">
        <div class="items-per-page">
          <label>Items per page:</label>
          <select v-model="itemsPerPage">
            <option v-for="n in [5,10,15]" :key="n" :value="n">{{ n }}</option>
          </select>
        </div>

        <div class="page-controls">
          <span>صفحه {{ currentPage }} از {{ totalPages }}</span>
          <button class="pg-btn" :disabled="currentPage===1" @click="prevPage">
            <img src="@/assets/icons/chevron-right.svg" alt="prev" />
          </button>
          <button class="pg-btn" :disabled="currentPage===totalPages" @click="nextPage">
            <img src="@/assets/icons/chevron-left.svg" alt="next" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()

const admins = ref([
  { id: 1, parking: "پارکینگ خاقانی", name: "احمد احمدی", phone: "۰۹۱۲۱۲۳۴۵۶۷", joinDate: "۱۴۰۲/۰۲/۱۵", role: "اپراتور" },
  { id: 2, parking: "پارکینگ محتشم کاشانی", name: "یاسر بابوئی", phone: "۰۹۱۲۳۳۴۴۵۵۶", joinDate: "۱۴۰۳/۰۵/۰۲", role: "ادمین" },
  { id: 3, parking: "پارکینگ نیکبخت", name: "علی موسوی", phone: "۰۹۱۲۴۵۶۷۸۹۰", joinDate: "۱۴۰۱/۱۱/۲۷", role: "اپراتور" },
  { id: 4, parking: "پارکینگ درمانی", name: "محمدامین حامدیان", phone: "۰۹۱۲۷۸۹۰۰۱۱", joinDate: "۱۴۰۲/۰۹/۱۰", role: "ادمین" },
])

const searchQuery = ref("")
const itemsPerPage = ref(5)
const currentPage = ref(1)

function normalize(s: string) {
  return s ? s.toString().trim().replace(/\s+/g, " ").toLowerCase() : ""
}

const filteredAdmins = computed(() => {
  const q = normalize(searchQuery.value)
  if (!q) return admins.value
  return admins.value.filter(
    (a) => normalize(a.name).includes(q) || normalize(a.parking).includes(q)
  )
})

const totalPages = computed(() =>
  Math.max(1, Math.ceil(filteredAdmins.value.length / itemsPerPage.value))
)

const paginatedAdmins = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  return filteredAdmins.value.slice(start, start + itemsPerPage.value)
})

function prevPage() {
  if (currentPage.value > 1) currentPage.value--
}
function nextPage() {
  if (currentPage.value < totalPages.value) currentPage.value++
}

function goToAddAdmin() {
  router.push("/dashboard/add-admin")
}
function goToDetails(a: any) {
  router.push("/dashboard/operator-profile")
}
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

.header-controls {
  display: flex;
  align-items: center;
  gap: 10px;
  justify-content: left;
  margin-left: 50px;
  width: 100%;
}

.search-wrap {
  position: relative;
  display: flex;
  align-items: center;
  background: #fff;
  border: 1px solid #e6eef6;
  border-radius: 8px;
  padding: 4px 8px;
  min-width: 176px;
  height: 29px;
}
.search-input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 13px;
  padding: 4px;
}
.icon-search {
  width: 14px;
  height: 14px;
  margin-left: 6px;
}
.clear-btn {
  border: none;
  background: none;
  cursor: pointer;
  font-size: 12px;
  color: #777;
}

.btn-add {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #fff;
  color: #000;
  border: 1px solid #000;
  border-radius: 8px;
  padding: 8px 12px;
  font-size: 13px;
  cursor: pointer;
}
.btn-add:hover {
  background: #1d4ed8;
  color: white;
}
.btn-add .plus {
  font-weight: bold;
}

.table-wrap {
  margin: 0 50px;
}

.admins-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}
.admins-table th {
  text-align: right;
  padding: 10px;
  color: #555;
  border-bottom: 1px solid #eee;
}
.admins-table td {
  padding: 10px;
  border-bottom: 1px solid #f3f3f3;
}

.admin-name {
  font-weight: 600;
}
.admin-role {
  font-size: 11px;
  color: #888;
}

.btn-details {
  border: 1px solid #ddd;
  background: #f9fafb;
  border-radius: 6px;
  padding: 6px 10px;
  font-size: 12px;
  cursor: pointer;
}
.btn-details:hover {
  background: #f1f5f9;
}

.no-results {
  text-align: center;
  padding: 20px;
  color: #777;
}

/* pagination */
.pagination {
  margin-top: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  padding: 0 50px;
}
.items-per-page select {
  margin-right: 6px;
  padding: 2px 6px;
  font-size: 12px;
}
.page-controls {
  display: flex;
  align-items: center;
  gap: 6px;
}
.pg-btn {
  border: 1px solid #ddd;
  background: #fff;
  border-radius: 6px;
  padding: 4px 6px;
  cursor: pointer;
}
.pg-btn:disabled {
  opacity: 0.4;
  cursor: default;
}
.pg-btn img {
  width: 12px;
  height: 12px;
}
</style>