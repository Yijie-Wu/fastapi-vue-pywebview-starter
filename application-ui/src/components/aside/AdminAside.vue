<script setup>
import {User, DataBoard, Grape, Setting, Calendar, DocumentCopy} from '@element-plus/icons-vue'

</script>

<template>
  <el-menu
      :default-active="$route.path"
      class="admin-aside"
      router
      unique-opened
      active-text-color="darkorange"
      :collapse-transition="false"
  >
    <el-menu-item index="/admin">
      <el-icon>
        <DataBoard/>
      </el-icon>
      <template #title>后台首页</template>
    </el-menu-item>
    <el-sub-menu index="roles-users">
      <template #title>
        <el-icon>
          <User/>
        </el-icon>
        用户管理
      </template>
      <el-menu-item index="/admin/roles/list">角色列表</el-menu-item>
      <el-menu-item index="/admin/users/list">用户列表</el-menu-item>
      <el-menu-item index="/admin/users/add">新增用户</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="alumnus-manager">
      <template #title>
        <el-icon>
          <Grape/>
        </el-icon>
        校友管理
      </template>
      <el-menu-item index="/admin/alumnus">校友列表</el-menu-item>
      <el-menu-item index="/admin/alumnus/add">新增校友</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="class-manager">
      <template #title>
        <el-icon>
          <Calendar/>
        </el-icon>
        年份照片
      </template>
      <el-menu-item index="/admin/year/list">年份列表</el-menu-item>
      <el-menu-item index="/admin/year/add">新增年份</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="fronts-manager">
      <template #title>
        <el-icon>
          <DocumentCopy/>
        </el-icon>
        轮播管理
      </template>
      <el-menu-item index="/admin/carousel/list">轮播列表</el-menu-item>
      <el-menu-item index="/admin/carousel/add">新增轮播</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="user-settings">
      <template #title>
        <el-icon>
          <Setting/>
        </el-icon>
        用户设置
      </template>
      <el-menu-item index="/admin/user/profile">用户信息</el-menu-item>
      <el-menu-item index="/admin/user/change-avatar">修改头像</el-menu-item>
      <el-menu-item index="/admin/user/change-password">修改密码</el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<style scoped>
.admin-aside {
  overflow-y: scroll;
  overflow-x: hidden;
}
</style>