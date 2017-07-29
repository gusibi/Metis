var config = require('./config.js')

var host = config.host || 'https://metis.gusibi.mobi';
var basic_token = config.basic_token || 'Basic token=';

module.exports = {
    host: host,
    basic_token: basic_token
}