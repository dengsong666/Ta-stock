import http from './http'
import { StockIndex } from './types/stock'

export function searchIndex(params: { input: string }) {
  return http.get<StockIndex[]>({
    url: '/stock-index/search',
    params
  })
}
export function getIndexDay(params: { name: string; code: string }) {
  return http.get({
    url: '/stock-index/get-day',
    params
  })
}
