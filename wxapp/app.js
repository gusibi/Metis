//app.js
var config = require('./config.js');
var common = require('./common.js');

App({
    onLaunch: function() {
        //调用API从本地缓存中获取数据
        var jwt = wx.getStorageSync('jwt');
        var that = this;
        if (!jwt.access_token){ //检查 jwt 是否存在 如果不存在调用登录
            common.login(that);
        } else {
            console.log(jwt.account_id);
        }
    },
    get_user_info: function(jwt) {
        wx.request({
            url: config.host + '/auth/accounts/self',
            header: {
                Authorization: jwt.token_type + ' ' + jwt.access_token
            },
            method: "GET",
            success: function (res) {
                if (res.statusCode === 201) {
                    wx.showToast({
                        title: '已注册',
                        icon: 'success'
                    });
                } else if (res.statusCode === 401 || res.statusCode === 403) {
                    wx.showToast({
                        title: '未注册',
                        icon: 'error'
                    });
                }

                console.log(res.statusCode);
                console.log('request token success');
            },
            fail: function (res) {
                console.log('request token fail');
            }
        })
    },

    globalData: {
        userInfo: null
    }
})