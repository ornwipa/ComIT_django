// $(document).ready(function(){ // use jquery
document.addEventListener('DOMContentLoaded', (event) => {
    let main = document.getElementById('main-content');
    let button = document.getElementById("button");
    button.onclick = function(event) { main.append("button clicked "); }
}); // event handler, to run this function when document is alerady load