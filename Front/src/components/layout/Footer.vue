<template>
  <footer class="site-footer" dir="rtl">
    <div class="container">
      <div class="copy">
        <img src="@/assets/icons/larger-parkingo-logo.svg" alt="Parkingo" />
      </div>

      <div class="links">
        <div class="text-links">
          <router-link :to="{ name: 'home' }"> درباره ما </router-link>
          <router-link :to="{ name: 'home' }">حریم خصوصی</router-link>
          <router-link :to="{ name: 'home' }">تماس با ما</router-link>
          <router-link :to="{ name: 'home' }">قوانین و مقررات</router-link>
        </div>
        <div class="logo-links">
          <router-link :to="{ name: 'home' }"
            ><img src="@/assets/icons/telegram.svg"
          /></router-link>
          <router-link :to="{ name: 'home' }"><img src="@/assets/icons/github.svg" /></router-link>
          <router-link :to="{ name: 'home' }"
            ><img src="@/assets/icons/instagram.svg"
          /></router-link>
        </div>
      </div>
    </div>
    <div class="divider"></div>
    <small>© {{ new Date().getFullYear() }} پارکینگو — راهکاری هوشمند برای مدیریت پارکینگ</small>
  </footer>
</template>

<style scoped>
.site-footer {
  border-top: 1px solid #e6ebef;
  background: linear-gradient(
    90deg,
    #369f66 0%,
    #2c886c 25%,
    #1c716a 50%,
    #185c66 75%,
    #124f64 100%
  );
  min-height: 250px;
  text-align: center;
  overflow: hidden;
  max-height: 300px;
}

.container {
  max-width: 1100px;
  min-width: fit-content;
  margin: 0 auto;
  padding: 18px 16px;
  display: flex;
  gap: 10px;
  direction: rtl;
  margin-top: 40px;
}

.links {
  display: grid;
  flex-wrap: wrap;
  width: 70%;
  justify-content: center;
  align-items: center;
}

.links a {
  color: #fff;
  text-decoration: none;
}

.links a:hover {
  text-decoration: underline;
}

.text-links,
.logo-links {
  display: flex;
  gap: 50px;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  font-size: 15px;
}

.logo-links {
  gap: 20px;
}

.copy {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #6b7a85;
}

.copy img {
  height: 150px;
}

.divider {
  height: 1px;
  width: 50%;
  justify-self: center;
  background-color: #fff;
  min-width: 450px;
}

small {
  color: #fff;
  justify-self: center;
  margin: 100px 0;
  font-size: 14px;
  font-weight: 300;
}

@media (max-width: 700px) {
  .copy img {
    height: 100px;
  }
  .text-links,
  .logo-links {
    gap: 25px;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    font-size: 13px;
    margin-top: 20px;
  }
  small {
    font-size: 12px;
  }
}
</style>
