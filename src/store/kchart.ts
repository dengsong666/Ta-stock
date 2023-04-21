import { StockIndexDay } from '@/apis/types/stock'
export const useKChart = defineStore('k-chart', {
  state: () => ({
    list: [] as StockIndexDay[],
    crosshair: {} as StockIndexDay,
    markers: [],
    indicator: {
      checked: ['KDJ', 'BOLL'],
      kdj: {
        k: [20, 80],
        d: [20, 80],
        j: [20, 80]
      },
      boll: [0, 1]
    },
    option: {
      chart: {} as ChartOption.Base,
      series: {} as ChartOption.Series
    }
  }),
  actions: {
    calculate(indicator: typeof this.indicator, data: StockIndexDay[]) {
      const { boll, kdj, checked } = indicator
      let markers: any[] = []
      /**
       * 0 卖
       * 1 买
       * 2 不买不卖
       */
      data.forEach((item) => {
        const { time, close, bollLower, bollUpper, slowK, slowD, slowJ, _internal_originalTime } = item
        const bollPB = (close - bollLower) / (bollUpper - bollLower)
        const isBuy: { [key: string]: number } = { BOLL: 2, KDJ: 2 }
        // 计算买点
        if (checked.includes('BOLL')) {
          if (bollPB <= boll[0]) isBuy.BOLL = 1
          if (bollPB > boll[1]) isBuy.BOLL = 0
        }
        if (checked.includes('KDJ')) {
          if (slowK <= kdj.k[0] && slowD <= kdj.d[0] && slowJ <= kdj.j[0]) isBuy.KDJ = 1
          if (slowK > kdj.k[1] && slowD > kdj.d[1] && slowJ > kdj.j[1]) isBuy.KDJ = 0
        }
        if (checked.every((item) => isBuy[item] == 1)) {
          markers.push({
            time: _internal_originalTime,
            position: 'belowBar',
            color: '#2196F3',
            shape: 'arrowUp',
            text: '买'
          })
        }
        if (checked.every((item) => isBuy[item] == 0)) {
          markers.push({
            time,
            position: 'aboveBar',
            color: '#e91e63',
            shape: 'arrowDown',
            text: '卖'
          })
        }
      })
      return markers
    }
  }
})
