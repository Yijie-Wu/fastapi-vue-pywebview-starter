<script setup>
import {ref, reactive} from "vue";
import {add_year} from "../../../apis/year.js";
import {showMessage} from "../../../utils/message.js";
import {useRouter} from "vue-router";

const formRef = ref(null)
const router = useRouter()
const form = reactive({
  year_name: '',
})

const rules = reactive({
  year_name: [
    {required: true, message: '年份不能为空', trigger: 'blur'}
  ],
})

const createYear = (formEl) => {
  formEl.validate(valid => {
    if (!valid) {
      return false
    }

    add_year(form).then(res => {
      showMessage('success', '添加年份成功')
      router.push('/admin/year/list')
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
            <span>创建新年份</span>
          </div>
        </template>
        <el-row :gutter="10">
          <el-col :span="24">
            <el-form-item style="margin-top:10px;" prop="year_name" label="年份">
              <el-date-picker
                  v-model="form.year_name"
                  type="year"
                  placeholder="选择年份"
                  style="width: 40%;min-width:240px;"
                  value-format="YYYY"
              />
            </el-form-item>
          </el-col>
        </el-row>
      </el-card>

      <el-form-item style="margin:50px 0;" type="submit">
        <el-button type="primary" @click="createYear(formRef)" plain style="width: 100%;" size="large" round>创建新年份</el-button>
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