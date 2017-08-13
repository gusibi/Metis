var config = require('../../config.js')
Page({
    data: {
        showTopTips: false,
        error_msg: null,
        checked_value: null,
        test_id: null,
        step: 0,
        jwt: {},
        questions: [
            '以下 SQL 语句正确的是？',
            '以下哪个语句可以查出最高分？'
        ],
        radioItemsList: [
            [
                { name: 'select * from account;', checked: false},
                { name: 'select 1 from account;', checked: false},
                { name: 'select count(1) from account;', checked: false},
                { name: 'select count(*) from account;', checked: false}
            ],
            [
                { name: 'select * from account;', checked: false},
                { name: 'select score from account limit 1;', checked: false},
                { name: 'select score from account order by score desc;', checked: false},
                { name: 'select max(score) from account;', checked: false}
            ]
        ],
        radioItems: []
    },
    onLoad: function (options) {
        var step = options.step || 0,
            test_id = options.test_id,
            that = this,
            jwt = {};
        if (!test_id){
            that.showTopTips('测试不存在！')
        }else{
            that.setData({
                test_id: test_id
            })
        };
        wx.getStorage({
            key: 'jwt',
            success: function(res) {
                that.setData({
                    jwt: res.data
                })
            },
        })
        this.setData({
            radioItems: this.data.radioItemsList[step]
        });
    },
    showTopTips: function(msg) {
        var that = this;
        this.setData({
            showTopTips: true,
            error_msg: msg
        });
        setTimeout(function() {
            that.setData({
                showTopTips: false
            });
        }, 3000);
    },
    submit: function(){
        var that = this;
        if (!that.checked_value){
            that.showTopTips('请选择答案');
        }else{
            console.log(that.data.test_id)
            console.log(config.host + '/v1/tests/' + that.data.test_id);
            console.log(that.data.jwt.access_token);
            wx.request({ // 发送请求 获取 jwt
                url: config.host + '/v1/tests/' + that.data.test_id,
                header: {
                    Authorization: 'JWT' + that.data.jwt.access_token
                },
                data: {
                    step: that.step,
                    value: that.checked_value
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
                        that.register();
                    } else {
                        // 提示错误信息
                        wx.showToast({
                            title: res.data.error_code,
                            icon: 'success',
                            duration: 2000
                        });
                    }
                },
                fail: function (res) {
                    console.log('request token fail');
                }
            })
        }
    },
    radioChange: function(e) {
        var that = this;
        console.log('radio发生change事件，携带value值为：', e.detail.value);

        var radioItems = this.data.radioItems;
        console.log(radioItems);
        for (var i = 0, len = radioItems.length; i < len; ++i) {
            radioItems[i].checked = i == e.detail.value;
            console.log(radioItems[i], e.detail.value);
        }
        console.log(radioItems);
        that.checked_value = e.detail.value;
        this.setData({
            radioItems: radioItems
        });
    },
});