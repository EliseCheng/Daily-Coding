/*
 * 存储基础类工厂方法.
 * @conf 后端访问各种不同存储服务器的配置信息
 */
var Store = function (conf) {
    var store;
    switch (conf.scheme) {
        case 'swift':
              store = new SwiftStore();
              break;
        case 'http':
             store = new HttpStore();
             break;
        case 'file':
        default:
             store = new FileStore();
     }
     store.conf = conf
     return store;
};

 


var SwiftStore = function(){
    
    this.add = function(){
        alert(this.conf.scheme)
    }
};


var HttpStore = function(){
    this.add = function(){
        alert(this.conf.scheme)
    }
};

var FileStore = function(){
    this.add = function(){
        alert(this.conf.scheme)
    }
};



