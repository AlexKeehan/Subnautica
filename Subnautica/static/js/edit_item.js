// For add_item.html image display functionality
function imageDisplay() {
    $(document).ready(function() {
        // Check for image being selected
        $(`#item_image`).on("change", function(event) {
            // Get file
            const file = event.target.files[0];

            // List of allowed file types
            const acc_file_types = [
                "image/jpeg",
                "image/png",
                "image/webp",
            ]

            // Check if file is an allowed type
            if (acc_file_types.includes(file.type)) {

                // Check if file exists
                if (file) {
                    // Init file reader and get the image data and set as the src for the image_section
                    const reader = new FileReader();

                    reader.onload = function (data) {
                        $(".image_section img").attr("src", data.target.result);
                    }
                    reader.readAsDataURL(file);
                }
            }
            else {
                // Output error upon invalid file type
                alert("Please Select a Valid Image Type (JPEG, WEBP, PNG");
                // Reset the image section to default placeholder image
                $(`#item_image`).val('');
                $(`.image_section img`).attr("src", "../placeholder_img.png");
            }
        });
    });
}

// Separate logic for checkmark
// Not finished yet
function checkmarkLogic(selElement) {
    const selectedOptions = Array.from(selElement.selectedOptions);
    selectedOptions.forEach(option => {
        option.style.backgroundColor = '#D3F9D8';
    });

    const allOptions = Array.from(selElement.options);
    allOptions.forEach(option => {
        if (!option.selected) {
            option.style.backgroundColor = '';
        }
    });
}

// Have listeners for all the html fields to see when the user chooses an item
function mulListeners() {
    const multipleSelects = document.querySelectorAll('select[multiple]');
    multipleSelects.forEach(selElement => {
        selElement.addEventListener('change', function() {
            checkmarkLogic(selElement);
        });
        checkmarkLogic(selElement);
    });
}


document.addEventListener('DOMContentLoaded', function() {
    mulListeners();
});
