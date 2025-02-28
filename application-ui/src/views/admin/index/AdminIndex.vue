<script setup>
import {computed, onMounted, ref, onBeforeUnmount} from "vue";
import {showMessage} from "../../../utils/message.js";
import {useRouter} from 'vue-router'
import {get_admin_message} from "../../../apis/message.js";
import {Picture, User, Grape, Calendar, DocumentCopy} from "@element-plus/icons-vue";
import * as echarts from 'echarts';

const years_data = ref([])
const photo_data = ref([])

const route = useRouter();
const adminMessage = ref({})
const windowHeight = computed(() => {
  return window.innerHeight - 340
})

// 创建一个 ref 引用，用于绑定 ECharts 容器
const chartRef = ref(null);
let chartInstance = null;

// 初始化图表函数
const initChart = () => {
  // 初始化 ECharts 实例
  chartInstance = echarts.init(chartRef.value);
  let option = {
    title: {
      text: '历年老照片数量',
      subtext: '单位(张)'
    },
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['照片数量']
    },
    toolbox: {
      show: true,
      feature: {
        mark: {show: true},
        dataView: {show: true, readOnly: false},
        magicType: {show: true, type: ['line', 'bar']},
        restore: {show: true},
        saveAsImage: {show: true}
      }
    },
    calculable: true,
    xAxis: [
      {
        type: 'category',
        boundaryGap: false,
        data: years_data.value
      }
    ],
    yAxis: [
      {
        type: 'value',
        axisLabel: {
          formatter: '{value} 张'
        }
      }
    ],
    series: [
      {
        name: '照片数量',
        type: 'line',
        data: photo_data.value,
        markPoint: {
          data: [
            {type: 'max', name: '最大值'},
            {type: 'min', name: '最小值'}
          ]
        },
        markLine: {
          data: [
            {type: 'average', name: '平均值'}
          ]
        }
      },
    ],
    // 添加 dataZoom 组件
    dataZoom: [
      {
        type: 'slider', // 使用滑动条
        start: 0, // 初始起始位置百分比
        end: 100, // 初始结束位置百分比
        xAxisIndex: [0] // 作用于第一个 x 轴
      }
    ]
  };

  // 使用配置项填充图表
  chartInstance.setOption(option);
};

onMounted(() => {
  get_admin_message().then(res => {
    adminMessage.value = res.data;
    years_data.value = adminMessage.value.years_list;
    photo_data.value = adminMessage.value.photo_list;

    initChart();
  }).catch(err => {
    showMessage('error', '获取后台信息失败')
  })

  initChart();
})

// 在组件卸载时销毁 ECharts 实例
onBeforeUnmount(() => {
  if (chartInstance) {
    chartInstance.dispose();
  }
});


</script>

<template>
  <div class="adin-index-container">
    <el-row :gutter="10">
      <el-col :span="12">
        <div class="custom-card">
          <div style="display: flex;">
            <div style="width: 50%;">
              <img src="@/assets/image/users.webp" style="height: 200px;width: 100%;border-radius:10px;border: 1px solid lightgrey;" alt="">
            </div>
            <div style="display: flex;align-items: flex-start;justify-content: flex-start;width: 50%;flex-direction: column;margin:0 10px;">
              <div style="display: flex;align-items: center;justify-content: flex-end;width: 100%;">
                <el-button :icon="User" size="large" plain circle type="success" @click="route.push('/admin/users/list');"></el-button>
              </div>
              <div style="width: 100%;">
                <div>
                  <strong style="margin-right: 10px;">账号:</strong>
                  <el-tag type="warning">{{ adminMessage.admin_count }} 管理员</el-tag>
                  <el-tag style="margin-left: 10px;">{{ adminMessage.user_count }} 普通用户</el-tag>
                </div>
                <div style="margin-top: 20px;">
                  管理系统, 由您来绘制美丽的画卷, 一切美好, 都来自于最初的相识, 离别只是为了更好的相聚
                </div>
              </div>
            </div>
          </div>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="custom-card">
          <div style="display: flex;">
            <div style="width: 50%;">
              <img src="@/assets/image/alumnus.png" style="height: 200px;width: 100%;border-radius:10px;" alt="">
            </div>
            <div style="display: flex;align-items: flex-start;justify-content: flex-start;width: 50%;flex-direction: column;margin:0 10px;">
              <div style="display: flex;align-items: center;justify-content: flex-end;width: 100%;">
                <el-button :icon="Grape" size="large" plain circle type="success" @click="route.push('/admin/alumnus');"></el-button>
              </div>
              <div style="margin-top: 0px;width: 100%;">
                <div><strong>校友数量: {{ adminMessage.alumnus_count }} 人</strong></div>
                <div style="margin-top: 20px;">
                  时间苍老了青春、奋斗淹没了岁月, Hi, 校友, 他日我们必将相逢, 恰同学少年, 风华正茂, 书生义气, 挥斥方遒
                </div>
              </div>
            </div>
          </div>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="custom-card">
          <div style="display: flex;">
            <div style="width: 50%;">
              <img src="@/assets/image/oldpic.png" style="height: 200px;width: 100%;border-radius:10px;" alt="">
            </div>
            <div style="display: flex;align-items: flex-start;justify-content: flex-start;width: 50%;flex-direction: column;margin:0 10px;">
              <div style="display: flex;align-items: center;justify-content: flex-end;width: 100%;">
                <el-button :icon="Calendar" size="large" plain circle type="success" @click="route.push('/admin/year/list');"></el-button>
              </div>
              <div style="width: 100%;">
                <div><strong>老照片年数: {{ adminMessage.year_count }} 年, 共 <span style="color:#0dda91;">{{ adminMessage.photo_count }}</span> 张</strong></div>
                <div style="margin-top: 20px;">
                  回忆那段激情燃烧的水月, 历久弥新, 用不褪色
                </div>
              </div>
            </div>
          </div>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="custom-card">
          <div style="display: flex;">
            <div style="width: 50%;">
              <img src="@/assets/image/lb.png" style="height: 200px;width: 100%;border-radius:10px;border:1px solid lightgrey;" alt="">
            </div>
            <div style="display: flex;align-items: flex-start;justify-content: flex-start;width: 50%;flex-direction: column;margin:0 10px;">
              <div style="display: flex;align-items: center;justify-content: flex-end;width: 100%;">
                <el-button :icon="DocumentCopy" size="large" plain circle type="success" @click="route.push('/admin/carousel/list');"></el-button>
              </div>
              <div style="width: 100%;">
                <div><strong>首页轮播: {{ adminMessage.carousel_count }} 张</strong></div>
                <div style="margin-top: 20px;">
                  那些最值得回忆的时刻, 值得我们反复品味, 如老酒般历久弥香, 回味无穷
                </div>
              </div>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>

    <div ref="chartRef" style="width: 100%; height: 400px;border: 1px solid lightgrey;margin: 20px 0;border-radius: 5px;">1</div>


  </div>
</template>

<style scoped>
.adin-index-container {
  width: 98%;
  margin: 1px auto;
}

.custom-card {
  height: 200px;
  margin-top: 10px;
  border-radius: 5px;
  padding: 5px;
  background-color: rgba(255, 255, 255, 0.1);
  border: 1px solid lightgrey;
}


</style>