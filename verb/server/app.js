//server

let express = require('express');
let router = require('./routers/index');
let morgan = require('morgan');
let fs = require('fs');
let path = require('path');
let bodyParser = require('body-parser');
let app = express();

//router
app.use('/',router);

//static
app.use('/static', express.static('../static'));

//log
let  accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), {flags: 'a'});
app.use(morgan('combined',{
	stream:accessLogStream
}));
//diable x-powered-by header
app.disable('x-powered-by');

//json format
app.use(bodyParser.json({limit: '1mb'}));  //body-parser 解析json格式数据
app.use(bodyParser.urlencoded({            //此项必须在 bodyParser.json 下面,为参数编码
  extended: true
}));

//interface
app.post('/inputword',(req,res,next)=>{
	 console.log(req.body);
	 //echo server
	 res.send(req.body);
	 next();
})

//start server
let server = app.listen(3030,()=>{
	console.log('server start');
});

