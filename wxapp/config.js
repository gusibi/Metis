var config = require('./local_config.js')
console.log(config.host);
console.log(config.basic_token);

var host = config.host || 'https://metis-apis.gusibi.mobi';
var basic_token = config.basic_token || 'Basic token=';

module.exports = {
    host: host,
    basic_token: basic_token
}