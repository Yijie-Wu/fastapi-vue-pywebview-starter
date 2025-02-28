<template>
  <div class="logo-container" @click="goHome">
    <div class="logo">
      <img src="@/assets/image/logo.jpg" alt="logo">
    </div>
    <div class="logo-title hidden-md-and-down">
      <img src="@/assets/image/cnb_name.png" alt="logo" style="height: 30px;">
    </div>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'

const route = useRouter();

function goHome() {
  route.push('/')
}

</script>

<style scoped>
.logo-container {
  display: flex;
  align-items: center;
  width: 100%;
  min-width: 80px;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 42px;
  width: 42px;
  border-radius: 50%;
}

.logo img {
  height: 45px;
  width: 45px;
  border-radius: 50%;
}


.logo-title {
  height: 60px;
  display: flex;
  align-items: center;
  padding: 0 10px;
  flex: 1;
}

</style>