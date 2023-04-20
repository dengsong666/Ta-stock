import http from './http'
import { StockIndex, StockIndexDay } from './types/stock'

export function searchIndex(params: { input_value: string }) {
  return http.get<StockIndex[]>({
    url: '/stock-index/search',
    params
  })
}
export function getIndexDay(params: { name: string; code: string }) {
  return http.get<StockIndexDay[]>({
    url: '/stock-index/get-day',
    params
  })
}
