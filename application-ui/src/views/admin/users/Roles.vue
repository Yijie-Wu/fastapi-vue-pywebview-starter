<script setup>
import {ref, onMounted} from "vue";

import {get_roles} from "../../../apis/role.js";
import {useAllRolesStore} from "../../../stores/admin/role.js";
import {showMessage} from "../../../utils/message.js";
import {calcAvatar} from "../../../utils/common.js";

const store = useAllRolesStore()

onMounted(() => {
  get_roles().then(res => {
    store.setRoles(res.data)
  }).catch(err => {
    showMessage('error', '获取角色列表失败')
  })
})

</script>


<template>
  <div class="datas-container">
    <el-table :data="store.roles" style="width: 100%" border>
      <el-table-column label="角色编号" prop="id" align="center" fixed="left" width="100"/>
      <el-table-column label="角色名称" prop="name" align="center" fixed="left" width="200"/>
      <el-table-column label="用户列表" prop="roles" align="center">
        <template #default="{row}">
          <el-avatar
              v-for="user in row.users"
              :key="user.id"
              :size="50"
              :src="calcAvatar(user.avatar)"
              :title="user.username"
              shape="circle"
              style="margin: 0 3px;"
          />
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>


<style scoped>
.datas-container {
  width: 98%;
  margin: 10px auto;
}
</style>