<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from 'vue-router';
import {search_alumnus} from "../../apis/alumnus.js";
import {get_show_carousels} from "../../apis/carousel.js";
import {useCarouselsStore} from "../../stores/main/carousel.js";
import {showMessage} from "../../utils/message.js";
import LogoMain from "../../components/basic/LogoMain.vue";
import MainSearch from "../../components/cards/MainSearch.vue"
import MainIndexPeoples from "../../components/cards/MainIndexPeoples.vue"
import MainMenuAvatar from "../../components/avatar/MainMenuAvatar.vue";
import {Search, Close, Refresh, Postcard, Picture} from "@element-plus/icons-vue";

const router = useRouter()
const searchMode = ref(false)
const searchResult = ref([])
const searchText = ref('');
const in_search = ref(false)
const searching = ref('搜索')
const carousel_store = useCarouselsStore()


onMounted(() => {
  get_show_carousels().then(res => {
    carousel_store.setCarousels(res.data);
  }).catch(err => {
    showMessage('error', '获取轮播列表失败')
  })
})

const startSearch = () => {
  if (searchText.value.trim() === '') {
    showMessage('warning', '请输入最少一个字符');
    return
  }

  searching.value = '搜索中...'
  in_search.value = true

  let data = {
    search_by: '姓名',
    q: searchText.value
  }

  search_alumnus(data).then(res => {
    searchResult.value = res.data;
    searchMode.value = true;
    searching.value = '搜索'
    in_search.value = false
  }).catch(err => {
    searching.value = '搜索'
    in_search.value = false
    showMessage('error', '搜索出错');
  })
}

const clearSearch = () => {
  searchMode.value = false;
  in_search.value = false
  searchText.value = '';
  searchResult.value = []
  searching.value = '搜索'
}

const refreshIndexPage = () => {
  router.go(0);
  showMessage('success', '刷新成功');
}

</script>

<template>
  <div class="main-container">
    <div class="main-head">
      <el-row class="main-nav">
        <el-col :xs="3" :sm="2" :md="2" :lg="6" :xl="6">
          <div class="logo-container">
            <LogoMain/>
          </div>
        </el-col>
        <el-col :xm="8" :sm="6" :md="10" :lg="9" :xl="9">
          <div class="menu-container">
            <el-input
                v-model="searchText"
                style="height: 40px;border-radius: 20px;"
                :prefix-icon="Postcard"
                placeholder="请输入校友姓名, 并点击搜索按钮"
                clearable
            ></el-input>
          </div>
        </el-col>
        <el-col :xm="13" :sm="16" :md="12" :lg="9" :xl="9">
          <div class="nav-user-area">
            <div>
              <el-button type="success" round :disabled="in_search == true" :icon="Search" @click="startSearch();">{{searching}}</el-button>
              <el-button type="warning" round :icon="Close" :disabled="!searchMode" @click="clearSearch();">清除</el-button>
              <el-button type="primary" round :icon="Refresh" @click="refreshIndexPage();">刷新</el-button>
              <el-button type="info" round :icon="Picture" @click="router.push('/old-photos');" style="margin-right: 20px;">老照片</el-button>
            </div>
            <MainMenuAvatar/>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="main-body">
      <MainSearch v-if="searchMode" :alumnus="searchResult"/>
      <MainIndexPeoples v-else :carousels="carousel_store.carousels"/>
    </div>
  </div>

</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background: linear-gradient(90deg, rgba(243, 198, 16, 0.76) 40%, rgba(123, 239, 105, 0.4) 60%);
}

.main-head {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  height: 80px;
}

.main-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: calc(100vh - 80px);
  overflow-y: scroll;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-nav {
  height: 60px;
  margin: 10px;
  padding: 0 10px;
  border-radius: 30px;
  box-sizing: border-box;
  background-color: rgba(255,255,255,0.1);
  box-shadow: 20px 20px 50px rgba(0,0,0,0.5);
    /* 背景模糊 */
  backdrop-filter: blur(5px);
}

.nav-user-area {
  display: flex;
  justify-content: flex-end;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.logo-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin: 0;
  padding: 0;
  height: 60px;
  box-sizing: border-box;
}

.menu-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin: 0;
  padding: 0;
  height: 60px;
  box-sizing: border-box;
}

.nav-user-area {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin: 0;
  padding-left: 15px;
  height: 60px;
  box-sizing: border-box;
}

</style>
