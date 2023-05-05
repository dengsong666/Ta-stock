import http from './http'
import { StockIndex, StockIndexDay } from './types/stock'

export function searchIndex(params: { input_value: string }) {
  return http.get<StockIndex[]>({
    url: '/ta/search',
    params
  })
}
export function saveIndex(params: { code: string }) {
  return http.get({
    url: '/ta/save-index',
    params
  })
}
export function getIndex(params: { code: string }) {
  return http.get<StockIndexDay[]>({
    url: '/ta/get-index',
    params
  })
}
