<script setup>
import {ref, onMounted, computed} from "vue";
import {Search} from "@element-plus/icons-vue";
import {useRouter} from 'vue-router'
import {get_years_photos_message, get_year_photos_message, search_photos} from "@/apis/message.js";
import {showMessage} from "@/utils/message.js";
import {calcFile} from "@/utils/common.js";

const search = ref('');
const viewMode = ref('年份模式');
const searchCurrent = ref('');
const current_year = ref('');
const route = useRouter();
const viewPhotos = ref([])
const years = ref([])
const view_photo = ref(false)
const current_view_image = ref('')
const current_view_image_name = ref('')

const searchPhoto = () => {
  if (search.value.trim().length === 0) {
    showMessage('error', '请至少输入一个非空字符串')
    return
  }
  viewMode.value = '搜索模式'
  search_photos(search.value.trim()).then(res => {
    viewPhotos.value = res.data.old_photos
  }).catch(err => {
    showMessage('error', '搜索照片信息失败')
    viewPhotos.value = []
  })

}

const getYearPhoto = (ye) => {
  viewMode.value = '年份模式';
  current_year.value = ye;
  get_year_photos_message(current_year.value.year_id).then(res => {
    viewPhotos.value = res.data.old_photos
  }).catch(err => {
    showMessage('error', '获取照片信息失败')
  })
}

const handleViewPhoto = (name, store) => {
  current_view_image.value = store
  current_view_image_name.value = name
  view_photo.value = true
}


onMounted(() => {
  get_years_photos_message().then(res => {
    years.value = res.data;
    if (years.value.length > 0) {
      current_year.value = years.value[0]

      get_year_photos_message(current_year.value.year_id).then(res => {
        viewPhotos.value = res.data.old_photos
      }).catch(err => {
        showMessage('error', '获取照片信息失败')
      })
    }
  }).catch(err => {
    showMessage('error', '获取年份照片信息失败')
  })
})

const filteredList = computed(() => {
  if (!searchCurrent.value) {
    // 如果搜索框为空，返回所有列表
    return viewPhotos.value;
  }
  // 返回匹配的项，使用 `toLowerCase` 以进行不区分大小写的比较
  return viewPhotos.value.filter(item =>
      item.original_name.toLowerCase().includes(searchCurrent.value.toLowerCase())
  );
})

</script>

<template>
  <div class="container">
    <div class="aside">
      <div class="aside-header">
        <el-input v-model="search" size="large" :prefix-icon="Search" placeholder="搜索老照片" style="width: 160px;margin-left: 3px;"/>
        <el-button type="primary" size="large" style="margin-left: 5px;" @click="searchPhoto();">搜索</el-button>
      </div>
      <div class="aside-body">
        <el-badge
            :value="ye.old_photos_count"
            :class="['year-container', { 'year-active': current_year.year_id === ye.year_id }]"
            :offset="[-28, 12]"
            type="success"
            v-for="ye in years" @click="getYearPhoto(ye);"
        >
          <div>
            <img src="@/assets/image/oldpic.png" alt="" style="width: 64px;height: 36px;border-radius: 3px;"/>
          </div>
          <div>
            <h4 style="margin-left: 10px;" v-if="ye.year_name === '1964' || ye.year_name === '1965'">{{ ye.year_name }} 级老照片</h4>
            <h4 style="margin-left: 10px;" v-else>{{ ye.year_name }} 届老照片</h4>
          </div>
        </el-badge>
      </div>
    </div>
    <div class="images-container">
      <div class="photo-menu">
        <div>
          <el-input v-model="searchCurrent" size="large" :prefix-icon="Search" placeholder="搜索当前页老照片"/>
        </div>
        <div style="display: flex;">
          <el-tag type="primary">{{ viewMode }}</el-tag>
          <div v-if="current_year.year_name === '1964' || current_year.year_name === '1965'">
            <el-tag type="info" v-if="viewMode==='年份模式'" style="margin-left: 10px;">{{ current_year.year_name }}级老照片,共{{ current_year.old_photos_count }}张</el-tag>
            <el-tag type="warning" v-else style="margin-left: 10px;">[{{ search }}]的老照片搜索结果,共{{ viewPhotos.length }}张</el-tag>
          </div>
          <div v-else>
            <el-tag type="info" v-if="viewMode==='年份模式'" style="margin-left: 10px;">{{ current_year.year_name }}届老照片,共{{ current_year.old_photos_count }}张</el-tag>
            <el-tag type="warning" v-else style="margin-left: 10px;">[{{ search }}]的老照片搜索结果,共{{ viewPhotos.length }}张</el-tag>
          </div>
        </div>
        <div>
          <el-button round type="warning" @click="route.go(0)" style="margin-right: 3px;">刷新页面</el-button>
          <el-button round type="primary" @click="route.push('/')" style="margin-right: 3px;">返回首页</el-button>
        </div>
      </div>
      <div style="height: calc(100vh - 60px);overflow-y: scroll;">
        <el-row>
          <el-col :span="8" style="margin-top: 5px;" v-for="p in filteredList">
            <div style="width: 100%;display: flex;align-items: center;justify-content: center;flex-direction: column;">
              <div>
                <el-image
                    :src="calcFile(p.store_name)"
                    alt="老照片"
                    style="height: 240px;width: 100%;"
                    loading="lazy"
                    @click="handleViewPhoto(p.original_name, p.store_name)"
                />
              </div>
              <div>
                <el-text truncated>{{ p.original_name }}</el-text>
              </div>
            </div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>

  <el-dialog
      v-model="view_photo"
      :title="current_view_image_name"
      width="80%"
      align-center
  >
    <div>
      <el-image
            :src="calcFile(current_view_image)"
            alt="老照片"
            style="max-width: 100%;"
            loading="lazy"
        />
    </div>
  </el-dialog>
</template>


<style scoped>
.container {
  width: 100vw;
  height: 100vh;
  display: flex;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.aside {
  height: 100%;
  width: 240px;
  border-right: 1px solid lightgrey;
}

.aside-header {
  width: 100%;
  height: 60px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid lightgrey;
}

.aside-body {
  margin: 0;
  padding: 0;
  height: calc(100vh - 65px);
  width: 100%;
  overflow-y: scroll;
}


.year-container {
  height: 50px;
  margin: 3px;
  width: 226px;
  border: 1px solid lightgrey;
  padding: 3px;
  border-radius: 3px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.year-active {
  background-color: #06f5b5;
}


.images-container {
  height: calc(100vh - 10px);
  width: calc(100vw - 260px);
  margin: 0 auto;
}

.photo-menu {
  height: 50px;
  border: 1px solid lightgrey;
  background-color: rgba(240, 210, 13, 0.23);
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: 25px;
  margin-top: 5px;
  padding: 0 20px;
}

</style>
