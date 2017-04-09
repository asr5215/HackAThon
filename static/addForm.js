function check(){
	/*if (!checkTitle){
	}
	else if(!checkLocation){	
	}
	else if(!checkStart){		
	}
	else if(!checkEnd){		
	}
	else if(!checkDesc){		
	}
	else{*/
		show("Submit complete");
		document.getElementById("submit").type="submit";
	//}
}/*
function checkTitle(){
	var title = document.getElementById("title").value;
	if (title == ""){
        show("Event Title field must be filled out.");
	}
	return title != "";
}
function checkLocation{
	var loc = document.getElementById("location").value;
	if (loc == ""){
        show("Location field must be filled out.");
	}
	return loc != "";
}
function checkStart(){
	var date = document.getElementById("start").value;
	if(!date.match([0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]T[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]){
		show("Start date must have correct format.");
	}
	return date != "";
}
function checkEnd(){
	var date = document.getElementById("end").value;
	if(!date.match([0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]T[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]){
		show("End date must have correct format.");
	}
	return date != "";
}
function checkDesc{
	var desc = document.getElementById("description").value;
	if (desc == ""){
        show("Description field must be filled out.");
	}
	return desc != "";
}

//snackbar function
function show(a){
    var x = document.getElementById("snackbar");
    x.innerHTML = a;
    x.className = "show";
    setTimeout(function(){
        x.className = x.className.replace("show", ""); }, 3000);
}*/