<script setup lang="ts">
import KChart from '@/components/Kchart.vue'
import { test_data, test_markers } from './test'
import { searchIndex } from '@/apis'
import 'uno.css'
import { VNodeChild } from 'vue'
import { SelectOption } from 'naive-ui'
import { StockIndex } from './apis/types/stock'
const kChart = ref()
const search = reactive({
  input: '',
  loading: false,
  result: [] as StockIndex[]
})

async function handleSearch(input: string) {
  if (!input) return
  console.log(input)
  search.loading = true
  const { data } = await searchIndex({ input })
  console.log(data)
  search.loading = false
  search.result = data
  // consNumber indexCode indexName publishDate
}

function renderLabel(option: StockIndex): VNodeChild {
  const { indexName, indexCode } = option
  return [h('div', { class: 'w100% grid-1-2-0' }, [h('span', indexName), h('span', indexCode)])]
}

// function renderOption(a) {
//   console.log(a)
// }
</script>

<template>
  <n-select
    v-model:value="search.input"
    filterable
    placeholder="搜索歌曲"
    label-field="indexName"
    value-field="indexCode"
    :loading="search.loading"
    :options="search.result"
    :render-label="renderLabel"
    clearable
    remote
    @search="handleSearch"
  />
  <!-- <KChart type="Candlestick" :data="test_data" :markers="test_markers" ref="kChart" /> -->
</template>
<style lang="scss">
.n-base-select-option {
  padding: 0 !important;
}
.n-base-select-option__content {
  flex: 1;
}
</style>
