document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const messageElement = document.getElementById('message');

    const response = await fetch('/auth/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'username': username,
            'password': password
        })
    });

    const result = await response.json();

    if (response.ok) {
        localStorage.setItem('access_token', result.access_token);
        window.location.href = '/homepage';
    } else {
        messageElement.style.color = 'red';
        messageElement.textContent = result.detail;
    }
});
