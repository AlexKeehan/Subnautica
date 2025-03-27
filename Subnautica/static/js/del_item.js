function showConfPopup() {
    document.getElementById("confirmation_popup").style.display = "block";
}

function closePopup() {
    document.getElementById("confirmation_popup").style.display = "none";
}

function confirmDelete() {
    document.getElementById("edit_item_form").submit();
}