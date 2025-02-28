<script setup>
import {defineProps, ref} from "vue";
import {calcFile} from "../../utils/common.js";
import {View} from "@element-plus/icons-vue";
import AlumnusDetail from '../../components/cards/AlumnusDetail.vue'

const props = defineProps(['alumnus'])
const windowHeight = window.innerHeight - 180

const viewData = ref({})
const viewDialog = ref(false)

const handleView = (index, row) => {
  viewData.value = row
  viewDialog.value = true
}


</script>

<template>
  <div class="container">
    <div class="carousel-area">
      <div class="carousel-container">
        <el-table :data="props.alumnus" style="width: 100%" border :height="windowHeight">
          <el-table-column label="校友编号" prop="id" align="center" fixed="left" width="100"/>
          <el-table-column label="校友ID" prop="alumnus_id" align="center" fixed="left" width="200"/>
          <el-table-column label="校友头像" prop="photo" align="center" width="110">
            <template #default="{row}">
              <el-image
                  v-if="row.photo.length > 0"
                  :src="calcFile(row.photo)"
                  loading="lazy"
                  style="width:40px;height: 40px;border-radius: 50%;"
              />
              <el-tag v-else type="warning" round>暂时未上传</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="校友姓名" prop="alumnus_name" align="center" width="200"/>
          <el-table-column label="校友性别" prop="alumnus_gender" align="center" width="100"/>
          <el-table-column label="校友生日" prop="birthday" align="center" width="200"/>
          <el-table-column label="校友国籍" prop="nationality" align="center" width="200"/>
          <el-table-column label="校友民族" prop="nation" align="center" width="200"/>
          <el-table-column label="校友学号" prop="student_number" align="center" width="200"/>
          <el-table-column label="校友籍贯" prop="native_place" align="center" width="400">
            <template #default="{row}">
              <el-text truncated>{{ row.native_place }}</el-text>
            </template>
          </el-table-column>
          <el-table-column align="center" fixed="right" width="120" label="相关操作">
            <template #default="scope">
              <el-button type="success" round @click="handleView(scope.$index, scope.row)" :icon="View">查看</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div style="display: flex;align-items: center;justify-content: center;margin-top: 10px;">
          {{ props.alumnus.length }} 条搜索结果
        </div>
      </div>
    </div>
  </div>

  <el-dialog
      v-model="viewDialog"
      title="校友信息详情"
      width="75%"
  >
    <AlumnusDetail :data="viewData"/>
  </el-dialog>
</template>

<style scoped>
.container {
  width: 98%;
  height: 100%;
  margin: 10px auto;
}

.carousel-area {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-container {
  width: 100%;
  height: 96%;
  border: 1px solid lightgrey;
}


</style>