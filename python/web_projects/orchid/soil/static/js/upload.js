$(document).ready(function(){
    $('#submit').on('click', function(){
        var conf = {'scheme': 'file'};
        var store = Store(conf);
        store.add()
    });
});


