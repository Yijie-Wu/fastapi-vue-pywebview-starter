<script setup>
import {ref, onMounted, computed, reactive} from "vue";

import {change_avatar, get_users, update_user, delete_user} from "../../../apis/user.js";
import {useAllUsersStore} from "../../../stores/admin/user.js";
import {showMessage} from "../../../utils/message.js";
import {calcAvatar} from "../../../utils/common.js";
import {get_roles} from "../../../apis/role.js";
import {useAllRolesStore} from "../../../stores/admin/role.js";
import {genFileId} from "element-plus";
import {Plus} from "@element-plus/icons-vue";

const store = useAllUsersStore()
const search = ref('')
const editDialog = ref(false)
const editData = ref({})
const formRef = ref(null)
const upload = ref(null)
const files = ref([])
const selectUserID = ref(0)
const roles_store = useAllRolesStore()
const windowHeight = window.innerHeight - 20
const upload_api = 'http://127.0.0.1:8000/upload/user/avatar'

onMounted(() => {
  get_users().then(res => {
    store.setUsers(res.data)
  }).catch(err => {
    showMessage('error', '获取用户列表失败')
  })

  get_roles().then(res => {
    roles_store.setRoles(res.data)
  }).catch(err => {
    showMessage('error', '获取角色列表失败')
  })
})

const form = reactive({
  avatar: '',
  username: '',
  role_id: ''
})

const rules = reactive({
  avatar: [
    {required: true, message: '请上传头像', trigger: 'blur'}
  ],
  username: [
    {required: true, message: '用户名不能为空', trigger: 'blur'},
    {min: 1, max: 20, message: '用户名长度必须在1到20之间', trigger: 'blur'},
  ],
  role_id: [
    {required: true, message: '请选择角色', trigger: 'blur'}
  ],
})


const handleEdit = (index, row) => {
  editDialog.value = true
  editData.value = row
  form.avatar = row.avatar
  form.username = row.username
  form.role_id = row.role_id
  selectUserID.value = row.id
}

const handleDelete = (index, row) => {
  delete_user(row.id).then(res => {
    showMessage('success', '用户删除成功')
    store.removeUser(row.id)
  }).catch(err => {
    showMessage('error', '用户删除失败')
  })
}

function handleSuccess(file) {
  files.value.push(file.avatar);
  form.avatar = file.avatar;
  showMessage('success', '头像上传成功')
}

function handleError(err) {
  showMessage('error', '头像上传失败')
}

const handleExceed = (files) => {
  upload.value.clearFiles()
  const file = files[0]
  file.uid = genFileId()
  upload.value.handleStart(file)
  upload.value.submit()
}

const handleClose = () => {
  upload.value.clearFiles()
}


const updateUser = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    update_user(selectUserID.value, form).then(res => {
      showMessage('success', '修改用户信息成功!');
      store.updateUser(res.data);
      editDialog.value = false;
    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}

</script>


<template>
  <div class="datas-container">
    <el-table :data="store.users" style="width: 100%" border :height="windowHeight">
      <el-table-column label="用户编号" prop="id" align="center" fixed="left" width="100"/>
      <el-table-column label="用户名称" prop="username" align="center" width="200" fixed="left"/>
      <el-table-column label="用户角色" prop="role" align="center" width="160">
        <template #default="{row}">
          <el-tag type="success" round>{{ row.role }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="用户头像" prop="avatar" align="center" width="100">
        <template #default="{row}">
          <el-avatar
              :size="50"
              :src="calcAvatar(row.avatar)"
              shape="circle"
          />
        </template>
      </el-table-column>
      <el-table-column label="创建时间" prop="created_at" align="center" width="240"/>
      <el-table-column label="更新时间" prop="updated_at" align="center" width="240"/>
      <el-table-column align="center" fixed="right" width="240">
        <template #header>
          <el-input v-model="search" placeholder="搜索用户"/>
        </template>
        <template #default="scope">
          <el-button type="warning" round :disabled="scope.row.username === 'root'" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-popconfirm title="确定要删除吗?" confirm-button-text="确定" cancel-button-text="取消" width="300">
            <template #reference>
              <el-button type="danger" round :disabled="scope.row.role === '超级管理员'" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <el-dialog
      v-model="editDialog"
      title="修改用户信息"
      width="75%"
      @closed="handleClose"
  >
    <el-form ref="formRef" :model="form" :rules="rules" style="max-width:100%;" label-width="auto" label-position="left">
      <el-form-item style="margin-top:20px;" prop="role_id" label="用户角色">
        <el-select v-model="form.role_id" style="width: 200px;">
          <el-option v-for="role in roles_store.roles" :key="role.id" :label="role.name" :value="role.id"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item style="margin-top:10px;" prop="username" label="用户名">
        <el-input v-model="form.username" class="w-50 m-2" placeholder="用户名" size="large" type="text" style="width:50%;"/>
      </el-form-item>
      <el-row>
        <el-col :span="6" style="display: flex;align-items: center;justify-content: center;flex-direction: column;">
          <el-avatar
              :src="calcAvatar(editData.avatar)"
              :size="150"
              shape="square"
          />
          <div>现有头像</div>
        </el-col>
        <el-col :span="12" style="display: flex;align-items: center;justify-content: center;">
          <el-form-item style="margin-top:10px;" prop="avatar" label="头像">
            <el-upload
                ref="upload"
                :action="upload_api"
                list-type="picture-card"
                :auto-upload="true"
                :show-file-list="true"
                :v-model="files"
                :limit="1"
                :onSuccess="handleSuccess"
                :onError="handleError"
                :onExceed="handleExceed"
                accept="image/*"
            >
              <el-icon>
                <Plus/>
              </el-icon>
              <template #file="{ file }">
                <div>
                  <img class="el-upload-list__item-thumbnail" :src="file.url" alt=""/>
                </div>
              </template>
            </el-upload>
          </el-form-item>
        </el-col>
      </el-row>

      <el-form-item style="margin-top:100px;" type="submit">
        <el-button type="primary" @click="updateUser(formRef)" plain style="width: 100%;"
                   size="large" round>更新用户信息
        </el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>


<style scoped>
.datas-container {
  width: 98%;
  margin: 10px auto;
}
</style>