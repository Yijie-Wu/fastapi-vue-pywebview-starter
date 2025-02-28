<script setup>

</script>

<template>
  <el-carousel indicator-position="outside" height="420px">
    <el-carousel-item v-for="item in 4" :key="item">
      <h3 text="2xl" justify="center">{{ item }}</h3>
    </el-carousel-item>
  </el-carousel>
</template>

<style scoped>

</style>