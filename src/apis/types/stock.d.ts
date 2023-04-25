export interface StockIndex {
  code: string
  name: string
  series: string
  classify: string
  size: number
  source: string
}
export interface StockIndexDay {
  time: string
  open: number
  close: number
  high: number
  low: number
  chg: number
  chgp: number
  vol: number
  bollLower: number
  bollUpper: number
  eneUpper: number
  eneLower: number
  td913: number
  slowK: number
  slowD: number
  slowJ: number

  _internal_originalTime: string
}
