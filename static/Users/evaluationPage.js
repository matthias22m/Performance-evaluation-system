function showitems(){
    document.getElementById("navbar").style.display="flex";
 }
 function hideItmes(){
     document.getElementById("navbar").style.display="none";
 }
 window.addEventListener('resize', ()=>{
     const windowWidth = window.innerWidth; 
     if(windowWidth>800){
         document.getElementById("navbar").style.display="none";
     }
 
 });