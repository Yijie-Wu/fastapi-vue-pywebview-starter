<script setup>
import {ref, onMounted, reactive} from "vue";
import {useUserStore} from "../../../stores/user/user.js";
import {add_user, update_profile, get_userinfo} from '../../../apis/user.js'
import {calcAvatar} from "../../../utils/common.js";
import {showMessage} from "../../../utils/message.js";
import {useRouter} from "vue-router";
import {removeToken} from "../../../utils/token.js";

const store = useUserStore()
const user_id = ref(0)
const formRef = ref(null)
const router = useRouter()

const form = reactive({
  username: '',
})

const rules = reactive({
  username: [
    {required: true, message: '用户名称不能为空', trigger: 'blur'},
    {min: 1, max: 20, message: '用户名称长度必须在1到20之间', trigger: 'blur'},
  ]
})

onMounted(() => {
  get_userinfo().then(res => {
    form.username = res.data.username
    user_id.value = res.data.id
  }).catch(err => {
    showMessage('error', '获取原始用户信息失败')
  })
})


const updateUserProfile = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    let data = {
      user_id: user_id.value,
      username: form.username
    }

    update_profile(data).then(res => {
      showMessage('success', '修改用户名成功, 请重新登陆!');
      removeToken();
      router.push('/auth/login');


    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}


</script>

<template>
  <div class="profile-container">
    <el-card>
      <el-row :gutter="10">
        <el-col :span="6">
          <el-avatar
              :src="calcAvatar(store.userInfo.avatar)"
              :size="200"
              shape="square"
          />
        </el-col>
        <el-col :span="18">
          <div>
            <el-form ref="formRef" :model="form" :rules="rules" style="max-width:100%;" label-width="auto" label-position="left">
              <el-form-item style="margin-top:10px;" prop="username" label="用户名称">
                <el-input v-model="form.username" class="w-50 m-2" :disabled="store.userInfo.username === 'root'" placeholder="用户名称" size="large" type="text"/>
              </el-form-item>

              <el-form-item style="margin-top:100px;" type="submit">
                <el-button type="primary" @click="updateUserProfile(formRef)" :disabled="store.userInfo.username === 'root'" plain style="width: 100%;"
                           size="large" round>更新用户名
                </el-button>
              </el-form-item>
            </el-form>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<style scoped>
.profile-container {
  width: 96%;
  margin: 30px auto;
}
</style>