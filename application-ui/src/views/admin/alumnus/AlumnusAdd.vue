<script setup>
import {ref, reactive} from "vue";
import {useRouter} from "vue-router";
import {add_alumnus} from "../../../apis/alumnus.js"
import {showMessage} from "../../../utils/message.js"
import {genFileId} from "element-plus";
import {Plus} from "@element-plus/icons-vue";

const formRef = ref(null)
const router = useRouter()
const files = ref([])
const upload = ref(null)
const alumnus_genders = ['男', '女']
const politics_status = ['群众', '共青团员', '中共党员', '其他']
const upload_api = 'http://127.0.0.1:8000/upload/file'

const form = reactive({
  alumnus_id: '',//校友ID
  alumnus_name: '',//姓名
  alumnus_gender: '',//性别
  birthday: '',//出生日期
  nationality: '',//国籍
  native_place: '',// 籍贯
  nation: '',//民族
  politics_status: '',// 政治面貌
  address: '', // 通讯地址
  enrollment_year: '',// 入学年份
  graduation_year: '',//毕业年份
  student_number: '',//学号
  department: '',//院系
  major: '',//专业
  class_name: '',//班级
  school_name: '', //学校名称
  photo: '',//证件照
  description: '' // 个人描述信息
})

const rules = reactive({
  alumnus_id: [
    {required: true, message: '校友ID不能为空', trigger: 'blur'},
    {min: 1, max: 30, message: '校友ID长度必须在1到30之间', trigger: 'blur'},
  ],
  alumnus_name: [
    {required: true, message: '校友名称不能为空', trigger: 'blur'},
    {min: 2, max: 50, message: '校友名称长度必须在2到50之间', trigger: 'blur'},
  ],
  alumnus_gender: [
    {required: true, message: '校友性别不能为空', trigger: 'blur'},
  ],
  birthday: [
    {required: true, message: '校友生日不能为空', trigger: 'blur'},
  ],
  nationality: [
    {required: true, message: '校友国籍不能为空', trigger: 'blur'},
    {min: 2, max: 20, message: '校友国籍长度必须在2到20之间', trigger: 'blur'},
  ],
  native_place: [
    {min: 2, max: 100, message: '校友籍贯长度必须在2到100之间', trigger: 'blur'}
  ],
  nation: [
    {min: 1, max: 10, message: '校友民族长度必须在1到10之间', trigger: 'blur'}
  ],
  politics_status: [
    {required: true, message: '校友政治面貌不能为空', trigger: 'blur'},
  ],
  photo: [
    {required: true, message: '请上传校友照片', trigger: 'blur'},
  ],
})


function handleSuccess(file) {
  files.value.push(file.filename);
  form.photo = file.filename;
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

const createAlumnus = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    add_alumnus(form).then(res => {
      showMessage('success', '添加校友成功')
      router.push('/admin/alumnus')
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
            <span>个人基本信息</span>
          </div>
        </template>
        <el-row :gutter="10">
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="alumnus_id" label="校友ID">
              <el-input v-model="form.alumnus_id" class="w-50 m-2" placeholder="校友ID" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="alumnus_name" label="校友姓名">
              <el-input v-model="form.alumnus_name" class="w-50 m-2" placeholder="校友姓名" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="alumnus_gender" label="校友性别">
              <el-select
                  v-model="form.alumnus_gender"
                  placeholder="选择校友性别"
                  size="large"
                  style="width: 40%;min-width:240px;"
              >
                <el-option
                    v-for="item in alumnus_genders"
                    :key="item"
                    :label="item"
                    :value="item"
                />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="birthday" label="校友生日">
              <el-date-picker
                  v-model="form.birthday"
                  type="date"
                  placeholder="选择校友生日"
                  style="width: 40%;min-width:240px;"
                  value-format="YYYY-MM-DD"
              />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="nationality" label="校友国籍">
              <el-input v-model="form.nationality" class="w-50 m-2" placeholder="校友国籍" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="nationality" label="校友民族">
              <el-input v-model="form.nation" class="w-50 m-2" placeholder="校友民族" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="politics_status" label="政治面貌">
              <el-select
                  v-model="form.politics_status"
                  placeholder="选择政治面貌"
                  size="large"
                  style="width: 40%;min-width:240px;"
              >
                <el-option
                    v-for="item in politics_status"
                    :key="item"
                    :label="item"
                    :value="item"
                />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="photo" label="校友照片">
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
            <el-form-item style="margin-top:10px;" prop="native_place" label="校友籍贯">
              <el-input v-model="form.native_place" class="w-50 m-2" placeholder="校友籍贯" size="large" type="text"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="address" label="通讯地址">
              <el-input v-model="form.address" class="w-50 m-2" placeholder="通讯地址" size="large" type="text"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="school_name" label="学校名称">
              <el-input v-model="form.school_name" class="w-50 m-2" placeholder="学校名称" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="enrollment_year" label="入学年份">
              <el-date-picker
                  v-model="form.enrollment_year"
                  type="year"
                  placeholder="选择入学年份"
                  style="width: 40%;min-width:240px;"
                  value-format="YYYY"
              />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="graduation_year" label="毕业年份">
              <el-date-picker
                  v-model="form.graduation_year"
                  type="year"
                  placeholder="选择毕业年份"
                  style="width: 40%;min-width:240px;"
                  value-format="YYYY"
              />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="student_number" label="校友学号">
              <el-input v-model="form.student_number" class="w-50 m-2" placeholder="校友学号" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="department" label="校友院系">
              <el-input v-model="form.department" class="w-50 m-2" placeholder="校友院系" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="major" label="校友专业">
              <el-input v-model="form.major" class="w-50 m-2" placeholder="校友专业" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="class_name" label="校友班级">
              <el-input v-model="form.class_name" class="w-50 m-2" placeholder="校友班级" size="large" type="text" style="width: 40%;min-width:240px;"/>
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="description" label="个人简介">
              <el-input v-model="form.description" class="w-50 m-2" placeholder="个人简介" size="large" type="textarea" rows="4"/>
            </el-form-item>
          </el-col>
        </el-row>
      </el-card>

      <el-form-item style="margin:50px 0;" type="submit">
        <el-button type="primary" @click="createAlumnus(formRef)" plain style="width: 100%;" size="large" round>创建新校友</el-button>
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

.mt-1 {
  margin-top: 1rem;
}


</style>