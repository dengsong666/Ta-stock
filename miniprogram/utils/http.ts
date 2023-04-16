
interface ResponseData<T> extends WechatMiniprogram.RequestSuccessCallbackResult {
  data: T
}

function _r(method: | "GET" | "POST" | "PUT" | "DELETE") {
  return function <T = any>(config: WechatMiniprogram.RequestOption): Promise<ResponseData<T>> {
    wx.showLoading({ title: '加载中...', mask: true })
    config.url = "http://127.0.0.1:8000" + config.url
    // 请求拦截
    return new Promise((resolve, reject) =>
      wx.request({
        ...config, method,
        success: (res: ResponseData<T>) => resolve(res),
        fail: err => reject(err),
        complete: () => wx.hideLoading()
      }))
  }
}
export const Http = { get: _r('GET'), post: _r('POST'), put: _r('PUT'), delete: _r('DELETE') }
