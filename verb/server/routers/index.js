let express = require('express');
let router = express.Router();

router.use((req,res,next)=>{
	//log
	console.log('time',Date.now())
	next()
});

router.get('/index',(req,res,next)=>{
	res.send('test');
	next();
})

module.exports = router;