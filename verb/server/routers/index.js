let express = require('express');
let router = express.Router();

// let views = {
// 	'index':
// };

router.get('/',(req,res,next)=>{
	res.send('test');
	next();
})

module.exports = router;