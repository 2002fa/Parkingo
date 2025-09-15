<template>
  <div class="parkings-page">

    <div class="header-title">
      <h1>اپراتور جدید</h1>
    </div>
    
    <div class="card">
      <div class="form-content">
        <div class="form-section">
          <h3>اطلاعات اپراتور</h3>
          <div class="form-grid">
            <div class="form-row">
              <label>شماره پرسنلی</label>
              <input type="text" placeholder=".........." />
            </div>
            <div class="form-row">
              <label>نام کاربری</label>
              <input type="text" placeholder=".........." />
            </div>
            <div class="form-row">
              <label>نام و نام خانوادگی</label>
              <input type="text" placeholder=".........." />
            </div>
            <div class="form-row">
              <label>رمز عبور</label>
              <input type="password" placeholder=".........." />
            </div>
            <div class="form-row">
              <label>ایمیل</label>
              <input type="email" placeholder=".........." />
            </div>
            <div class="form-row">
              <label>شماره موبایل</label>
              <input type="text" placeholder="+98-.........." />
            </div>
            <div class="form-row">
              <label>نام پارکینگ</label>
              <select>
                <option>...........</option>
              </select>
            </div>
          </div>
        </div>

        <div class="form-actions">
          <button type="button" class="cancel">انصراف</button>
          <button type="submit" class="submit">اضافه کردن</button>
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