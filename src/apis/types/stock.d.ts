export interface StockIndex {
  consNumber: string
  indexCode: string
  indexName: string
  publishDate: string
}
export interface StockIndexDay {
  change: number
  changePct: number
  close: number
  consNumber: number
  high: number
  low: number
  open: number
  peg: number
  time: string
  tradingValue: number
  tradingVol: number
  _internal_originalTime: string
}
