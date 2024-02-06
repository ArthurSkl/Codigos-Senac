const q1 = document.getElementById("q1");
function expandir(){
    q1.style.transform = "scale(250)";
    setTimeout(()=> {
        window.location.href = "transition.html"    
    }
      ,900)
}