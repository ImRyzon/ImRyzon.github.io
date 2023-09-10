document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('create-project-form');

    form.onsubmit = function(event) {
        event.preventDefault();

        const title = document.getElementById('form-title').value;
        const description = document.getElementById('form-description').value;
        const imagePath = document.getElementById('form-path').value;

        const badges = [];
        const badgeSelect = document.getElementById('form-badges');
        for (let i = 0; i < badgeSelect.length; i++) {
            if (badgeSelect.options[i].selected) {
                badges.push(badgeSelect.options[i].text);
            }
        }

        const projectLink = document.getElementById('form-link').value;
        const inProgress = document.getElementById('form-in-progress').checked;

        fetch('/create-project', {
            method: 'POST',
            body: JSON.stringify({
                title: title,
                description: description,
                imagePath: imagePath,
                badges: badges,
                projectLink: projectLink,
                inProgress: inProgress
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            window.location.href = '/projects/1';
        });
    };
})