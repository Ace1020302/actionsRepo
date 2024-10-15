function alertMe(message)
{
    alert(message);
}

function toggleVisibility(id){
    elem = document.getElementById(id)
    elem.style.display = elem.style.display == "none" ? "block" : "none";
}