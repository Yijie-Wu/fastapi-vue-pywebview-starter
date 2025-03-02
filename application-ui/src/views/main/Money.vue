<script setup>
import {ref, onMounted, computed} from "vue";
import {Search, Money, SwitchButton, Remove} from "@element-plus/icons-vue";

const searchText = ref('')
const tableHeight = computed(() => {
  return window.innerHeight - 110;
})

const tableData = [
  {
    date: '2016-05-03',
    time: 'Tom',
    tf_flag: 'California',
    valuta: 'Los Angeles',
    fsn_count: 0,
    money_flag: [],
    char_num: 'CA 90036',
    sno: [],
    machine_sno:[],
    reserve1:0,
    image_sno:''
  },
]
</script>


<template>
  <div class="container">
    <div class="header">
      <div class="header-left">
        点钞历史记录
      </div>
      <div class="header-right">
        <div class="search-container">
          <el-input
              v-model="searchText"
              size="large"
              :prefix-icon="Money"
              :suffix-icon="Search"/>
        </div>
        <div class="function-area">
          <el-button :icon="SwitchButton" circle type="primary"></el-button>
          <el-button :icon="SwitchButton" circle type="primary"></el-button>
          <el-button :icon="Remove" circle type="danger"></el-button>
        </div>
      </div>
    </div>
    <div class="content">
      <el-table :data="tableData" border style="width: 100%" :height="tableHeight">
        <el-table-column prop="date" label="日期" width="150" fixed="left"/>
        <el-table-column prop="time" label="时间" width="120" fixed="left" />
        <el-table-column prop="tf_flag" label="真伪标志" width="120" fixed="left" />
        <el-table-column prop="valuta" label="币值" width="120" />
        <el-table-column prop="fsn_count" label="纸币计数" width="100" />
        <el-table-column prop="char_num" label="冠字号码字符数" width="130" />
        <el-table-column prop="sno" label="冠字号码" width="120" />
        <el-table-column prop="machine_sno" label="机具编号" width="120" />
        <el-table-column prop="reserve1" label="保留字" />
        <el-table-column fixed="right" prop="image_sno" label="图像冠字号码结构">
        </el-table-column>
      </el-table>
    </div>
    <div style="margin-top: 20px; display: flex; justify-content: center;align-items: center;width: 100%;">
      <el-pagination background layout="prev, pager, next" :total="1000"/>
    </div>
  </div>
</template>

<style scoped>
.container {
  height: 100%;
  width: 100%;
}

.header {
  height: 50px;
  border: 1px solid lightgray;
  margin-bottom: 10px;
  margin-top: 10px;
  display: flex;
  padding: 0 10px;
  align-items: center;
  border-radius: 10px;
}

.header-left {
  height: 100%;
  width: 140px;
  display: flex;
  align-items: center;
}

.header-right {
  height: 100%;
  flex: 1;
  display: flex;
  align-items: center;
}

.search-container {
  display: flex;
  align-items: center;
  height: 100%;
  flex: 1;
  padding: 0 15px;
}

.function-area {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  width: 200px;
  height: 100%;
}

.content {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  border-radius: 10px;
  height: calc(100vh - 140px);
}


</style>