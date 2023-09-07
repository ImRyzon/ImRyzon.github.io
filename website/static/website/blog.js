function initComments(blog_id) {
    fetch(`/comments/${blog_id}`)
    .then(response => response.json())
    .then(comments => {
        console.log(comments);
        if (comments.length > 0) {
            const parentDiv = document.getElementById('comment-parent');
            parentDiv.innerHTML = "";

            comments.forEach(function(comment) {
                const flexStartDiv = document.createElement('div');
                flexStartDiv.setAttribute('class', 'd-flex flex-start mt-4');
                flexStartDiv.innerHTML += '<img class="rounded-circle shadow-1-strong me-3" src="/static/website/images/default-pfp.png" alt="avatar" width="65" height="65"/>';

                const secondaryDiv = document.createElement('div');
                secondaryDiv.setAttribute('id', `secondary-div-${comment.id}`);
                secondaryDiv.setAttribute('class', 'flex-grow-1 flex-shrink-1');
                secondaryDiv.innerHTML = `<div id="${comment.id}"><div class="d-flex justify-content-between align-items-center"><p class="mb-1"><b>${comment.first_name} ${comment.last_name}</b><span class="small"><b> - ${comment.date} (UTC)</b></span></p><button style="border: none; background: none; color: blue; font-weight: bold;" onclick="showForm(${comment.id}, '${comment.first_name} ${comment.last_name}', ${comment.id})"><i class="fas fa-reply fa-xs"></i><span class="small"> reply</span></button></div><p class="small mb-0" style="display: inline-block; text-align: left; margin-top: 20px; margin-bottom: 20px;">${comment.content}</p></div>`;

                fetch(`/replies/${comment.id}`)
                .then(response => response.json())
                .then(replies => {
                    console.log(replies);
                    replies.forEach(function(reply) {
                        secondaryDiv.innerHTML += `<div id="${reply.id}" class="d-flex flex-start mt-4"><a class="me-3" href="#"><img class="rounded-circle shadow-1-strong" src="/static/website/images/default-pfp.png" alt="avatar" width="65" height="65"/></a><div class="flex-grow-1 flex-shrink-1"><div><div class="d-flex justify-content-between align-items-center"><p class="mb-1"><b>${reply.first_name} ${reply.last_name}</b><span class="small"><b> - ${reply.date} (UTC)</b></span></p><button style="border: none; background: none; color: blue; font-weight: bold;" onclick="showForm(${reply.id}, '${reply.first_name} ${reply.last_name}', ${comment.id})"><i class="fas fa-reply fa-xs"></i><span class="small"> reply</span></button></div><p class="small mb-0" style="display: inline-block; text-align: left; margin-top: 20px; margin-bottom: 20px;">${reply.content}</p></div></div></div>`;
                    });
                });

                flexStartDiv.append(secondaryDiv);
                parentDiv.append(flexStartDiv);
                for (let i = 0; i < 2; i++) parentDiv.append(document.createElement('br'));
            });
        } else {
            document.getElementById('alternative-comments').innerHTML = '<h3 style="font-weight: bold; margin-top: 50px;">Sorry, nothing to find here just yet :(</h3>';
        }
    });
}

function showForm(comment_id, sourcePing, parent_id) {
    const formDiv = document.createElement('div');
    formDiv.setAttribute('id', `form-div-${comment_id}`);

    const formHTML = 
    `
    <div class="d-flex flex-start mt-4" id="reply-div-${comment_id}">
        <a class="me-3" href="#">
            <img class="rounded-circle shadow-1-strong"
                src="/static/website/images/default-pfp.png" alt="avatar"
                width="65" height="65" />
        </a>
        <div class="flex-grow-1 flex-shrink-1" style="border: 1px solid black; border-radius: 10px;">
            <div>
                <form onsubmit="createReply(event, ${comment_id}, ${parent_id})" id="reply-form-${comment_id}" data-parent="${parent_id}" style="margin: 25px;">
                    <input required id="comment-first-name-${comment_id}" minlength="2" type="text" placeholder="Enter first name">
                    <input required id="comment-last-name-${comment_id}" minlength="2" type="text" placeholder="Enter last name">
                    <textarea required rows="5" cols="46" minlength="2" id="comment-content-${comment_id}" placeholder="Enter content" style="margin-top: 20px;">@${sourcePing}</textarea>
                    <div style="display: inline-block;">
                        <input type="submit" value="Reply" class="paginator-button" style="margin-top: 30px; margin-bottom: 15px;">
                        <button class="paginator-button" style="margin-top: 30px; margin-bottom: 15px;" onclick="(() => document.getElementById('reply-div-${comment_id}').remove())()">Cancel</button>
                    </div>
                <form/>
            </div>
        </div>
    </div>
    `;
    formDiv.innerHTML = formHTML;

    const secondaryDiv = document.getElementById(`${parent_id}`);
    secondaryDiv.append(formDiv);
}

function createReply(event, source_id, parent_id) {
    event.preventDefault();

    const firstName = document.getElementById(`comment-first-name-${source_id}`);
    const lastName = document.getElementById(`comment-last-name-${source_id}`);
    const content = document.getElementById(`comment-content-${source_id}`);

    fetch(`/create-reply/${parent_id}`, {
        method: 'POST',
        body: JSON.stringify({
            first_name : firstName.value,
            last_name: lastName.value,
            content: content.value
        })
    })
    .then(response => response.json())
    .then(reply => {
        console.log(reply);

        const secondaryDiv = document.getElementById(`secondary-div-${parent_id}`);
        const replyDiv = document.createElement('div')
        replyDiv.setAttribute('id', `${reply.id}`);
        replyDiv.setAttribute('class', 'd-flex flex-start mt-4');
        replyDiv.innerHTML = `<a class="me-3" href="#"><img class="rounded-circle shadow-1-strong" src="/static/website/images/default-pfp.png" alt="avatar" width="65" height="65"/></a><div class="flex-grow-1 flex-shrink-1"><div><div class="d-flex justify-content-between align-items-center"><p class="mb-1"><b>${reply.first_name} ${reply.last_name}</b><span class="small"><b> - ${reply.date} (UTC)</b></span></p><button style="border: none; background: none; color: blue; font-weight: bold;" onclick="showForm(${reply.id}, '${reply.first_name} ${reply.last_name}', ${parent_id})"><i class="fas fa-reply fa-xs"></i><span class="small"> reply</span></button></div><p class="small mb-0" style="display: inline-block; text-align: left; margin-top: 20px; margin-bottom: 20px;">${reply.content}</p></div></div>`;

        secondaryDiv.append(replyDiv);
    })

    document.getElementById(`reply-div-${source_id}`).remove();
}