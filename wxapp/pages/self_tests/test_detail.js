// test_detail.js
var config = require('../../config.js');
var common = require('../../common.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
      test: {}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
      var that = this,
          jwt = {};
      try {
          var jwt = wx.getStorageSync('jwt')
          console.log(jwt);
          if (jwt) {
              that.setData({
                  jwt: jwt
              })
          }
      } catch (e) {
          common.login(that)
      }
      that.setData({
          title: options.title,
          test_id: options.test_id
      });
      that.get_test_detail(options.test_id);
      wx.setNavigationBarTitle({
          title: '随你选测试'
      });
  },

  get_test_detail: function(test_id){
      var that = this;
      wx.request({ // 发送请求 获取 jwts
          url: config.host + '/v1/self/tests/' + test_id,
          header: {
              Authorization: 'JWT' + ' ' + that.data.jwt.access_token
          },
          method: "GET",
          success: function (res) {
              console.log(res.data)
              if (res.statusCode === 200) {
                  that.setData({
                      test: res.data
                  })
              } else {
                  // 提示错误信息
                  wx.showToast({
                      title: res.data.text,
                      icon: 'success',
                      duration: 2000
                  });
              }
          },
          fail: function (res) {
              console.log('添加测试失败');
          }
      })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})