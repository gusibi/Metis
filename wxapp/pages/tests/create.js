// tests/create.js
Page({

  /**
   * 页面的初始数据
   */
    data: {
        showTopTips: false,
        start_date: "2016-09-01",
        start_time: "12:01",
        end_date: "2016-09-01",
        end_time: "12:31"
    },
    showTopTips: function () {
        var that = this;
        this.setData({
            showTopTips: true
        });
        setTimeout(function () {
            that.setData({
                showTopTips: false
            });
        }, 3000);
    },
    bindDateChange: function (e) {
        this.setData({
            date: e.detail.value
        })
    },
    bindTimeChange: function (e) {
        this.setData({
            time: e.detail.value
        })
    },
    formSubmit: function (e) {
        console.log('form发生了submit事件，携带数据为：', e.detail.value)
        var form_data = e.detail.value;
        var params = {
            'title': form_data.title,
            'description': form_data.description,
            'remark': form_data.remark,
            'start_time': form_data.start_date + ' ' + form_data.start_time,
            'end_time': form_data.end_date + ' ' + form_data.end_time
        };
        console.log('form发生了submit事件，表单数据为：', params)
    },
    formReset: function () {
        console.log('form发生了reset事件')
    },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  
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