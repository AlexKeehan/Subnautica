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

document.addEventListener("DOMContentLoaded", function() {
    const modelSelect = document.getElementById('select_model');
    const itemSelect = document.getElementById('item_element');

    modelSelect.addEventListener('change', function() {
        const model = modelSelect.value;

        console.log('Model selected:', model); // Log the model selected

        // Perform AJAX request to update item list based on selected model
        fetch(`/subnautica/edit_item/?select_model=${model}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json(); // Only proceed if the response is OK
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log('Received data:', data); // Log the data received from the server

            // Clear the existing item options
            itemSelect.innerHTML = '<option value="">Select An Item</option>';

            // Populate new item options
            data.item_list.forEach(item => {
                const option = document.createElement('option');
                option.value = item.id;
                option.textContent = item.name;
                itemSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error updating item list:', error);
        });
    });
});
