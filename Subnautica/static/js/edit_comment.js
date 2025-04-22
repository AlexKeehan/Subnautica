document.addEventListener('DOMContentLoaded', function() {
    console.log("Edit Comments JS is loaded");

    // Get edit icons
    const edit_icons = document.querySelectorAll('.edit_icon');

    // Loop through and listen for clicks
    edit_icons.forEach(function(icon) {
        icon.addEventListener('click', function() {
            // Get data
            const comment_id = icon.getAttribute('data-comment-id');
            const edit_form = document.getElementById(`edit_form_${comment_id}`);

            console.log("Edit icon clicked for comment ID:", comment_id);

            // Toggle visibility of edit form
            if (edit_form.style.display === 'none' || edit_form.style.display === '') {
                edit_form.style.display = 'block';
            } else {
                edit_form.style.display = 'none';
            }
        });
    });

    // Handle form submission
    const edit_forms = document.querySelectorAll('.edit_comment_form_wrapper form');
    edit_forms.forEach(function(form) {
        // Wait for submit
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            // Get new data
            const form_data = new FormData(form);
            const comment_id = form_data.get('content_id');
            const content = form_data.get('content');
            const csrfToken = form_data.get('csrfmiddlewaretoken');

            // Construct url
            var baseUrl = window.location.pathname.split('/');
            var model = baseUrl[2];
            var item = baseUrl[3];

            var url = `/subnautica/${model}/${item}/comment/${comment_id}/edit/`;

            // Create an AJAX request to update the comment
            const xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.setRequestHeader('X-CSRFToken', csrfToken);

            xhr.onload = function() {
                console.log("XHR status", xhr.status);
                console.log("XHR Response:", xhr.responseText);
                if (xhr.status === 200) {
                    // Get new comment
                    const new_comment = JSON.parse(xhr.responseText);

                    // Update the comment text on the page
                    const comment_content = document.querySelector(`#comment_${comment_id} .comment_text`);
                    comment_content.textContent = new_comment.content;

                    // Hide the edit form after successful update
                    document.getElementById(`edit_form_${comment_id}`).style.display = "none";

                    console.log("Comment updated");
                }
                else {
                    alert("Error editing comment");
                }
            };
            xhr.send(form_data);
        });
    });
});
