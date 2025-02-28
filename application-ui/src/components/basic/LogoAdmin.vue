<template>
  <div class="logo-container" @click="goHome">
    <div class="logo-collapse">
      <img src="@/assets/image/logo.jpg" alt="logo">
    </div>
    <div class="logo-title">
      <img src="@/assets/image/cnb_name.png" alt="logo" style="height: 20px;">
    </div>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'

const route = useRouter()

function goHome() {
  route.push('/')
}

</script>

<style scoped>
.logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  height: 60px;
  box-sizing: border-box;
  padding: 0;
  overflow: hidden;
  width: 100%;
}

.logo-collapse {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 65px;
  width: 65px;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.logo img {
  height: 48px;
  width: 48px;
  border-radius: 50%;
}

.logo-collapse img {
  height: 48px;
  width: 48px;
  border-radius: 50%;
}


.logo-title {
  height: 56px;
  display: flex;
  align-items: center;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  flex: 1;
}

.logo-text-admin {
  font-size: 18px;
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  padding: 0;
}

</style>
