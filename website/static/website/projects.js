var allProjectIds = [];

document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.search-icon');
    const textbar = document.querySelector('.textbar');

    button.onclick = () => {
        textbar.focus()
    };

    allProjectIds.forEach(function(id) {
        fetch(`/project/${id}`)
        .then(response => response.json())
        .then(project => {
            const div = document.getElementById(String(id));

            project.badges.forEach(function(badge) {
                div.innerHTML += `<button class="badge-button">${badge}</button>`;
            });
        });
    });

    textbar.addEventListener('keydown', function(e) {
        if (e.keyCode == 13) {
            if (textbar.value) {
                window.location.href = `/projects/${textbar.value}/1`;
            } else {
                window.location.href = '/projects/1';
            }
        }
    });
});

function redirect(link) {
    window.location.href = link;
}

function add_id(id) {
    allProjectIds.push(id);
}
