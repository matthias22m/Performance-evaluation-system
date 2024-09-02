function showitems(){
    document.getElementById("navbar").style.display="flex";
 }
 function hideItmes(){
     document.getElementById("navbar").style.display="none";
 }
 const windowWidth = window.innerWidth; 
 console.log("Window width:", windowWidth); 
 window.addEventListener('resize', ()=>{
    const windowWidth = window.innerWidth; 
    console.log("Window width:", windowWidth); 
    if(windowWidth>800){
        document.getElementById("navbar").style.display="none";
    }

});