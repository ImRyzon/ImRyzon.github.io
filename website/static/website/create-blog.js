document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('create-blog-form');

    form.onsubmit = function(event) {
        event.preventDefault();

        const title = document.getElementById('form-title').value;
        const description = document.getElementById('form-description').value;
        const content = document.getElementById('form-content').value;
        const approxLength = document.getElementById('form-length').value;
        const imagePath = document.getElementById('form-path').value;
        const isActive = document.getElementById('form-is-active').checked;

        fetch('/create-blog', {
            method: 'POST',
            body: JSON.stringify({
                title: title,
                description: description,
                content: content,
                approxLength: approxLength,
                imagePath: imagePath,
                isActive: isActive
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            window.location.href = '/blogs/1';
        });
    };
})