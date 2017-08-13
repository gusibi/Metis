var config = require('./config.js');
var login = function(that) {
    // 登录部分代码
    wx.login({
        // 调用 login 获取 code
        success: function (res) {
            var code = res.code;
            wx.getUserInfo({
                // 调用 getUserInfo 获取 encryptedData 和 iv
                success: function (res) {
                    // success
                    that.globalData.userInfo = res.userInfo;
                    var encryptedData = res.encryptedData || 'encry';
                    var iv = res.iv || 'iv';
                    console.log(config.basic_token);
                    wx.request({ // 发送请求 获取 jwt
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
                        success: function (res) {
                            if (res.statusCode === 201) {
                                // 得到 jwt 后存储到 storage，
                                wx.showToast({
                                    title: '登录成功',
                                    icon: 'success'
                                });
                                wx.setStorage({
                                    key: "jwt",
                                    data: res.data
                                });
                                that.globalData.access_token = res.data.access_token;
                                that.globalData.account_id = res.data.sub;
                            } else if (res.statusCode === 401) {
                                // 如果没有注册调用注册接口
                                register(that);
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
                            console.log('request token fail');
                        }
                    })
                },
                fail: function () {
                    // fail
                },
                complete: function () {
                    // complete
                }
            })
        }
    })

}

var register = function(that) {
    // 注册代码
    wx.login({ // 调用登录接口获取 code
        success: function (res) {
            var code = res.code;
            consolse.log('>>>>>>>>>>>>>>');
            wx.getUserInfo({
                // 调用 getUserInfo 获取 encryptedData 和 iv
                success: function (res) {
                    // success
                    that.globalData.userInfo = res.userInfo;
                    var encryptedData = res.encryptedData || 'encry';
                    var iv = res.iv || 'iv';
                    console.log(iv);
                    wx.request({ // 请求注册用户接口
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
                        success: function (res) {
                            if (res.statusCode === 201) {
                                wx.showToast({
                                    title: '注册成功',
                                    icon: 'success'
                                });
                                login(that);
                            } else if (res.statusCode === 400) {
                                wx.showToast({
                                    title: '用户已注册',
                                    icon: 'success'
                                });
                                that.login();
                            } else if (res.statusCode === 403) {
                                wx.showToast({
                                    title: res.data.text,
                                    icon: 'success'
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
                fail: function () {
                    // fail
                },
                complete: function () {
                    // complete
                }
            })
        }
    })
}

module.exports = {
    login: login,
    register: register
}