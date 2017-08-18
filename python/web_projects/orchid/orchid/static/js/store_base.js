/*
 * 存储基础类方法.
 * @conf 后端访问各种不同存储服务器的配置信息
 */
var Store = function (conf) {
    this.add(conf);
};


Store.prototype = {
    getBackendStore: function (conf) {
        var store;

        switch (conf.scheme) {
            case 'swift':
                  store = new SwiftStore(conf);
                  break;
            case 'http':
                 store = new HttpStore(conf);
                 break;
            case 'file':
            default:
                 store = new FileStore(conf);
         }
         
         return store;
    }
    
};



var SwiftStore = function(conf){
    this.add = function(conf){
        alert(conf)
    }
};

var HttpStore = function(){
    alert('http')
};

var FileStore = function(){
    alert('file')
};



