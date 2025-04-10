function showConfPopup() {
    document.getElementById("confirmation_popup").style.display = "block";
}

function closePopup() {
    document.getElementById("confirmation_popup").style.display = "none";
}

function confirmDelete() {
    document.getElementById("edit_item_form").submit();
}

// Function to only show submit button after an item has been selected
function showSubmitButton() {
    var selItem = document.getElementById("item_element").value;

    if (selItem !== "") {
        document.querySelector(".submit_button").style.display = "block";
    }
    else {
        document.querySelector(".submit_button").style.display = "none";
    }
}

window.onload = function() {
    showSubmitButton();
}