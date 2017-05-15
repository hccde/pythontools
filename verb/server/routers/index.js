let express = require('express');
let router = express.Router();
let fs = require('fs');
let str = fs.readFileSync('../view/index.html','utf-8');
// let views = {
// 	'index':
// };

router.get('/',(req,res,next)=>{
	res.send(str);
	next();
})

module.exports = router;