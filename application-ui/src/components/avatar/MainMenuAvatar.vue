<script setup>
import {onMounted, computed} from "vue";
import {useRouter} from 'vue-router'
import {User, SwitchButton, DataBoard, Postcard, Picture} from "@element-plus/icons-vue";

import {calcAvatar} from "../../utils/common.js";
import {get_userinfo} from "@/apis/user.js";
import {removeToken} from "@/utils/token.js";
import {showMessage} from "@/utils/message.js";
import {useUserStore} from "@/stores/user/user.js";

const route = useRouter();
let user_store = useUserStore()


onMounted(() => {
  if (user_store.isLogin) {
    get_userinfo().then((res) => {
        user_store.setUserInfo(res.data);
      });
  }
});

const avatar_url = computed(() => {
  if (user_store.userInfo.avatar === undefined) {
    return calcAvatar();
  } else {
    return calcAvatar(user_store.userInfo.avatar);
  }
});

const isAdmin = computed(() => {
  return adminRoles.includes(user_store.userInfo.role);
});


function goTo(link) {
  route.push(link);
}

function logout() {
  removeToken();
  user_store.setUserInfo({});
  user_store.isLogin = false;
  showMessage('success', '登出成功');
  route.push('/');
}
</script>

<template>
  <div v-if="user_store.userInfo.username === undefined">
    <el-button :icon="User" type="danger" round @click="route.push('/auth/login')">登陆</el-button>
  </div>
  <div v-else class="avatar-container">
    <el-dropdown trigger="click">
    <span class="el-dropdown-link">
      <el-avatar
          :src="avatar_url"
          :size="45"
          class="avatar"
      />
    </span>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>
            <el-icon>
              <User/>
            </el-icon>
            {{user_store.userInfo.username}}
          </el-dropdown-item>
          <el-dropdown-item>
            <el-icon>
              <Postcard/>
            </el-icon>
            {{user_store.userInfo.role}}
          </el-dropdown-item>
          <el-dropdown-item @click="goTo('/admin');" divided v-if="user_store.userInfo.role === '超级管理员'">
            <el-icon>
              <DataBoard/>
            </el-icon>
            后台管理
          </el-dropdown-item>
          <el-dropdown-item divided @click="logout">
            <el-icon>
              <SwitchButton/>
            </el-icon>
            退出系统
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>

</template>


<style scoped>
.avatar-container {
  width: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.avatar {
  cursor: pointer;
  border: 3px solid mediumslateblue;
}

.avatar:hover {
  border: 3px solid #0dcaf0;
  transition: 1s;
}

</style>
