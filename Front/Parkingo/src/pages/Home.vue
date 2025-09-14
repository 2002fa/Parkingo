<template>
  <div class="home" dir="rtl">
    <!-- نوار بالایی -->
    <div class="topbar">
      <div class="tagline">
        <p>پارکینگو ... راه من و تو :)</p>
      </div>
      <button class="login-link" @click="goLogin">ورود</button>
    </div>

    <!-- بنر -->
    <section class="hero">
      <div class="hero-bg">
        <img src="@/assets/images/hero-banner.png" />
      </div>
      <div class="hero-logo">
        <img src="@/assets/icons/hero-logo.svg" />
      </div>
    </section>

    <!-- تب‌های خاکستری -->
    <nav class="tabs">
      <ul>
        <li v-for="t in tabs" :key="t.id">
          <button :class="['tab', { active: activeTab === t.id }]" @click="goTo(t.id)">
            {{ t.label }}
          </button>
        </li>
      </ul>
    </nav>

    <!-- داستان ما -->
    <section id="story" class="section narrow">
      <h2>داستان ما</h2>
      <p>
        ایده «پارک هوشمند» از یک دغدغه ساده شروع شد؛ پیدا کردن جای پارک در شلوغی‌های روزمره همیشه
        وقت‌گیر و خسته‌کننده بود. ما خواستیم سیستمی بسازیم که این مشکل را هم برای رانندگان و هم برای
        اپراتورها حل کند. در تابستان ۱۴۰۴، با همکاری دو دانشجوی دانشگاه اصفهان، زهره سورانی و فاطمه
        علی‌ملکی، پروژه کارشناسی شکل گرفت و گام به گام به سامانه‌ای تبدیل شد که می‌تواند ورود و خروج
        خودروها را ثبت کند، جای پارک مناسب اختصاص دهد و مدیریت پارکینگ را ساده‌تر کند.
      </p>
    </section>

    <!-- ارزش‌ها -->
    <section id="values" class="section narrow">
      <h2>ارزش‌ها</h2>
      <ul class="values">
        <li>
          <img :src="iconUser" alt="" />
          <div class="text-value">
            <h3>سادگی و کاربرپسندی</h3>
            <p>سامانه باید برای همه قابل فهم و آسان باشد.</p>
          </div>
        </li>
        <li>
          <img :src="iconTime" alt="" />
          <div class="text-value">
            <h3>صرفه‌جویی در زمان و انرژی</h3>
            <p>کاهش زمان جست‌وجوی جای پارک و روان‌تر شدن ترافیک داخلی.</p>
          </div>
        </li>
        <li>
          <img :src="iconSec" alt="" />
          <div class="text-value">
            <h3>اعتماد و دقت</h3>
            <p>اطمینان خاطر راننده و اپراتور در تخصیص جای پارک و مدیریت درست.</p>
          </div>
        </li>
      </ul>
    </section>

    <!-- چشم‌انداز -->
    <section id="vision" class="section narrow">
      <h2>چشم‌انداز ما</h2>
      <p>
        ما آینده‌ای را تصور می‌کنیم که در آن پارکینگ‌های شهری دیگر محلی برای استرس و اتلاف وقت
        نباشند؛ بلکه محیطی هوشمند، منظم و ساده برای همه کاربران باشند. چشم‌انداز ما تبدیل شدن به
        بستری قابل اعتماد برای مدیریت هوشمند پارکینگ‌ها در مقیاس شهری است تا تجربه پارک‌کردن بخشی
        روان و لذت‌بخش از زندگی روزمره شود.
      </p>
    </section>

    <!-- مأموریت‌ها -->
    <section id="mission" class="section narrow">
      <h2>ماموریت‌ها</h2>
      <p>
        ماموریت ما از ابتدا روشن بود: ایجاد تجربه‌ای بهتر برای رانندگان و ابزار مدیریتی مطمئن برای
        اپراتورها و مدیران پارکینگ. ما ارزش‌هایی مثل سادگی استفاده، صرفه‌جویی در زمان، دقت در
        مدیریت، و رضایت کاربران را در قلب طراحی خود قرار دادیم. باور داریم که یک سامانه هوشمند، اگر
        واقعاً کاربرپسند باشد، می‌تواند هم رضایت راننده را بالا ببرد و هم فشار کاری اپراتور را کمتر
        کند.
      </p>
      <div class="missions">
        <article>
          <div class="ic"><img :src="iconDrv" alt="" /></div>
          <div class="divider"></div>
          <div class="txt">
            <h3>1. بهبود تجربه راننده با ارائه راهنمای سریع و دقیق برای یافتن جای پارک مناسب.</h3>
          </div>
        </article>
        <article style="direction: ltr">
          <div class="ic"><img :src="iconEasy" alt="" /></div>
          <div class="divider"></div>
          <div class="txt" style="direction: rtl">
            <h3>2. کمک به اپراتورها برای مدیریت آسان‌تر ورود، خروج و ظرفیت پارکینگ.</h3>
          </div>
        </article>
        <article>
          <div class="ic"><img :src="iconTrf" alt="" /></div>
          <div class="divider"></div>
          <div class="txt">
            <h3>3. کاهش بار ترافیکی درون پارکینگ و اطراف آن با هدایت هوشمند خودروها.</h3>
          </div>
        </article>
      </div>
    </section>

    <!-- مخاطبین -->
    <section id="audience" class="section narrow">
      <h2>مخاطبین</h2>
      <p>
        مخاطبین اصلی این سامانه اپراتورهای پارکینگ و مدیران هستند که نیاز دارند در لحظه وضعیت ظرفیت
        و رزروها را کنترل کنند. در کنار آن، رانندگان نیز از مزایای سیستم بهره می‌برند؛ از یافتن سریع
        جای پارک گرفته تا خروج بدون دردسر. این ترکیب از کاربران نشان می‌دهد که سامانه همزمان برای
        مدیریت حرفه‌ای و استفاده روزمره طراحی شده است.
      </p>
    </section>

    <!-- تماس با ما -->
    <section id="contact" class="section narrow">
      <div class="contact-card">
        <h2>تماس با ما</h2>

        <div class="contact-grid">
          <!-- راست: اطلاعات تماس -->
          <div class="contact-info">
            <div class="row">
              <span class="icon circle">
                <!-- تلفن -->
                <img src="@/assets/icons/phone.svg" />
              </span>
              <div class="val">
                <span class="lbl">تلفن:</span>
                <a class="ltr tel" href="tel:093607464042">093607464042</a>
              </div>
            </div>

            <div class="row">
              <span class="icon circle green">
                <!-- لوکیشن -->
                <img src="@/assets/icons/location.svg" />
              </span>
              <div class="val">
                <span class="lbl">آدرس:</span>
                <p class="addr">
                  اصفهان - خیابان هزار جریب - دانشگاه اصفهان - مجتمع انصاری - دانشکده مهندسی
                  کامپیوتر
                </p>
              </div>
            </div>
          </div>

          <!-- چپ: شبکه‌های اجتماعی کوچک -->
          <div class="contact-side">
            <div class="uni">دانشگاه اصفهان - دانشکده مهندسی کامپیوتر</div>
            <div class="socials">
              <a
                href="https://github.com/2002fa/Parkingo.git"
                target="_blank"
                rel="noopener"
                aria-label="GitHub"
              >
                <!-- <img src="@/assets/icons/github.svg" alt="GitHub" /> -->
              </a>
              <a href="#" aria-label="LinkedIn">
                <svg viewBox="0 0 24 24">
                  <path
                    fill="currentColor"
                    d="M6.94 6.5A1.94 1.94 0 1 1 5 4.56 1.94 1.94 0 0 1 6.94 6.5zM5.5 8.25h2.88V20H5.5zM10.5 8.25h2.76v1.6h.04A3 3 0 0 1 16 8.36c2.89 0 3.42 1.9 3.42 4.36V20h-2.87v-5.2c0-1.24 0-2.83-1.72-2.83s-2 1.34-2 2.73V20H10.5z"
                  />
                </svg>
              </a>
              <a href="#" aria-label="Instagram">
                <svg viewBox="0 0 24 24">
                  <path
                    fill="currentColor"
                    d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5m10 2H7a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3m-5 3.9A4.1 4.1 0 1 1 12 14.1 4.1 4.1 0 0 1 12 7.9m0 2A2.1 2.1 0 1 0 14.1 12 2.1 2.1 0 0 0 12 9.9m5.25-2.4a1 1 0 1 1-1 1 1 1 0 0 1 1-1z"
                  />
                </svg>
              </a>
              <a href="#" aria-label="Twitter">
                <svg viewBox="0 0 24 24">
                  <path
                    fill="currentColor"
                    d="M22 5.8a8.3 8.3 0 0 1-2.36.64A4.11 4.11 0 0 0 21.4 4a8.22 8.22 0 0 1-2.6 1 4.11 4.11 0 0 0-7 3.75 11.68 11.68 0 0 1-8.48-4.3 4.1 4.1 0 0 0 1.27 5.47 4.08 4.08 0 0 1-1.86-.52v.05a4.11 4.11 0 0 0 3.3 4 4.12 4.12 0 0 1-1.85.07 4.11 4.11 0 0 0 3.83 2.85A8.24 8.24 0 0 1 2 18.58 11.62 11.62 0 0 0 8.29 20c7.55 0 11.68-6.25 11.68-11.66v-.53A8.3 8.3 0 0 0 22 5.8z"
                  />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'

import logo from '@/assets/icons/parkingo-logo.png'

// آیکن‌ها (طبق نام‌هایی که دادی)
import iconUser from '@/assets/icons/user-friendly.svg'
import iconTime from '@/assets/icons/time-saving.svg'
import iconSec from '@/assets/icons/security.svg'
import iconDrv from '@/assets/icons/driving.svg'
import iconEasy from '@/assets/icons/easy-management.svg'
import iconTrf from '@/assets/icons/traffic.svg'

const router = useRouter()

const tabs = [
  { id: 'story', label: 'داستان ما' },
  { id: 'values', label: 'ارزش‌ها' },
  { id: 'vision', label: 'چشم‌انداز ما' },
  { id: 'mission', label: 'ماموریت‌ها' },
  { id: 'audience', label: 'مخاطبین' },
  { id: 'contact', label: 'تماس با ما' }, // ← اضافه شد
] as const

const activeTab = ref<(typeof tabs)[number]['id']>('story')

function goTo(id: string) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  activeTab.value = id as any
}

function goLogin() {
  router.push({ name: 'login' })
}

// هایلایت تب بر اساس اسکرول
let io: IntersectionObserver | null = null
onMounted(() => {
  io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          const id = e.target.getAttribute('id') as any
          if (id) activeTab.value = id
        }
      })
    },
    {
      root: null,
      threshold: 0.2,
      /* ارتفاع تب چسبان را از بالا کم کن تا دقیق همان سکشن فعال شود */
      rootMargin: '-72px 0px -60% 0px',
    },
  )
  tabs.forEach((t) => {
    const el = document.getElementById(t.id)
    if (el) io?.observe(el)
  })
})
onBeforeUnmount(() => io?.disconnect())
</script>

<style scoped>
/* پایه */
.home {
  background: #ffffff;
  color: #455a64;
  padding-bottom: 50px;
}

.section {
  padding: 40px 14px;
  scroll-margin-top: 72px;
}

.narrow {
  max-width: 900px;
  margin: 0 auto;
}

h2 {
  font-size: 25px;
  margin: 50px 0 30px;
  border-bottom: 2px solid #0277bd;
  width: fit-content;
}

/* نوار بالا */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 50px;
}

.topbar p {
  text-shadow: 1px 2px #6be2bc;
  font-size: 20px;
  color: #0277bd;
  text-decoration: rtl;
}

.login-link {
  background: transparent;
  border: 2px solid #2e5d6e;
  color: #2e5d6e;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 20px;
  width: 120px;
}

.login-link:hover {
  background: #e2e8f0;
  animation-fill-mode: forwards;
}

/* Hero */
.hero {
  position: relative;
  height: 450px;
  overflow: hidden;
  border-bottom: 1px solid #e6ebef;
  min-height: 330px;
  justify-content: center;
  align-items: center;
  justify-items: center;
  text-align: center;
}

.hero img {
  width: 100%;
  height: fit-content;
  min-width: 370px;
  margin-left: 0;
  justify-self: center;
  min-width: fit-content;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    #369f66 0%,
    #2c886c 25%,
    #1c716a 50%,
    #185c66 75%,
    #124f64 100%
  );
}

.hero-logo {
  position: absolute;
  top: 120px;
  margin-right: 400px;
  z-index: 10;
  width: 200px;
}

.hero-logo img {
  height: 250px;
}

.slice {
  position: absolute;
  right: 0;
  top: 0;
  height: 100%;
  width: 46%;
  transform: skewX(-28deg);
  opacity: 0.25;
}

.slice.s1 {
  background: #fff;
  right: -18%;
}

.slice.s2 {
  background: #0a6bd9;
  right: -8%;
}

.slice.s3 {
  background: #27d1c0;
  right: 2%;
}

.hero-inner {
  position: relative;
  z-index: 1;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding-inline: 16px;
}

.brand {
  width: 56px;
  height: 56px;
  object-fit: contain;
  border-radius: 50%;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}

.hero-inner h1 {
  margin: 8px 0 0;
  color: #fff;
  font-size: 25px;
  font-weight: 800;
}

/* Tabs */
.tabs {
  background: #e2e8f0;
  position: sticky;
  top: 0;
  z-index: 10;
  width: 100%;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.tabs ul {
  margin: 0;
  padding: 0 12px;
  display: flex;
  gap: 20px;
  list-style: none;
  justify-self: center;
}

.tab {
  border: none;
  border-radius: 10px;
  padding: 8px 14px;
  cursor: pointer;
  font-weight: 700;
  position: relative;
  background: #e2e8f0;
}

.tab.active {
  color: #0d47a1;
}

.tab.active::after {
  content: '';
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 0px;
  height: 2px;
  background-color: #0277bd;
}

/* Values */
.values {
  list-style: none;
  padding: 0;
  margin: 0px 0 0;
  display: grid;
  gap: 30px;
}

.values li {
  display: flex;
  gap: 5px;
  align-items: flex-start;
  background: none;
  padding: 0 0;
}

.values img {
  width: 80px;
  height: 80px;
}

.text-value {
  border-bottom: 1px solid #e6ebef;
  padding: 0 10px;
}

.values h3 {
  margin: 0 0 0px;
  font-size: 16px;
  font-weight: bold;
}

/* Missions */
.missions {
  display: grid;
  gap: 14px;
}

.missions article {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 2px;
  display: flex;
  align-items: center;
  background: #fff;
  /* border: 1px solid #e6ebef; */
  border-radius: 12px;
  padding: 12px;
}

.missions .ic img {
  width: 80px;
  height: 80px;
}

.divider {
  width: 200px;
  height: 2px;
  background-color: #cfd8dc;
}

.txt {
  background-color: #ecf1ff;
  padding: 20px 30px;
  border-radius: 16px;
  box-shadow: 4px 4px #3c3b3b26;
}

.missions h3 {
  margin: 0 0 6px;
  font-size: 16px;
}
/* Contact */
.contact-card {
  background: linear-gradient(180deg, #ffffff 0%, #f2f8fd 10%, #ecf1ff 90%, #ffffff 100%);
  /* border: 1px solid #e6ebef;
  border-radius: 16px; */
  padding: 50px 16px;
  box-shadow: 0 10px 24px rgba(2, 119, 189, 0.06);
}
.contact-card h2 {
  font-size: 22px;
  margin-bottom: 20px;
}
.contact-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 30px;
}
.contact-info .row {
  display: flex;
  gap: 15px;
  align-items: flex-start;
  margin: 20px 0;
}
.icon.circle {
  width: 25px;
  height: 25px;
  min-width: 32px;
  border-radius: 100px;
  background: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #0ea5e9;
  box-shadow: 0 1px 6px rgba(0, 0, 0, 0.06);
}
.icon.circle img {
  width: 30px;
  height: 30px;
}

.val {
  display: flex;
  gap: 6px;
  align-items: center;
  flex-wrap: wrap;
}
.val .lbl {
  font-weight: 700;
  color: #334155;
}
.tel {
  color: #0ea5e9;
  text-decoration: underline;
}
.addr {
  margin: 0;
  line-height: 1.9;
  color: #475569;
}
.contact-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}
.uni {
  font-size: 12px;
  color: #94a3b8;
}
.socials {
  display: flex;
  gap: 10px;
  align-items: center;
  justify-self: center;
}
.socials img,
.socials svg {
  width: 16px;
  height: 16px;
  fill: #64748b;
  color: #64748b;
}
.socials a:hover img,
.socials a:hover svg {
  filter: brightness(0.6);
}

@media (max-width: 900px) {
  .hero {
    height: 350px;
  }
  .hero-logo {
    position: absolute;
    top: 120px;
    margin-right: 0px;
    z-index: 10;
    width: 200px;
  }
  .hero-logo img {
    height: 200px;
  }
}

@media (max-width: 560px) {
  .tabs ul {
    gap: 0px;
  }
  .tab {
    font-size: 11px;
    font-weight: 300;
    padding: 8px 8px;
  }
}

@media (max-width: 460px) {
  .login-link {
    padding: 4px 8px;
    border-radius: 6px;
    font-size: 16px;
    width: 80px;
  }

  .topbar {
    padding: 6px 10px;
  }

  .topbar p {
    font-size: 18px;
  }

  .divider {
    display: none;
  }

  .ic img {
    width: 30px;
  }

  .missions article {
    gap: 20px;
  }
}
</style>
