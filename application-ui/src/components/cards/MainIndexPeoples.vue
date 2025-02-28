<script setup>
import {ref, defineProps} from 'vue'
import UserCard from '../../components/cards/UserCard.vue'
import AlumnusDetail from '../../components/cards/AlumnusDetail.vue'
import {calcFile} from "../../utils/common.js";

const props = defineProps(['carousels'])
const carouselHeight = (window.innerHeight - 100) + 'px'
const viewData = ref({})
const viewDialog = ref(false)

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
            :interval="6000"
        >
          <el-carousel-item v-for="item in props.carousels" :key="item.id">
            <div style="width: 100%;height: 100%;">
              <el-image :src="calcFile(item.store_name)" style="width: 100%;height: 100%;"></el-image>
            </div>
            <div class="image-desc">
              {{ item.desc }}
            </div>
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  width: 98%;
  height: 100%;
  margin: 0 auto;
}

.carousel-area {
  width: 100%;
  height: calc(100vh - 80px);
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}

.carousel-container {
  width: 100%;
  height: calc(100vh - 100px);
}

.image-desc {
  height: 200px;
  position: relative;
  top: -200px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  font-size: 30px;
  font-weight: bold;
  color: gold;
  padding: 0 20px;
}

</style>