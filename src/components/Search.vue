<script setup lang="ts">
import { getIndexDay, searchIndex } from '@/apis'
import { useKChart } from '@/store'
import { useLoadingBar, useMessage } from 'naive-ui'
const search = reactive({
  input_value: '',
  loading: false,
  result: [] as { index: string }[]
})
const emit = defineEmits(['index-day'])
window.$message = useMessage()
window.$loading = useLoadingBar()
async function handleSearch(input_value: string) {
  if (!input_value) return
  search.loading = true
  const { data } = await searchIndex({ input_value })
  search.loading = false
  search.result = data.map(({ indexName, indexCode }) => ({ index: `${indexName}-${indexCode}` }))
}

async function handleUpdate(value: string) {
  const [name, code] = value.split('-')
  const { data } = await getIndexDay({ name, code })
  handleIndexDay(data)
  useKChart().list = data
  emit('index-day', data)
}
function handleIndexDay(index_day: never[]) {
  index.data = index_day
  index_day.forEach((item) => {
    const { time, close, bollLower, bollMiddle, bollUpper, slowK, slowD, slowJ } = item as any
    const bollPB = (close - bollLower) / (bollUpper - bollLower)
    // console.log(close, bollLower, bollUpper, bollPB)
    let marker
    if (bollPB < 0 && slowK <= 20 && slowD <= 20 && slowJ <= 20) {
      marker = {
        time,
        position: 'belowBar',
        color: '#2196F3',
        shape: 'arrowUp',
        text: '买'
      }
    }
    if (bollPB > 1 && slowK >= 80 && slowD >= 80 && slowJ >= 80) {
      marker = {
        time,
        position: 'aboveBar',
        color: '#e91e63',
        shape: 'arrowDown',
        text: '卖'
      }
    }
    marker && index.markers.push(marker)
  })
  console.log(index.markers)
}
handleUpdate('科创50-000688')
</script>

<template>
  <n-select
    class="w20%"
    v-model:value="search.input_value"
    filterable
    placeholder="搜索股票指数"
    label-field="index"
    value-field="index"
    :loading="search.loading"
    :options="search.result"
    :render-label="({ index }) => index"
    clearable
    remote
    @search="handleSearch"
    @update:value="handleUpdate"
  />
</template>
<style scoped lang="scss"></style>
