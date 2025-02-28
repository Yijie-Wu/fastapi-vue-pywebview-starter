<script setup>
import {ref, onMounted, defineProps} from 'vue'
import {calcFile} from "../../utils/common.js";
import {Phone} from "@element-plus/icons-vue";

const props = defineProps(['data'])

</script>

<template>
  <el-card>
    <el-row :gutter="20">
      <el-col :span="6">
        <el-image
            v-if="props.data.photo.trim() !== ''"
            :src="calcFile(props.data.photo)"
            style="border: 1px solid lightgrey;border-radius: 8px;width: 100%;"
        />
        <el-empty description="照片暂未上传"/>
      </el-col>
      <el-col :span="18">
        <el-descriptions :title="props.data.alumnus_name" border>
          <el-descriptions-item label="性别">{{props.data.alumnus_gender}}</el-descriptions-item>
          <el-descriptions-item label="生日">{{props.data.birthday}}</el-descriptions-item>
          <el-descriptions-item label="校友ID">{{props.data.alumnus_id}}</el-descriptions-item>
          <el-descriptions-item label="国籍">
            <el-tag size="small">{{props.data.nationality}}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="民族">
            <el-tag size="small">{{props.data.nation}}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="政治面貌">
            {{props.data.politics_status}}
          </el-descriptions-item>
          <el-descriptions-item label="籍贯">
            {{props.data.native_place}}
          </el-descriptions-item>
        </el-descriptions>
        <el-descriptions title="其他信息" border style="margin-top: 20px;">
          <el-descriptions-item label="学校名称">{{props.data.school_name}}</el-descriptions-item>
          <el-descriptions-item label="入学年份">
            <el-tag size="small">{{props.data.enrollment_year}}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="毕业年份">
            <el-tag size="small">{{props.data.graduation_year}}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="学号">
            {{props.data.student_number}}
          </el-descriptions-item>
          <el-descriptions-item label="院系">
            {{props.data.department}}
          </el-descriptions-item>
          <el-descriptions-item label="专业">
            {{props.data.major}}
          </el-descriptions-item>
          <el-descriptions-item label="通讯地址">
            {{props.data.address}}
          </el-descriptions-item>
        </el-descriptions>
        <div style="margin-top: 15px;">
          <h3>个人简介</h3>
          <div>
            <el-input type="textarea" v-model="props.data.description" rows="3" disabled></el-input>
          </div>
        </div>

      </el-col>
    </el-row>
  </el-card>
</template>


<style scoped>
.detail-container {
  width: 100%;
}

.mt-5 {
  margin-top: 5px;
}

.mt-10 {
  margin-top: 10px;
}

.basic-avatar-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.basic-message-container {
  flex: 1;
  height: 170px;
  padding: 0 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}

.name {
  font-size: 20px;
  font-weight: bold;
}


</style>
