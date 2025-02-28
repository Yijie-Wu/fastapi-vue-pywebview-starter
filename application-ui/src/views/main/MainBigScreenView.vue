<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from 'vue-router';
import {get_show_carousels} from "../../apis/carousel.js";
import {useCarouselsStore} from "../../stores/main/carousel.js";
import {showMessage} from "../../utils/message.js";
import MainBigScreen from "../../components/cards/MainBigScreen.vue"


const router = useRouter()
const carousel_store = useCarouselsStore()


onMounted(() => {
  get_show_carousels().then(res => {
    carousel_store.setCarousels(res.data);
  }).catch(err => {
    showMessage('error', '获取轮播列表失败')
  })
})

setInterval(() => {
  get_show_carousels().then(res => {
    carousel_store.setCarousels(res.data);
  }).catch(err => {
    showMessage('error', '获取轮播列表失败')
  })
}, 3000)

</script>

<template>
  <div class="main-container">
    <div class="main-body">
      <MainBigScreen :carousels="carousel_store.carousels"/>
    </div>
  </div>

</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: calc(100vh);
  overflow-y: scroll;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}


</style>