function displayReplyForm(comment_id) {
    var reply_form = document.getElementById("reply_form_" + comment_id);

    if (reply_form.style.display === "none" || reply_form.style.display === "") {
        reply_form.style.display = "block";
    }
    else {
        reply_form.style.display = "none";
    }
}

function addReply(event, comment_id, reply_form) {
    event.preventDefault();

    var form_data = new FormData(reply_form);

    var base_url = window.location.pathname.split('/');
    var model = base_url[2];
    var item = base_url[3];

    var url = `/subnautica/${model}/${item}/comment/${comment_id}/reply/`;

    console.log("Sending request to", url);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");

    xhr.onload = function () {
        console.log("XHR status", xhr.status);
        console.log("XHR Response:", xhr.responseText);
        if (xhr.status === 200) {
            var reply = JSON.parse(xhr.responseText);

            var reply_html = `
                <div class="reply">
                    <div class="user_info">
                        <img src="/static/img/reply_icon.jpg" alt="profile picture" class="profile_pic" />
                        <span class="username">${reply.username}</span>
                    </div>
                    <div class="comment_content">
                        <p class="comment_text">${reply.content}</p>
                        <span class="comment_date">Posted on: ${reply.created_at}</span>
                    </div>
                </div>
            `;

            var reply_wrapper = document.querySelector("#comment_" + comment_id + "_reply_wrapper");
            if (!reply_wrapper) {
                reply_wrapper = document.createElement("div");
                reply_wrapper.classList.add("reply_wrapper");
                document.querySelector("#comment_" + comment_id).appendChild(reply_wrapper);
            }

            reply_wrapper.innerHTML += reply_html;

            reply_form.querySelector('textarea[name="reply_content"]').value = '';
            console.log("DONE");
        }
        else {
            alert("Error posting reply");
        }
    };

    xhr.send(form_data);
}

function editComment(comment_id) {
    const comment_text = document.getElementById(`comment_text_${comment_id}`);
    const edit_form = document.getElementById(`edit_form_${comment_id}`);
    comment_text.style.dissplay = "none";
    edit_form.style.display = "block";
}