// pages/home/home.ts

import { searchIndex } from '../../apis/index'
import { test_data } from './list'
import drawKLinesUtil from '../../utils/drawKLinesUtil'
Page({
  /**
   * 页面的初始数据
   */
  data: {
    // searchList: [],
    hideSearchList: true,
    chartData: {},
    cHeight: 200
  },
  onChange(e: WechatMiniprogram.CustomEvent<String>) {
    if (!e.detail) {
      this.setData({
        hideSearchList: true
      })
    }
    console.log(e.detail)
  },
  async onSearch(e: WechatMiniprogram.CustomEvent<String>) {
    const { data } = await searchIndex({ search_input: e.detail })
    this.setData({
      searchList: data.map(({ indexCode, indexName }) => ({ indexName, indexCode })),
      hideSearchList: false,
      searchInput: e.detail ?? ''
    })
  },
  onCancel() {
    this.setData({ hideSearchList: true })
  },
  onSelect(e: WechatMiniprogram.BaseEvent) {
    // const { indexCode, indexName } = e.target.dataset.search
    this.setData({
      hideSearchList: true,
      searchInput: ''
    })
  },
    // 监听 scrollView 的滚动，监听当前滚动到的 K线为哪一根
  onScroll (e) {
    console.log(e);
    
    this.curMsg = drawKLinesUtil.onScroll(e.detail.scrollLeft)
    // 用于 scroll view 的 touch 事件，不需要绘制K线点击态可不写
    this.isScroll = true;
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad() {},

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {
    wx.createSelectorQuery()
      .selectAll('#mainctx, #optctx, #yctx')
      .fields({ node: true, size: true })
      .exec((res) => {
        // 0,1,2 mainctx optctx yctx
        console.log(res[0][0].node)
        // const canvas = res[0].node
        const mainctx = res[0][0].node.getContext('2d')
        const optctx = res[0][1].node.getContext('2d')
        const yctx = res[0][2].node.getContext('2d')
        console.log(yctx)
        
        // const dpr = wx.getSystemInfoSync().pixelRatio
        const w = res[0].width
        const h = res[0].height
        const maxV = Math.max(...test_data.map((item) => item.high))
        const minV = Math.min(...test_data.map((item) => item.low))
        let config = {
          wWidth: w, // 屏幕宽度
          wHeight: h, // 屏幕高度
          datas: test_data, // K线数据集
          signsList: [], // 信号数据集，不传则不绘制买卖信号
          yctx: yctx, // y 轴画布实例
          mainctx: mainctx, // K线画布与X轴画布实例
          optctx: optctx, // K线选中态 画布实例
          minNum: minV, // y轴最小值
          maxNum: maxV // y轴最大值
        }
        // 参数初始化
        // 返回K线画布宽度，需要将返回的  maincWidth 设置上 K线画布的 宽度 样式
        let maincWidth = drawKLinesUtil.init(config)
        // 绘制Y轴
        drawKLinesUtil.onDrawYAxis()
        // 绘制X轴
        drawKLinesUtil.onDrawXAxis()
        // 绘制K线图
        // scrollview 中嵌套canvas，scroll-left 必须在draw回调里面去实现，否则不起作用
        // 如果不需要用到 scroll-left 则直接调用K线绘制即可，不需要重现回调： drawKLinesUtil.onDrawKLines（）
        drawKLinesUtil.onDrawKLines( )
      })
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {},

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {},

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {},

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {},

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {},

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {}
})
