var config = require('./local_config.js')

var host = config.host || 'https://metis-apis.gusibi.mobi';
var basic_token = config.basic_token || 'Basic token=';
var cos_region = config.cos_region || 'shanghai';
var cos_appid = config.cos_appid || 'appid';
var cos_bucket_name = config.cos_bucket_name || 'name';
var cos_dir_name = config.cos_dir_name || '/dir_name';

module.exports = {
    host: host,
    basic_token: basic_token,
    cos_region: cos_region,
    cos_appid: cos_appid,
    cos_bucket_name: cos_bucket_name,
    cos_dir_name: cos_dir_name
}