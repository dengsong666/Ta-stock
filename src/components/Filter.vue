<script setup lang="ts">
import { useKChart } from '@/store'
const indicator = ['MACD', 'KDJ', 'RSI', 'BOLL', 'TD9', 'ENE']
const kChart = useKChart()
const visible = ref(false)
</script>

<template>
  <i @click="visible = true" class="i-my-filter"></i>
  <n-drawer v-model:show="visible" :default-width="500" resizable placement="left">
    <n-drawer-content title="指标">
      <n-checkbox-group class="mb16px" v-model:value="kChart.indicator.checked">
        <n-checkbox v-for="v in indicator" :value="v" :label="v" />
      </n-checkbox-group>
      <n-form ref="formRef" :model="kChart.indicator">
        <n-form-item v-show="kChart.indicator.checked.includes('KDJ')" label="KDJ">
          <n-slider v-model:value="kChart.indicator.kdj" :step="1" :max="30" />
        </n-form-item>
        <n-form-item v-show="kChart.indicator.checked.includes('BOLL')" label="BOLL">
          <n-slider v-model:value="kChart.indicator.boll" :step="1" :max="100" />
        </n-form-item>
        <n-form-item v-show="kChart.indicator.checked.includes('ENE')" label="ENE">
          <n-slider v-model:value="kChart.indicator.ene" :step="1" :max="200" />
        </n-form-item>
        <n-form-item v-show="kChart.indicator.checked.includes('TD9')" label="TD9">
          <n-slider v-model:value="kChart.indicator.td9" range :step="1" :min="1" :max="13" />
        </n-form-item>
      </n-form>
    </n-drawer-content>
  </n-drawer>
  <div></div>
</template>

<style lang="scss" scoped>
// :deep(.n-form-item-blank) {
//   width: 100%;
// }
// .n-slider :deep(.n-slider-rail) {
//   background-color: #18a058;
//   & .n-slider-rail__fill {
//     background-color: #dadadd;
//   }
// }
</style>
