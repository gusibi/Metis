// list.js
var sliderWidth = 96; // 需要设置slider的宽度，用于计算中间位置
var config = require('../../config.js');
Page({

   /**
   * 页面的初始数据
   */
    data: {
        jwt: {},
        tabs: ["已发布", "草稿"],
        activeIndex: 0,
        sliderOffset: 0,
        sliderLeft: 0,
        published_tests: [],
        draft_tests: []
    },
    tabClick: function (e) {
        this.setData({
            sliderOffset: e.currentTarget.offsetLeft,
            activeIndex: e.currentTarget.id
        });
        if (e.currentTarget.id == 0){
            this.get_tests('published');
        } else if (e.currentTarget.id == 1){
            this.get_tests('draft');
        }
    },

   /**
   * 生命周期函数--监听页面加载
   */
    onLoad: function () {
        var that = this;
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
        };
        wx.getSystemInfo({
            success: function (res) {
                that.setData({
                    sliderLeft: (res.windowWidth / that.data.tabs.length - sliderWidth) / 2,
                    sliderOffset: res.windowWidth / that.data.tabs.length * that.data.activeIndex
                });
            }
        });
        that.get_tests('published');
    },

  get_tests: function(status) {
      var that = this;
      wx.request({ // 已发布的测试
          url: config.host + '/v1/self/tests?status=' + status,
          header: {
              Authorization: 'JWT' + ' ' + that.data.jwt.access_token
          },
          method: "GET",
          success: function (res) {
              if (res.statusCode === 200) {
                  if (status === 'published'){
                      that.setData({
                          published_tests: res.data
                      });
                  }else if(status == 'draft'){
                      that.setData({
                          draft_tests: res.data
                      });
                  }
              } else if (res.statusCode !== 200) {
                  wx.showToast({
                      title: res.data.message,
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