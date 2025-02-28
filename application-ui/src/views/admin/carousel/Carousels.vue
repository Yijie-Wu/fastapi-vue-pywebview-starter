<script setup>
import {ref, onMounted, computed, reactive} from "vue";

import {get_carousels, delete_carousels, update_carousels} from "../../../apis/carousel.js";
import {useAllCarouselsStore} from "../../../stores/admin/carousel.js";
import {showMessage} from "../../../utils/message.js";
import {Plus} from "@element-plus/icons-vue";
import {calcFile} from "../../../utils/common.js";

const store = useAllCarouselsStore()
const editDialog = ref(false)
const editData = ref({})
const formRef = ref(null)
const selectUserID = ref(0)
const windowHeight = window.innerHeight - 20

onMounted(() => {
  get_carousels().then(res => {
    store.setCarousels(res.data)
  }).catch(err => {
    showMessage('error', '获取轮播列表失败')
  })
})

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


const handleEdit = (index, row) => {
  editDialog.value = true
  editData.value = row
  form.store_name = row.store_name
  form.desc = row.desc
  form.show = row.show
  selectUserID.value = row.id
}

const handleDelete = (index, row) => {
  delete_carousels(row.id).then(res => {
    showMessage('success', '轮播删除成功')
    store.removeCarousels(row.id)
  }).catch(err => {
    showMessage('error', '轮播删除失败')
  })
}


const updateCarousel = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    update_carousels(selectUserID.value, form).then(res => {
      showMessage('success', '修改轮播信息成功!');
      store.updateCarousels(res.data);
      editDialog.value = false;
    }).catch(err => {
      showMessage('error', err.message)
    })
  })
}

</script>


<template>
  <div class="datas-container">
    <el-table :data="store.carousels" style="width: 100%" border :height="windowHeight">
      <el-table-column label="轮播编号" prop="id" align="center" fixed="left" width="100"/>
      <el-table-column label="轮播图" prop="avatar" align="center" width="100">
        <template #default="{row}">
          <el-image
              :size="80"
              :src="calcFile(row.store_name)"
              loading="lazy"
          />
        </template>
      </el-table-column>
      <el-table-column label="轮播描述" prop="desc" align="center"/>
      <el-table-column label="是否展示" prop="show" align="center" width="100"/>
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
      title="修改轮播信息"
      width="75%"
  >
    <div>
      <div>
        <el-image
            :src="calcFile(form.store_name)"
            style="height: 200px;"
        />
      </div>
      <div>
        <el-form ref="formRef" :model="form" :rules="rules" style="max-width:100%;" label-width="auto" label-position="left">
          <el-form-item style="margin-top:10px;" prop="desc" label="轮播描述">
            <el-input v-model="form.desc" class="w-50 m-2" placeholder="轮播描述" size="large" type="text"/>
          </el-form-item>
          <el-form-item style="margin-top:10px;" prop="show" label="是否展示">
            <el-switch v-model="form.show" class="w-50 m-2" size="large"></el-switch>
          </el-form-item>
          <el-form-item style="margin-top:100px;" type="submit">
            <el-button type="primary" @click="updateCarousel(formRef)" plain style="width: 100%;"
                       size="large" round>更新轮播信息
            </el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </el-dialog>
</template>


<style scoped>
.datas-container {
  width: 98%;
  margin: 10px auto;
}
</style>