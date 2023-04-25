import http from './http'

export function addSelected(params: { name: string; code: string; source: string }) {
  return http.get({
    url: '/stock-index/get-day',
    params
  })
}
