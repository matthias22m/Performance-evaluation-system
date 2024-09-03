function showitems(){
    document.getElementById("navbar").style.display="flex";
 }
 function hideItmes(){
     document.getElementById("navbar").style.display="none";
 }
 const windowWidth = window.innerWidth; 
 window.addEventListener('resize', ()=>{
    const windowWidth = window.innerWidth; 
    if(windowWidth>800){
        document.getElementById("navbar").style.display="none";
    }

});