<script setup lang="ts">
import { getIndexDay, searchIndex } from '@/apis'
import { useKChart } from '@/store'
import { SelectOption, useLoadingBar, useMessage } from 'naive-ui'
const kChart = useKChart()
const search = reactive({
  input_value: '',
  loading: false,
  result: [] as SelectOption[]
})
const emit = defineEmits(['k-data'])
window.$message = useMessage()
window.$loading = useLoadingBar()
const renderLabel = ({ label }: any) => {
  return [
    h(
      'div',
      { class: 'grid-1-4-20' },
      label?.split('-').map((item: string) => h('span', { class: 'elp', title: item }, item))
    )
  ]
}
async function handleSearch(input_value: string) {
  if (!input_value) return
  search.loading = true
  const { data } = await searchIndex({ input_value })
  search.loading = false
  search.result = data.map(({ name, code, source, series, classify }) => ({ value: `${name}-${code}-${source}`, label: `${name}-${code}-${series}-${classify}` }))
}

async function handleUpdate(value: string) {
  const [name, code, source] = value.split('-')
  const { data } = await getIndexDay({ name, code, source })
  kChart.list = data
  emit('k-data', data)
}

handleUpdate('创业板指-399006-G')
</script>

<template>
  <n-select
    class="w400px mx16px"
    v-model:value="search.input_value"
    filterable
    placeholder="搜索股票指数"
    :loading="search.loading"
    :options="search.result"
    :render-label="renderLabel"
    clearable
    remote
    @search="handleSearch"
    @update:value="handleUpdate"
  />
</template>
<style scoped lang="scss"></style>
