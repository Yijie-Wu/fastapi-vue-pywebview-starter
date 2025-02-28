<script setup>
import {ref, reactive} from "vue";
import {useRouter} from "vue-router";
import {Plus} from "@element-plus/icons-vue";
import {showMessage} from "../../../utils/message.js";
import {genFileId} from "element-plus";
import {add_carousels} from "../../../apis/carousel.js";

const upload_api = 'http://127.0.0.1:8000/upload/file'
const files = ref([])
const upload = ref(null)
const formRef = ref(null)
const router = useRouter()

const form = reactive({
  store_name: '',
  desc: '',
  show: false
})

const rules = reactive({
  store_name: [
    {required: true, message: '请上传轮播图片', trigger: 'blur'}
  ],
  desc: [
    {min: 0, max: 100, message: '描述不能超过100个字符', trigger: 'blur'}
  ]
})


function handleSuccess(file) {
  files.value.push(file.filename);
  form.store_name = file.filename;
  showMessage('success', '上传轮播图片成功')
}

function handleError(err) {
  showMessage('error', '上传轮播图片失败')
}

const handleExceed = (files) => {
  upload.value.clearFiles()
  const file = files[0]
  file.uid = genFileId()
  upload.value.handleStart(file)
  upload.value.submit()
}


const createCarousel = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    add_carousels(form).then(res => {
      showMessage('success', '添加轮播成功')
      router.push('/admin/carousel/list')
    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}


</script>

<template>
  <div class="container">
    <el-form ref="formRef" :model="form" :rules="rules" style="width:100%;" label-width="auto" label-position="left">
      <el-card>
        <template #header>
          <div class="card-header">
            <span>创建新轮播</span>
          </div>
        </template>
        <el-row :gutter="10">
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="store_name" label="轮播照片">
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
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="desc" label="轮播描述">
              <el-input v-model="form.desc" class="w-50 m-2" placeholder="轮播描述" size="large" type="text"/>
            </el-form-item>
          </el-col>
          <el-form-item style="margin-top:10px;" prop="show" label="是否展示">
            <el-switch v-model="form.show" class="w-50 m-2" size="large"></el-switch>
          </el-form-item>
        </el-row>
      </el-card>

      <el-form-item style="margin:50px 0;" type="submit">
        <el-button type="primary" @click="createCarousel(formRef)" plain style="width: 100%;" size="large" round>创建新轮播</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>


<style scoped>
.container {
  width: 96%;
  margin: 10px auto;
  border-radius: 5px;
}
</style>