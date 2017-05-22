let el = document.getElementById('input-word');
el.addEventListener('input',deteChange);

function deteChange(event){
	let value = event.target.value;
	let json = {
		word:value
	};
	ajax(JSON.stringify(json));
}

function ajax(jsonstr){
	let xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange= getRes;
  	xmlhttp.open("post",'/inputword',true);
  	//set request header to send data by json
	xmlhttp.setRequestHeader("Content-Type","application/json");
	
	xmlhttp.send(jsonstr);

	function getRes(){
		if (xmlhttp.readyState==4){
  			if (xmlhttp.status==200){
  				console.log(xmlhttp.responseText)
    		}
  			else{
    			alert("Problem retrieving XML data");
    		}
  		}
	}
}