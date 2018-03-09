const request = require('request');
const fs = require('fs');
module.exports = {
	getImage(src){
		request(src).pipe(fs.createWriteStream('.',{
			fd:fs.openSync('./test.gif','w+')
		}).on('error',function(err){
			console.log(err);
		})
		).on('error',function(err){
			console.log(err)
		});
	}
}