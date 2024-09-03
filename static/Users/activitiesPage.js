const searchEngine = document.querySelector('#search');
const activityRows = document.querySelectorAll('#activityList tr');
searchEngine.addEventListener('keyup', (event) => {
    const query = event.target.value.toLowerCase();

    activityRows.forEach(row => {
        const taskName = row.cells[0].textContent.toLowerCase();
        row.style.display = taskName.includes(query) ? '' : 'none';
    });
});
function showitems(){
    document.getElementById("navbar").style.display="flex";
 }
 function hideItmes(){
     document.getElementById("navbar").style.display="none";
 }
function progress(){
    document.getElementById("progress-button").style.backgroundColor="green";
    document.getElementById("progress-button").textContent="Done";
}
window.addEventListener('resize', ()=>{
    const windowWidth = window.innerWidth; 
    if(windowWidth>800){
        document.getElementById("navbar").style.display="none";
    }
});