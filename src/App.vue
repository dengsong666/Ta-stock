<script setup lang="ts">
import 'uno.css'
const data = ref([])
</script>

<template>
  <Suspense>
    <div class="h100%">
      <Search @index-day="data = $event" />
      <KChart type="Candlestick" :data="data" :markers="[]">
        <KLegends />
      </KChart>
    </div>
  </Suspense>
</template>
<style lang="scss"></style>
