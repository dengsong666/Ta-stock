<script setup lang="ts">
import { getIndexDay, searchIndex } from '@/apis'
const search = reactive({
  input: '',
  loading: false,
  result: [] as { index: string }[]
})
const emit = defineEmits(['index-day'])
async function handleSearch(input: string) {
  if (!input) return
  search.loading = true
  const { data } = await searchIndex({ input })
  search.loading = false
  search.result = data.map(({ indexName, indexCode }) => ({ index: `${indexName}-${indexCode}` }))
}

async function handleUpdate(value: string) {
  const [name, code] = value.split('-')
  const { data } = await getIndexDay({ name, code })
  emit('index-day', data)
}
</script>

<template>
  <n-select
    v-model:value="search.input"
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
