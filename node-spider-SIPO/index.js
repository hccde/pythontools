let request = require('request'),
	cheerio = require('cheerio'),
	fs = require('fs');
let configure = './req_info.json'

let req_info = require('./req_info.json');
let key_info = require('./key.json');

let formData = {
		"resultPagination.limit": 12,
		"resultPagination.sumLimit": 10,
		"resultPagination.start": 12,
		"resultPagination.totalCount": 387941,
		"searchCondition.searchType": "Sino_foreign",
		"search_scope": "",
		"searchCondition.dbId": "",
		"searchCondition.searchExp": "江苏",
		"wee.bizlog.modulelevel": "0200101",
		"searchCondition.executableSearchExp": "VDB:(IBI='江苏')",
		"searchCondition.literatureSF": "",
		"searchCondition.strategy": "",
		"searchCondition.searchKeywords":"",
		"searchCondition.searchKeywords": "[江][ ]{0,}[苏][ ]{0,}",
	}
console.log(formData)
let proxy = undefined
function req() {
	request.post({
			url: "http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/showSearchResult-startWa.shtml",
			form: formData,
			gzip: true,
			headers:req_info.headers,
			// proxy:proxy&&('http://'+proxy)
			proxy:'http://183.4.175.239:9797'
		},
		function optionalCallback(err, httpResponse, body) {
			if (err) {
				get_proxy()
				return console.error('upload failed:', err);
			}
			console.log(body)
			// console.log(httpResponse)
			console.log(body.length)
			if(body.length == 2957 || body.length == 161 || body.length == 337||body.length<6000){
				return get_proxy()
			}else{
				get_info(body)
				req_info.params['resultPagination.start'] += req_info.params['resultPagination.limit'];
				if(req_info.params['resultPagination.start'] < req_info.params['resultPagination.totalCount'])
					return req();
				else
					console.log('this city ok')
			}
		});
}

function get_proxy(){
	// request = request.defaults({'proxy':'http://'+'localhost'})

	request.get(key_info['url'],function(err,res,body){
		if(err){
			console.log(err)
			proxy = undefined
			return get_proxy()
		}
		if(body){
			proxy = body.trim()
			console.log(proxy)
			return req()
		}else{
			proxy = undefined
			return get_proxy();
		}
	})
}

function get_info(html) {
	let $ = cheerio.load(html)
	str = '';
	$('.item-content-body').each(function() {
		let item = $(this).text().replace(/\s+/g, ' ')
		str = str + item + '\r\n'
	})
	fs.appendFile(req_info.result, str)
	fs.writeFile(configure,JSON.stringify(req_info))
	console.log(str)
}

req()