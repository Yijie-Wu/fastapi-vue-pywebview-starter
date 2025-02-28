<script setup>
import {ref, onMounted, computed, reactive} from "vue";

import {get_years, update_year, delete_year, update_year_photo, delete_year_photo} from "../../../apis/year.js";
import {useAllYearsStore} from "../../../stores/admin/year.js";
import {showMessage} from "../../../utils/message.js";
import {Plus} from "@element-plus/icons-vue";
import {calcFile} from "../../../utils/common.js";
import {genFileId} from "element-plus";
import {UploadFilled} from '@element-plus/icons-vue'

const store = useAllYearsStore()
const editDialog = ref(false)
const editPhotoDialog = ref(false)
const editPhotos = ref([])
const formRef = ref(null)
const photo_original_name = ref('')
const selectYearID = ref(0)
const selectPhotoID = ref(0)
const selectPhoto = ref('')
const windowHeight = window.innerHeight - 20
const upload_api = computed(() => {
  return 'http://127.0.0.1:8000/upload/old-photo/' + selectYearID.value
})
const files = ref([])
const upload = ref(null)

onMounted(() => {
  get_years().then(res => {
    store.setYears(res.data)
  }).catch(err => {
    showMessage('error', '获取年份列表失败')
  })
})

const form = reactive({
  year_name: '',
})

const rules = reactive({
  year_name: [
    {required: true, message: '年份不能为空', trigger: 'blur'}
  ],
})

const handleEdit = (index, row) => {
  editDialog.value = true
  form.year_name = row.year_name
  editPhotos.value = row.old_photos
  selectYearID.value = row.id
}

const handlePhotoEdit = (row) => {
  editPhotoDialog.value = true
  photo_original_name.value = row.original_name
  selectPhotoID.value = row.id
  selectPhoto.value = row.store_name
}

const handleDelete = (index, row) => {
  delete_year(row.id).then(res => {
    showMessage('success', '年份删除成功')
    store.removeYears(row.id)
  }).catch(err => {
    showMessage('error', '年份删除失败')
  })
}


const updateYear = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    update_year(selectYearID.value, form).then(res => {
      showMessage('success', '修改年份信息成功!');
      store.updateYears(res.data);
      editDialog.value = false;
    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}

function handleSuccess(file) {
  files.value.push(file.filename);
  editPhotos.value.push({
    'store_name': file.filename,
    'original_name': file.name,
    'id': file.id
  })
  showMessage('success', '照片上传成功')
}

function handleError(err) {
  showMessage('error', '照片上传失败')
}

const handleExceed = (fi) => {
  upload.value.clearFiles()
  const file = fi[0]
  file.uid = genFileId()
  upload.value.handleStart(file)
  upload.value.submit()
}


const editPhoto = () => {
  if (photo_original_name.value.length > 199) {
    showMessage('error', '照片原始名称不能超过200字符')
    return
  }

  let data = {'original_name': photo_original_name.value}

  update_year_photo(selectPhotoID.value, data).then(res => {
    showMessage('success', '更新照片信息成功!');
    store.updateYears(res.data);
    editPhotos.value = res.data.old_photos
    editPhotoDialog.value = false

  }).catch(err => {
    showMessage('error', err.message)
  })
}


const deletePhoto = (photo_id) => {
  delete_year_photo(photo_id).then(res => {
    showMessage('success', '删除照片成功!');
    store.updateYears(res.data);
    editPhotos.value = res.data.old_photos
  }).catch(err => {
    showMessage('error', err.message)
  })
}


</script>


<template>
  <div class="datas-container">
    <el-table :data="store.years" style="width: 100%" border :height="windowHeight">
      <el-table-column label="编号" prop="id" align="center" fixed="left" width="100"/>
      <el-table-column label="年份" prop="year_name" align="center" fixed="left" width="100"/>
      <el-table-column label="老照片数量" prop="old_photos" align="center" fixed="left">
        <template #default="scope">
          <el-button type="primary" plain round>{{ scope.row.old_photos.length }} 张老照片</el-button>
        </template>
      </el-table-column>
      <el-table-column align="center" fixed="right" label="操作" width="160">
        <template #default="scope">
          <el-button type="warning" round @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-popconfirm title="确定要删除吗?" @confirm="handleDelete(scope.$index, scope.row)" confirm-button-text="确定" cancel-button-text="取消" width="300">
            <template #reference>
              <el-button type="danger" round>删除</el-button>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <el-dialog
      v-model="editDialog"
      title="修改年份信息"
      width="75%"
  >
    <div>
      <el-form ref="formRef" :model="form" :rules="rules" style="max-width:100%;" label-width="auto" label-position="left">
        <el-form-item style="margin-top:10px;" prop="year_name" label="年份">
          <el-date-picker
              v-model="form.year_name"
              type="year"
              placeholder="选择年份"
              style="width: 40%;min-width:240px;"
              value-format="YYYY"
          />
        </el-form-item>
        <el-table :data="editPhotos" style="width: 100%" border :height="300">
          <el-table-column label="照片编号" prop="id" align="center" fixed="left" width="100"/>
          <el-table-column label="照片原名" prop="original_name" align="center" width="200"/>
          <el-table-column label="照片存储名称" prop="store_name" align="center"/>
          <el-table-column label="照片预览" prop="store_name" align="center" width="200">
            <template #default="{row}">
              <el-image
                  :src="calcFile(row.store_name)"
                  loading="lazy"
              />
            </template>
          </el-table-column>
          <el-table-column align="center" fixed="right" width="160" label="相关操作">
            <template #default="scope">
              <el-button type="warning" round :disabled="scope.row.username === '超级管理员'" @click="handlePhotoEdit(scope.row)">编辑</el-button>
              <el-popconfirm title="确定要删除吗?" @confirm="deletePhoto(scope.row.id)" confirm-button-text="确定" cancel-button-text="取消" width="300">
                <template #reference>
                  <el-button type="danger" round :disabled="scope.row.role === '超级管理员'">删除</el-button>
                </template>
              </el-popconfirm>
            </template>
          </el-table-column>
        </el-table>
        <div style="margin-top: 20px;">
          <el-upload
              ref="upload"
              :action="upload_api"
              :auto-upload="true"
              :show-file-list="false"
              :v-model="files"
              drag
              multiple
              :onSuccess="handleSuccess"
              :onError="handleError"
              :onExceed="handleExceed"
              accept="image/*"
          >
            <el-icon class="el-icon--upload">
              <upload-filled/>
            </el-icon>
            <div class="el-upload__text">
              拖拽照片到此, 或者 <em>点击上传</em>
            </div>
          </el-upload>
        </div>
        <el-form-item style="margin-top:10px;" type="submit">
          <el-button type="primary" @click="updateYear(formRef)" plain style="width: 100%;"
                     size="large" round>更新年份信息
          </el-button>
        </el-form-item>
      </el-form>
    </div>

    <el-dialog
        v-model="editPhotoDialog"
        width="80%"
        title="更新照片信息"
        append-to-body
    >
      <div>
        <div style="display: flex;align-items: center;justify-content: center;">
          <el-image :src="calcFile(selectPhoto)" style="height: 240px;max-width: 100%;" loading="lazy"/>
        </div>
        <div style="margin-top: 20px;">
          <h4>照片原始名称</h4>
          <el-input v-model="photo_original_name" size="large"/>
          <el-button type="success" size="large" style="margin-top: 20px; width:100%;" @click="editPhoto()">更新图片信息</el-button>
        </div>
      </div>
    </el-dialog>
  </el-dialog>
</template>


<style scoped>
.datas-container {
  width: 98%;
  margin: 10px auto;
}
</style>