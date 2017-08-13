// self.js
var config = require('../../config.js');
var common = require('../../common.js');

Page({

  /**
   * 页面的初始数据
   */
  data: {
      jwt: {},
      account: {}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
      var test_id = options.test_id,
          that = this,
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
      wx.request({ // 请求注册用户接口
          url: config.host + '/auth/accounts/self',
          header: {
              Authorization: 'JWT' + ' ' + that.data.jwt.access_token
          },
          method: "GET",
          success: function (res) {
              if (res.statusCode === 200) {
                  wx.showToast({
                      title: '取到用户信息',
                      icon: 'success'
                  });
                  console.log(res.data);
                  that.setData({
                      account: res.data
                  });
              } else if (res.statusCode === 404) {
                  wx.showToast({
                      title: '用户不存在',
                      icon: 'success'
                  });
              }
          },
          fail: function (res) {
              console.log('request token fail');
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