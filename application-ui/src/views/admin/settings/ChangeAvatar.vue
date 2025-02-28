<script setup>
import {ref, onMounted, reactive} from "vue";
import {useUserStore} from "../../../stores/user/user.js";
import {change_avatar, get_userinfo} from '../../../apis/user.js'
import {calcAvatar} from "../../../utils/common.js";
import {showMessage} from "../../../utils/message.js";
import {useRouter} from "vue-router";
import {removeToken} from "../../../utils/token.js";
import {genFileId} from "element-plus";
import {Plus} from "@element-plus/icons-vue";

const store = useUserStore()
const user_id = ref(0)
const formRef = ref(null)
const upload = ref(null)
const files = ref([])
const router = useRouter()
const upload_api = 'http://127.0.0.1:8000/upload/user/avatar'

const form = reactive({
  avatar: '',
})

const rules = reactive({
  avatar: [
    {required: true, message: '请上传头像', trigger: 'blur'}
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


const updateAvatar = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    change_avatar(form).then(res => {
      showMessage('success', '修改头像成功!');
      store.userInfo.avatar = res.data.avatar
    }).catch(err => {
      showMessage('error', err.message)
    })
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
              <el-row>
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
                <el-col :span="12" v-if="form.avatar !== ''" style="display: flex;align-items: center;justify-content: center;flex-direction: column;">
                  <div>预览</div>
                  <el-avatar
                      :src="calcAvatar(form.avatar)"
                      :size="160"
                      shape="square"
                  />
                </el-col>
              </el-row>

              <el-form-item style="margin-top:100px;" type="submit">
                <el-button type="primary" @click="updateAvatar(formRef)" plain style="width: 100%;"
                           size="large" round>更新头像
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