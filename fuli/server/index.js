
var el = document.getElementById('app');

$.ajax({
    url:"/list",
    data: {
        page:1,
        pageSize:20
    },
    success:function(res){
        console.log(res)
    }
});