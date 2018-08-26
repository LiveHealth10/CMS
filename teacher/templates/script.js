$(document).ready(function(){

	$.getJSON("http://127.0.0.1:8000/teacher/?format=json",function(obj){
		var check='';
	
	$.each(obj,function(key,value){
		check =+ "<li>"+value.date+"<li>"
	$('#check').append(check);
});

});
});