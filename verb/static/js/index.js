let el = document.getElementById('input-word');
el.addEventListener('input',deteChange);

function deteChange(event){
	let value = event.target.value;
	console.log(event.target.value)
}
