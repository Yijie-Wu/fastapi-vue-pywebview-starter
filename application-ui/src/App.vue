<script setup>
import {onMounted} from 'vue';
</script>

<template>
  <div class="main">
    <router-view/>
  </div>
</template>

<style scoped>
.main {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100vh;
  width: 100vw;
}
</style>
