<script setup lang="ts">
import { useKChart } from '@/store'
const indicator = ['MACD', 'KDJ', 'RSI', 'BOLL', '九转序列']
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
          <div class="grid-1-3-16 w100%">
            <span class="text-center">k<n-slider v-model:value="kChart.indicator.kdj.k" range :step="1" /> </span>
            <span class="text-center">d<n-slider v-model:value="kChart.indicator.kdj.d" range :step="1" /> </span>
            <span class="text-center">j<n-slider v-model:value="kChart.indicator.kdj.j" range :step="1" /></span>
          </div>
        </n-form-item>
        <n-form-item v-show="kChart.indicator.checked.includes('BOLL')" label="BOLL" path="user.phone">
          <n-slider v-model:value="kChart.indicator.boll" range :min="-0.5" :max="1.5" :step="0.1" />
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
.n-slider :deep(.n-slider-rail) {
  background-color: #18a058;
  & .n-slider-rail__fill {
    background-color: #dadadd;
  }
}
</style>
