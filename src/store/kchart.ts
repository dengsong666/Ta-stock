import { StockIndexDay } from '@/apis/types/stock'
export const useKChart = defineStore('k-chart', {
  state: () => ({
    list: [] as StockIndexDay[],
    crosshair: {} as StockIndexDay,
    markers: [],
    indicator: {
      checked: ['KDJ', 'BOLL', 'TD9'],
      kdj: 20,
      boll: 0,
      ene: 0,
      td9: [8, 13]
    },
    option: {
      chart: {} as ChartOption.Base,
      series: {} as ChartOption.Series
    }
  }),
  actions: {
    calculate(indicator: typeof this.indicator, data: StockIndexDay[]) {
      const { boll, kdj, ene, checked } = indicator
      let markers: any[] = []
      /**
       * 0 卖
       * 1 买
       * 2 不买不卖
       */
      data.forEach((item) => {
        const { time, close, bollLower, bollUpper, slowK, slowD, slowJ, _internal_originalTime, td9, eneLower, eneUpper } = item
        const bollPB = (close - bollLower) / (bollUpper - bollLower)
        const isBuy = { BOLL: 2, KDJ: 2, TD9: 2, ENE: 2 }
        // 计算买点
        if (checked.includes('BOLL')) {
          if (close - bollLower <= boll && bollLower) isBuy.BOLL = 1
          if (bollUpper - close <= boll && bollUpper) isBuy.BOLL = 0
        }
        if (checked.includes('ENE')) {
          if (close - eneLower <= ene && eneLower) isBuy.ENE = 1
          if (eneUpper - close <= ene && eneUpper) isBuy.ENE = 0
        }
        if (checked.includes('KDJ')) {
          if (slowK <= kdj && slowD <= kdj && slowJ <= kdj) isBuy.KDJ = 1
          if (slowK > 100 - kdj && slowD > 100 - kdj && slowJ > 100 - kdj) isBuy.KDJ = 0
        }
        if (checked.includes('TD9')) isBuy.TD9 = indicator.td9.includes(td9 < 0 ? -td9 : td9) ? 1 : 0

        type C = keyof typeof isBuy
        if (checked.length && checked.every((item) => isBuy[item as C] == 1)) {
          markers.push({
            time: _internal_originalTime,
            position: 'belowBar',
            color: '#2196F3',
            shape: 'arrowUp',
            text: '买'
          })
        }
        if (checked.length && checked.every((item) => isBuy[item as C] == 0)) {
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
