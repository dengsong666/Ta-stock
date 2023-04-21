<script setup lang="ts">
import { getIndexDay, searchIndex } from '@/apis'
import { useKChart } from '@/store'
import { useLoadingBar, useMessage } from 'naive-ui'
import mitt from 'mitt'
const kChart = useKChart()
const search = reactive({
  input_value: '',
  loading: false,
  result: [] as { index: string }[]
})
const emit = defineEmits(['k-data'])
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
  kChart.list = data
  emit('k-data', data)
}

handleUpdate('科创50-000688')
</script>

<template>
  <n-select
    class="w20% mx16px"
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
