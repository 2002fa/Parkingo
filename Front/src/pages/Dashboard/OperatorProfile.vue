<template>
  <div class="parkings-page">

    <div class="header-title">
      <h1>اطلاعات فردی اپراتور</h1>
    </div>
    
    <div class="card">
      <div class="form-content">
        <div class="form-section">
          <h3>اطلاعات اپراتور</h3>
          <div class="form-grid">
            <div class="form-row">
              <label>شماره پرسنلی</label>
              <div class="input-with-icon">
                <input type="text" value="5001346" disabled />
              </div>
            </div>

            <div class="form-row">
              <label>نام کاربری</label>
              <div class="input-with-icon">
                <input type="text" value="Abolfazle_A" disabled />
              </div>
            </div>

            <div class="form-row">
              <label>نام و نام خانوادگی</label>
              <div class="input-with-icon">
                <input type="text" value="ابوالفضل احمدی" disabled />
              </div>
            </div>

            <div class="form-row">
              <label>رمز عبور</label>
              <div class="input-with-icon">
                <input type="password" value="******" disabled />
                <img src="@/assets/icons/nimbus_edit.svg" alt="edit" class="edit-icon" />
              </div>
            </div>

            <div class="form-row">
              <label>ایمیل</label>
              <div class="input-with-icon">
                <input type="email" value="abolfazleahmadi@gmail.com" disabled />
                <img src="@/assets/icons/nimbus_edit.svg" alt="edit" class="edit-icon" />
              </div>
            </div>

            <div class="form-row">
              <label>شماره موبایل</label>
              <div class="input-with-icon">
                <input type="text" value="+98-9365634187" disabled />
                <img src="@/assets/icons/nimbus_edit.svg" alt="edit" class="edit-icon" />
              </div>
            </div>

            <div class="form-row">
              <label>نام پارکینگ</label>
              <div class="input-with-icon">
                <input type="text" value="پارکینگ عمومی خاقانی" disabled />
              </div>
            </div>

            <div class="form-row">
              <label>آخرین زمان ورود به سیستم</label>
              <div class="input-with-icon">
                <input type="text" value="09/02/2025 - 09:12AM" disabled />
              </div>
            </div>

            <div class="form-row">
              <label>تصویر پروفایل</label>
              <div class="input-with-icon">
                <input type="text" placeholder="Browse file..." disabled />
                <img src="@/assets/icons/nimbus_edit.svg" alt="edit" class="edit-icon" />
              </div>
            </div>

            <div class="form-row">
              <label>تاریخ عضویت</label>
              <div class="input-with-icon">
                <input type="text" value="05/10/2023 - 04:12PM" disabled />
              </div>
            </div>

            <div class="form-row">
              <label>نوع اپراتور</label>
              <div class="input-with-icon">
                <input type="text" value="اپراتور گیت ورودی" disabled />
              </div>
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" class="logout-btn">
            <img src="@/assets/icons/material-symbols_logout.svg" alt="logout" class="logout-icon" />
            خروج از حساب کاربری
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

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
  margin: 20px 0;
}

.header-title h1 {
  font-size: 18px;
  margin: 0;
  color: #333;
}

.card {
  width: 950px;
  padding: 16px;
  margin-top: 20px;
}

.form-content {
  padding: 0 20px;
}

.form-section {
  background: #CDECDE;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
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

.input-with-icon {
  display: flex;
  align-items: center;
  position: relative;
}

.input-with-icon input {
  padding-right: 35px;
  width: 100%;
}

.edit-icon {
  position: absolute;
  left: 10px;
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 15px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #eee;
}

.logout-btn {
  background: #fff;
  border: 1px solid #dc3545;
  color: #dc3545;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 13px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.logout-btn:hover {
  background: #dc3545;
  color: #fff;
}

.logout-icon {
  width: 18px;
  height: 18px;
}
</style>