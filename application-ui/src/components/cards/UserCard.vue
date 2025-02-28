<script setup>
import {defineProps, ref} from "vue";
import {calcFile} from "../../utils/common.js";

const props = defineProps(['info'])
import AlumnusDetail from '../../components/cards/AlumnusDetail.vue'

const carouselHeight = (window.innerHeight - 100) + 'px'
const viewData = ref({})
const viewDialog = ref(false)

const handleView = (data) => {
  viewData.value = data
  viewDialog.value = true
}

</script>

<template>
  <div class="user-card-container">
    <el-row :gutter="10" style="height: 100%;">
      <el-col :span="8" v-for="user in props.info" style="margin: 10px 0;height: 46%;">
        <el-card shadow="hover" @click="handleView(user)" style="background-color: rgb(125, 186, 152, 0.4);">
          <el-row :gutter="10" style="height: 100%;">
            <el-col :span="11" style="height: 100%;">
              <img :src="calcFile(user.photo)" class="avatar-image" alt=""/>
            </el-col>
            <el-col :span="13">
              <div>姓名: {{user.alumnus_name}}</div>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
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
.user-card-container {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.avatar-image {
  border: 1px solid lightgrey;
  border-radius: 5px;
  width: 100%;
  height: calc(50vh - 120px);
}


</style>