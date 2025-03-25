// Namespace to group different pages for certain scripts
const app = {};

// For login.html to redirect user to admin_dashboard.html upon successful login
// And to display an error msg upon incorrect credentials
app.loginPage = function() {
    // Confirm current page
    if (document.documentElement.classList.contains('login_page')) {
        $(document).ready(function() {
            // Temporary
            // Will ultimately query a database for correct login credentials
            const valid_username = "admin";
            const valid_password = "admin";

            $(`#error_msg`).hide();

            $(`#login_form`).on("submit", function(event) {
                event.preventDefault();

                // Grab inputted credentials
                const username = $(`#username`).val();
                const password = $(`#password`).val();

                // Compare with valid ones
                if (username === valid_username && password === valid_password) {
                    // If valid, then redirect to admin dashboard
                    window.location.href = "admin_dashboard.html";
                }
                else {
                    // Display error message
                    $(`#error_msg`).show();
                }
            });
        });
    }
};

// For add_item.html image display functionality
app.imageDisplay = function() {
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
};

// Init function for different JavaScript scripts
app.init = function() {
    app.loginPage();
    app.imageDisplay();
}

// If page is ready, then init scripts
$(document).ready(function() {
    app.init();
});