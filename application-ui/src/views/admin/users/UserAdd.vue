<script setup>
import {ref, onMounted, reactive} from "vue";
import {useRouter} from "vue-router";
import {add_user} from "../../../apis/user.js";
import {get_roles} from "../../../apis/role.js";
import {showMessage} from "../../../utils/message.js"
import {useAllUsersStore} from "../../../stores/admin/user.js";
import {useAllRolesStore} from "../../../stores/admin/role.js";

const allTags = ref([])
const formRef = ref(null)
const router = useRouter()
const users_store = useAllUsersStore()
const roles_store = useAllRolesStore()

onMounted(() => {
  get_roles().then(res => {
    roles_store.setRoles(res.data)
  }).catch(err => {
    showMessage('error', '获取角色列表失败')
  })
})



const form = reactive({
  role_id: '',
  username: '',
})

const rules = reactive({
  role_id: [
    {required: true, message: '请选择用户角色', trigger: 'blur'},
  ],
  username: [
    {required: true, message: '用户名称不能为空', trigger: 'blur'},
    {min: 1, max: 20, message: '用户名称长度必须在1到20之间', trigger: 'blur'},
  ]
})


const createUser = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    let data = {
      role_id:form.role_id,
      username: form.username
    }

    add_user(data).then(res => {
      showMessage('success', '添加用户成功')
      router.push('/admin/users/list')
    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}

</script>

<template>
  <div class="container">
    <el-form ref="formRef" :model="form" :rules="rules" style="width:100%;" label-width="auto" label-position="left">
      <el-form-item style="margin-top:20px;" prop="role_id" label="用户角色">
        <el-select v-model="form.role_id" style="width:60%;min-width: 200px;">
          <el-option v-for="role in roles_store.roles" :key="role.id" :label="role.name" :value="role.id"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item style="margin-top:10px;" prop="username" label="用户名称">
        <el-input v-model="form.username" class="w-50 m-2" placeholder="用户名称" size="large" type="text"/>
      </el-form-item>

      <el-form-item style="margin-top:50px;" type="submit">
        <el-button type="primary" @click="createUser(formRef)" plain style="width: 100%;" size="large" round>创建新用户</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<style scoped>
.container {
  width: 90%;
  margin: 10px auto;
  border: 1px solid lightgrey;
  min-height: 200px;
  border-radius: 5px;
  padding: 10px;
}
</style>