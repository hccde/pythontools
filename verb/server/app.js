//server

let express = require('express');
let router = require('./routers/index');
let app = express();

//router
app.use('/',router);

//start server
let server = app.listen(3030,()=>{
	console.log('server start');
})