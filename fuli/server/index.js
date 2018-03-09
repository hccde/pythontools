
var list = [];
var index = 0;
var page = 1;
function getList(page){
$.ajax({
    url:"/list",
    data: {
        page:page,
        pageSize:20
    },
    success:function(res){
        list = res.list;
        index = 1;
    }
});
}
getList(1);
$('#button').click(function(){
    $('#video').attr('src',list[index])
    window.index=window.index+1;
    if(window.index >= 20){
        page+=1;
        getList(page);
    }
});
$('#submit').click(function(){
    var  p = $("#input").val();
    getList(p);
})