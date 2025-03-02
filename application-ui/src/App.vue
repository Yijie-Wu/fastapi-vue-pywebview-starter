<script setup>
import {onMounted} from 'vue';
import {useRouter} from "vue-router";

import Logo from "@/assets/image/logo.png"
import {Setting, Sunny, Money, CloseBold, SemiSelect, DCaret} from "@element-plus/icons-vue";

const router = useRouter();

const goTo = (path) => {
  router.push(path);
}


</script>

<template>
  <div class="main">
    <div class="aside">
      <!--      <div class="base-function">-->
      <!--        <div class="base-function-item red">-->
      <!--          <el-icon :size="10"><CloseBold/></el-icon>-->
      <!--        </div>-->
      <!--        <div class="base-function-item orange">-->
      <!--          <el-icon :size="10"><SemiSelect/></el-icon>-->
      <!--        </div>-->
      <!--        <div class="base-function-item green trans145">-->
      <!--          <el-icon :size="10"><DCaret/></el-icon>-->
      <!--        </div>-->
      <!--      </div>-->
      <div class="logo">
        <el-image :src="Logo" style="width: 50px;height: 50px;border-radius: 50%;"></el-image>
      </div>
      <div class="menu">
        <div class="menu-items">
          <div class="menu-item active" @click="goTo('/')" v-if="router.currentRoute.value.path === '/'">
            <el-icon :size="30">
              <Sunny/>
            </el-icon>
          </div>
          <div class="menu-item" @click="goTo('/')" v-else>
            <el-icon :size="30">
              <Sunny/>
            </el-icon>
          </div>
          <div class="menu-item active" @click="goTo('/money')" v-if="router.currentRoute.value.path === '/money'">
            <el-icon :size="30">
              <Money/>
            </el-icon>
          </div>
          <div class="menu-item" @click="goTo('/money')" v-else>
            <el-icon :size="30">
              <Money/>
            </el-icon>
          </div>
        </div>
        <div class="setting-container active" @click="goTo('/setting')" v-if="router.currentRoute.value.path === '/setting'">
          <el-icon :size="30">
            <Setting/>
          </el-icon>
        </div>
        <div class="setting-container" @click="goTo('/setting')" v-else>
          <el-icon :size="30">
            <Setting/>
          </el-icon>
        </div>
      </div>
    </div>
    <div class="body">
      <router-view/>
    </div>
  </div>
</template>

<style scoped>
.main {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100vh;
  width: 100vw;
  display: flex;
}

.aside {
  width: 66px;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-right: 1px solid lightgray;
}

.base-function {
  display: flex;
  height: 30px;
  align-items: center;
}

.base-function-item {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  margin: 0 2px;
}

.red {
  background-color: red;
}

.orange {
  background-color: orange;
}

.green {
  background-color: green;
}

.trans145 {
  transform: rotate(145deg);
}

.logo {
  width: 60px;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  box-sizing: border-box;
  margin-top: 10px;
}

.menu {
  display: flex;
  flex: 1;
  flex-direction: column;
  width: 66px;
  box-sizing: border-box;
  align-items: center;
  justify-content: space-between;
}


.body {
  width:100%;
  padding: 0 10px;
  box-sizing: border-box;
  height: 100%;
}

.menu-item,
.setting-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 46px;
  height: 46px;
  background-color: #ccffdd;
  margin: 20px 0;
  border-radius: 10px;
}

.active {
  background-color: #f66703;
}


</style>
