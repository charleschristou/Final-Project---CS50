// Add an event listener for the 'DOMContentLoaded' event
document.addEventListener("DOMContentLoaded", function() 
{
    // Get the row element by its id
    var row = document.getElementById("avg_temp");

    // Get all the cells within the row
    var cells = row.getElementsByTagName("td");

    // Iterate over the cells
    for (var i = 0; i < cells.length; i++) 
    {
        // Get the integer value of the cell
        var value = parseInt(cells[i].textContent);

        // Check if the value is greater than 20
        if (value < 5) {
        // Change the color of the cell
            cells[i].style.backgroundColor = "#abcbff";
        } else if (value < 10) {
            cells[i].style.backgroundColor = "#c8ffab";
        } else if (value < 15) {
            cells[i].style.backgroundColor = "#f9ffc2";
        } else if (value < 20) {
            cells[i].style.backgroundColor = "#fff1c2";
        } else if (value < 25) {
            cells[i].style.backgroundColor = "#ffe1c2";
        } else
            cells[i].style.backgroundColor = "#f5650c";

    }
});