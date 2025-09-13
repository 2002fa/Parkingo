<template>
  <header class="site-header">
    <div class="container">
      <img src="@/assets/icons/parkingo-logo.png" alt="Parkingo" class="logo" />
      <nav>
        <router-link to="/dashboard">داشبورد</router-link>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.site-header { padding: 12px 0; border-bottom: 1px solid #eee; background:#fff; }
.logo { height: 32px; vertical-align: middle; }
nav a { margin-inline-start: 16px; }
</style>
