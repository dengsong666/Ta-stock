import { StockIndexDay } from '@/apis/types/stock'

export const useKChart = defineStore('k-chart', {
  state: () => ({
    list: [] as StockIndexDay[],
    crosshair: {} as StockIndexDay,
    option: {
      chart: {} as ChartOption.Base,
      series: {} as ChartOption.Series
    }
  }),
  actions: {
    Func() {}
  }
})
