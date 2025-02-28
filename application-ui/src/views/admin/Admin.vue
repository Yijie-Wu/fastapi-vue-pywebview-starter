<script setup>
import {ref} from 'vue'

import AdminAside from "../../components/aside/AdminAside.vue";
import LogoAdmin from "../../components/basic/LogoAdmin.vue";

</script>

<template>
  <div class="admin">
    <el-container class="admin-container">
      <el-aside class="admin-aside">
        <div class="admin-aside-container">
          <div class="admin-aside-header">
            <LogoAdmin/>
          </div>
          <div class="admin-aside-menu">
            <AdminAside/>
          </div>
        </div>
      </el-aside>
      <el-main class="admin-body">
        <router-view/>
      </el-main>
    </el-container>
  </div>
</template>


<style scoped>
.admin {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100vh;
  width: 100vw;
}

.admin-container {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100%;
}

.admin-aside {
  margin: 0;
  padding: 0;
  width: 280px;
  box-sizing: border-box;
  border: none;
}

.admin-aside-container {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100%;
  display: flex;
  flex-direction: column;
  border: none;
  border-right: 1px solid lightgray;
}

.admin-aside-header {
  margin: 0;
  padding: 0 5px;
  box-sizing: border-box;
  height: 60px;
  border: none;
  border-bottom: 1px solid lightgray;
  overflow-x: hidden;
}

.admin-aside-menu {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  flex: 1;
  overflow-y: scroll;
  overflow-x: hidden;
}

.admin-body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 100%;
  overflow-y: scroll;
}


</style>