<script setup>
import {onMounted, computed} from "vue";
import {get_userinfo} from "../../../apis/user.js";

import {useUserStore} from "../../../stores/user/user.js";

let user_store = useUserStore();


onMounted(async () => {
  await get_userinfo().then((res) => {
    user_store.setUserInfo(res.data);
  });
});

const avatar_url = computed(() => {
  if (user_store.userInfo.avatar === undefined) {
    return '/api/user/avatar/avatar.png';
  } else {
    return '/api/user/avatar/' + user_store.userInfo.avatar;
  }
});

</script>

<template>
  <el-avatar :src="avatar_url" :size="45" class="avatar"/>
</template>


<style scoped>
.avatar {
  cursor: pointer;
  border: 3px solid mediumslateblue;
}

.avatar:hover {
  border: 3px solid #0dcaf0;
  transition: 1s;
}

</style>