var allBlogIds = [];

document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.search-icon');
    const textbar = document.querySelector('.textbar');

    button.onclick = () => {
        textbar.focus()
    };

    textbar.addEventListener('keydown', function(e) {
        if (e.keyCode == 13) {
            if (textbar.value) {
                window.location.href = `/blogs/${textbar.value}/1`;
            } else {
                window.location.href = '/blogs/1';
            }
        }
    });
});

function redirect(link) {
    window.location.href = link;
}

function add_id(id) {
    allBlogIds.push(id);
}
