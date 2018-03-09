let express = require('express');
let fs = require('fs');
let str = fs.readFileSync('./index.html').toString();
let list = fs.readdirSync('/Users/admos/Documents/notchild/VideoData');
app = express();

app.use(express.static('public'));
app.use(express.static('../server'));
app.use(express.static('/Users/admos/Documents/notchild/VideoData/'));

app.get('/list',function(req, res){
    console.log(req.query);
    let { page,pageSize} = req.query;
    res.send({
        code:200,
        list:list
    })
})

app.listen(3000);