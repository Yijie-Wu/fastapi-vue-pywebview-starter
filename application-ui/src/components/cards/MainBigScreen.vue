<script setup>
import {ref, defineProps} from 'vue'
import {calcFile} from "../../utils/common.js";

const props = defineProps(['carousels'])
const carouselHeight = window.innerHeight + 'px'

</script>

<template>
  <div class="container">
    <div class="carousel-area">
      <div class="carousel-container">
        <el-carousel
            indicator-position="none"
            :height="carouselHeight"
            :pause-on-hover="false"
            arrow="never"
        >
          <el-carousel-item v-for="item in props.carousels" :key="item.id">
            <div style="width: 100%;height: 100%;">
              <el-image :src="calcFile(item.store_name)" style="width: 100%;height: 100%;"></el-image>
            </div>

            <div class="image-desc">
              <el-text truncated type="warning" style="font-weight: bold; font-size: 40px;">{{ item.desc }}</el-text>
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.carousel-area {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.carousel-container {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}

.image-desc {
  height: 60px;
  position: relative;
  top: -60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>