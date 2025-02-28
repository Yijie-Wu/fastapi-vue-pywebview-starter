<script setup>
import {reactive, ref} from "vue";
import {useRouter} from "vue-router";
import {change_user_password} from "../../../apis/user.js";
import {showMessage} from "../../../utils/message.js";
import {removeToken} from "../../../utils/token.js";
import {Lock} from "@element-plus/icons-vue";

const formRef = ref(null)
const router = useRouter()

const form = reactive({
  old_password: '',
  new_password: '',
  confirm_password: ''
})

const rules = reactive({
  old_password: [
    {required: true, message: '旧密码不能为空', trigger: 'blur'},
  ],
  new_password: [
    {required: true, message: '新密码不能为空', trigger: 'blur'},
  ],
  confirm_password: [
    {required: true, message: '确认新密码不能为空', trigger: 'blur'},
    {
      validator: (rule, value, callback) => {
        if (value !== form.new_password) {
          callback(new Error('两次密码不一致'));
        } else {
          callback();
        }
      }
    }
  ],
})


const changePassword = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    change_user_password(form).then(res => {
      showMessage('success', '修改用户密码成功, 请重新登陆!');
      removeToken();
      router.push('/auth/login');
    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}


</script>

<template>
  <div class="change-pass-container">
    <el-row :gutter="10">
      <el-col :span="12">
        <el-form ref="formRef" :model="form" :rules="rules" style="max-width:100%;" label-width="auto" label-position="left">
          <el-form-item style="margin-top:10px;" prop="old_password" label="旧密码">
            <el-input v-model="form.old_password" class="w-50 m-2" placeholder="旧密码" size="large" type="text"/>
          </el-form-item>
          <el-form-item style="margin-top:10px;" prop="new_password" label="新密码">
            <el-input v-model="form.new_password" class="w-50 m-2" placeholder="新密码" size="large" type="text"/>
          </el-form-item>
          <el-form-item style="margin-top:10px;" prop="confirm_password" label="确认密码">
            <el-input v-model="form.confirm_password" class="w-50 m-2" placeholder="确认密码" size="large" type="text"/>
          </el-form-item>

          <el-form-item style="margin-top:100px;" type="submit">
            <el-button type="primary" @click="changePassword(formRef)" plain style="width: 100%;"
                       size="large" round>修改密码
            </el-button>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="12" style="display: flex;align-items: center;justify-content: center;">
        <el-icon :size="200" color="grey">
          <Lock/>
        </el-icon>
      </el-col>
    </el-row>
  </div>
</template>


<style scoped>
.change-pass-container {
  width: 90%;
  margin: 20px auto;
  border: 1px solid lightgrey;
  padding: 10px;
  border-radius: 10px;
}
</style>