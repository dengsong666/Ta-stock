import { Index } from 'typings/apis'
import { Http } from '../utils/index'

export function searchIndex(data: { search_input: String }) {
  return Http.get<Index[]>({
    url: '/stock-index/search',
    data
  })
}