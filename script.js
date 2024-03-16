// Get the button element
var createTaskButton = document.getElementById("createTaskButton");

// Get the modal element
var modal = document.getElementById("taskCreateForm");

// Get the close button element inside the modal
var closeButton = modal.querySelector(".close");

// Function to open the modal when the button is clicked
createTaskButton.addEventListener("click", function() {
  modal.style.display = "block";
});

// Function to close the modal when the close button is clicked
closeButton.addEventListener("click", function() {
  modal.style.display = "none";
});