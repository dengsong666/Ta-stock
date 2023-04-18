import http from './http'
import { StockIndex } from './types/stock'

export function searchIndex(params: { input: string }) {
  return http.get<StockIndex[]>({
    url: '/stock-index/search',
    params
  })
}
