let express = require('express');
let fs = require('fs');
let str = fs.readFileSync('./index.html').toString();
let list = fs.readdirSync('../dist');
console.log(list)
app = express();

app.use(express.static('public'));
app.use(express.static('../server'));

app.get('/', function(req, res){
    res.send(str);
});
app.get('/list',function(req, res){
    console.log(req.query);
    let { page,pageSize} = req.query;
    res.send({
        code:200,
        list:[]
    })
})

app.listen(3000);