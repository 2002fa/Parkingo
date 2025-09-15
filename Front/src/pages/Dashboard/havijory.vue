<template>
  <div class="admins-page">
    <div class="header-title">
      <h1>ادمین‌ها</h1>
      <p class="subtitle">مدیریت ادمین‌ها و اپراتورها</p>
    </div>

    <div class="card">
          <div class="details-container">
                <div class="form-box">
      <h2 class="section-title">اپراتور جدید</h2>
      <div class="form-grid">
        <div class="form-item">
          <label>شماره پرسنلی</label>
          <input type="text" placeholder=".........." />
        </div>
        <div class="form-item">
          <label>نام کاربری</label>
          <input type="text" placeholder=".........." />
        </div>
        <div class="form-item">
          <label>نام و نام خانوادگی</label>
          <input type="text" placeholder=".........." />
        </div>
        <div class="form-item">
          <label>رمز عبور</label>
          <input type="password" placeholder=".........." />
        </div>
        <div class="form-item">
          <label>ایمیل</label>
          <input type="email" placeholder=".........." />
        </div>
        <div class="form-item">
          <label>شماره موبایل</label>
          <input type="text" placeholder="+98-.........." />
        </div>
        <div class="form-item">
          <label>نام پارکینگ</label>
          <select>
            <option>...........</option>
          </select>
        </div>
      </div>

      <div class="buttons">
        <button class="cancel-btn">انصراف</button>
        <button class="add-btn">اضافه کردن</button>
      </div>
    </div>
          </div>
    </div>
  </div> 
</template>

<style>
.parkings-page {
  direction: rtl;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 0;
  background: #E4F5ED;
}

.details-container {
  padding: 20px 40px;
  font-family: sans-serif;
  color: #222;
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

</style>
