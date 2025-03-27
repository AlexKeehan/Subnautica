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

// Init function for different JavaScript scripts
app.init = function() {
    app.loginPage();
}

// If page is ready, then init scripts
$(document).ready(function() {
    app.init();
});