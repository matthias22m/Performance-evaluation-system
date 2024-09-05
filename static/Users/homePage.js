const button = document.getElementById('showResultButton');
const resultDiv = document.getElementById('result');
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
button.addEventListener('click', function() {
    if (resultDiv.style.display === 'block') {
        button.textContent="See Result"
        resultDiv.style.opacity = '0';
        setTimeout(() => {
            resultDiv.style.display = 'none';
        }, 500);
    } else {
        resultDiv.style.display = 'block';
        button.textContent="Hide Result"
        setTimeout(() => {
            resultDiv.style.opacity = '1';
        }, 10);
    }
});