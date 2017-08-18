$('#submit').on('click', function(){
    var conf = {'scheme': 'swift'};
    var store = Store.getBackendStore(conf);
    store.add()
});
