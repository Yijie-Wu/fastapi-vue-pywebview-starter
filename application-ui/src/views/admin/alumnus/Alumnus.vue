<script setup>
import {ref, onMounted, computed} from "vue";

import {get_alumnus, search_alumnus, delete_alumnus} from "../../../apis/alumnus.js";
import {useAllAlumnusStore} from "../../../stores/admin/alumnus.js";
import {showMessage} from "../../../utils/message.js";
import {calcAvatar, calcFile} from "../../../utils/common.js";
import {Search, Close} from "@element-plus/icons-vue";
import AlumnusDetail from '../../../components/cards/AlumnusDetail.vue'
import AlumnusEdit from '../../../components/cards/AlumnusEdit.vue'

const store = useAllAlumnusStore()
const search = ref('')
const searchType = ref('姓名')
const searchMode = ref(false)
const searchResult = ref([])
const viewDialog = ref(false)
const editDialog = ref(false)
const windowHeight = window.innerHeight - 150
const currentPage = ref(1);
const limit = ref(10);
const count = ref(null);
const viewData = ref({})
const editData = ref({})

onMounted(() => {
  get_alumnus(0, limit.value).then(res => {
    store.setAlumnus(res.data.data);
    count.value = res.data.total;
  }).catch(err => {
    showMessage('error', '获取校友列表失败')
  })
})

const fetchItems = (page) => {
  const skip = (page - 1) * limit.value;
  get_alumnus(skip, limit.value).then(res => {
    store.setAlumnus(res.data.data);
    count.value = res.data.total;
  }).catch(err => {
    showMessage('error', '获取校友列表失败')
  })
};

const handlePageChange = (page) => {
  currentPage.value = page;
  fetchItems(page);
};

const handleSearch = () => {
  if (search.value.trim() === '') {
    showMessage('warning', '请输入搜索字符串')
    return
  }

  let data = {
    search_by: searchType.value,
    q: search.value
  }

  search_alumnus(data).then(res => {
    searchResult.value = res.data;
    searchMode.value = true
  }).catch(err => {
    showMessage('error', '搜索出错')
  })
}

const handleClearSearch = () => {
  searchMode.value = false
  search.value = ''
}

const handleView = (index, row) => {
  viewData.value = row
  viewDialog.value = true
}

const handleEdit = (index, row) => {
  editDialog.value = true
  editData.value = row
}

const handleDelete = (index, row) => {
  delete_alumnus(row.id).then(res => {
    store.removeAlumnus(row.id);
    showMessage('success', '删除校友成功')
  }).catch(err => {
    showMessage('error', '删除校友失败')
  })
}

</script>


<template>
  <div class="search-container">
    <el-input
        v-model="search"
        placeholder="搜索校友"
        style="width:80%;">
      <template #prepend>
        <el-select v-model="searchType" placeholder="Select" style="width: 80px">
          <el-option label="姓名" value="姓名"/>
          <el-option label="学号" value="学号"/>
        </el-select>
      </template>

    </el-input>
    <el-button style="margin-left: 20px;" :icon="Search" type="success" round @click="handleSearch();">搜索</el-button>
    <el-button type="warning" :icon="Close" round @click="handleClearSearch();" :disabled="!searchMode">清除</el-button>
  </div>
  <div class="datas-container" v-show="!searchMode">
    <el-table :data="store.alumnuss" style="width: 100%" border :height="windowHeight">
      <el-table-column label="校友编号" prop="id" align="center" fixed="left" width="100"/>
      <el-table-column label="校友ID" prop="alumnus_id" align="center" fixed="left" width="200"/>
      <el-table-column label="校友头像" prop="photo" align="center" width="100">
        <template #default="{row}">
          <el-image
              :src="calcFile(row.photo)"
              loading="lazy"
              style="width:30px;height: 30px;border-radius: 50%;"
          />
        </template>
      </el-table-column>
      <el-table-column label="校友姓名" prop="alumnus_name" align="center" width="200"/>
      <el-table-column label="校友性别" prop="alumnus_gender" align="center" width="100"/>
      <el-table-column label="校友国籍" prop="nationality" align="center" width="200"/>
      <el-table-column label="校友民族" prop="nation" align="center" width="200"/>
      <el-table-column label="校友学号" prop="student_number" align="center" width="200"/>
      <el-table-column label="校友籍贯" prop="native_place" align="center" width="400">
        <template #default="{row}">
          <el-text truncated>{{ row.native_place }}</el-text>
        </template>
      </el-table-column>
      <el-table-column align="center" fixed="right" width="240" label="相关操作">
        <template #default="scope">
          <el-button type="success" round @click="handleView(scope.$index, scope.row)">查看</el-button>
          <el-button type="warning" round :disabled="scope.row.username === 'root'" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-popconfirm title="确定要删除吗?" @confirm="handleDelete(scope.$index, scope.row)" confirm-button-text="确定" cancel-button-text="取消" width="300">
            <template #reference>
              <el-button type="danger" round :disabled="scope.row.role === '超级管理员'">删除</el-button>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
  </div>
  <div class="datas-container" v-show="searchMode">
    <el-table :data="searchResult" style="width: 100%" border :height="windowHeight">
      <el-table-column label="校友编号" prop="id" align="center" fixed="left" width="100"/>
      <el-table-column label="校友ID" prop="alumnus_id" align="center" fixed="left" width="200"/>
      <el-table-column label="校友头像" prop="photo" align="center" width="100">
        <template #default="{row}">
          <el-avatar
              :size="50"
              :src="calcFile(row.photo)"
              shape="circle"
          />
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
      <el-table-column align="center" fixed="right" width="240" label="相关操作">
        <template #default="scope">
          <el-button type="success" round @click="handleView(scope.$index, scope.row)">查看</el-button>
          <el-button type="warning" round :disabled="scope.row.username === 'root'" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-popconfirm title="确定要删除吗?" @confirm="handleDelete(scope.$index, scope.row)" confirm-button-text="确定" cancel-button-text="取消" width="300">
            <template #reference>
              <el-button type="danger" round :disabled="scope.row.role === '超级管理员'">删除</el-button>
            </template>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
  </div>
  <div class="pagination-container" v-show="!searchMode">
    <el-pagination
        background
        layout="prev, pager, next"
        :total="count"
        prev-text="上一页"
        next-text="下一页"
        :current-page="currentPage"
        :page-size="limit"
        @current-change="handlePageChange"
    />
  </div>
  <div class="pagination-container" v-show="searchMode">
    {{ searchResult.length }} 条搜索结果
  </div>

  <el-dialog
      v-model="viewDialog"
      title="校友信息详情"
      width="75%"
  >
    <AlumnusDetail :data="viewData"/>
  </el-dialog>

  <el-dialog
      v-model="editDialog"
      title="修改校友信息"
      width="75%"
  >
    <AlumnusEdit :data="editData"/>
  </el-dialog>
</template>


<style scoped>

.search-container {
  width: 98%;
  margin: 10px auto;
  height: 50px;
  border: none;
  background-color: #09ECEC66;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 25px;
}

.datas-container {
  width: 98%;
  margin: 10px auto;
}

.pagination-container {
  height: 40px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}


</style>