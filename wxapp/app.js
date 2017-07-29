//app.js
var config = require('./config.js')

App({
    onLaunch: function() {
        //调用API从本地缓存中获取数据
        console.log(common.host);
        var that = this;
        that.login();
        var logs = wx.getStorageSync('logs') || []
        logs.unshift(Date.now())
        wx.setStorageSync('logs', logs)
    },
    login: function() {
        var that = this;
        console.log(this);
        wx.login({
            success: function(res) {
                var code = res.code;
                wx.getUserInfo({
                    success: function(res) {
                        // success
                        that.globalData.userInfo = res.userInfo;
                        var encryptedData = res.encryptedData || 'encry';
                        var iv = res.iv || 'iv';
                        wx.request({
                            url: config.host + '/auth/oauth/token?code=' + code,
                            header: {
                                Authorization: config.basic_token
                            },
                            data: {
                                username: encryptedData,
                                password: iv,
                                grant_type: "password",
                                auth_approach: 'wxapp',
                            },
                            method: "POST",
                            success: function(res) {
                                if (res.statusCode === 201) {
                                    wx.showToast({
                                        title: '已登录',
                                        icon: 'success'
                                    });
                                } else if (res.statusCode === 401 || res.statusCode === 403) {
                                    that.register();
                                }

                                console.log(res.statusCode);
                                console.log('request token success');
                            },
                            fail: function(res) {
                                console.log('request token fail');
                            }
                        })
                    },
                    fail: function() {
                        // fail
                    },
                    complete: function() {
                        // complete
                    }
                })
            }
        })

    },
    register: function() {
        var that = this;
        wx.login({
            success: function(res) {
                console.log('wxapp login success!')

                var code = res.code;
                console.log(code);
                wx.getUserInfo({
                    success: function(res) {
                        // success
                        that.globalData.userInfo = res.userInfo;
                        var encryptedData = res.encryptedData || 'encry';
                        var iv = res.iv || 'iv';
                        console.log(iv);
                        wx.request({
                            url: config.host + '/auth/accounts/wxapp',
                            header: {
                                Authorization: config.basic_token
                            },
                            data: {
                                username: encryptedData,
                                password: iv,
                                code: code,
                            },
                            method: "POST",
                            success: function(res) {
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
                            fail: function(res) {
                                console.log('request token fail');
                            }
                        })
                    },
                    fail: function() {
                        // fail
                    },
                    complete: function() {
                        // complete
                    }
                })
            }
        })

    },

    globalData: {
        userInfo: null
    }
})