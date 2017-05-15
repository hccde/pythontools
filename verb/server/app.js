//server

let express = require('express');
let router = require('./routers/index');
let morgan = require('morgan');
let fs = require('fs');
let path = require('path');
let app = express();

//router
app.use('/',router);

//static
app.use('/static', express.static(__dirname + '/static'));

//log
let  accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), {flags: 'a'});
app.use(morgan('combined',{
	stream:accessLogStream
}));


//start server
let server = app.listen(3030,()=>{
	console.log('server start');
})