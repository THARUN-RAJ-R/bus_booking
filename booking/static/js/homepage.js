function submitForm(formId, method, url) {
    var form = document.getElementById(formId);
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open(method, url + '?' + new URLSearchParams(formData).toString(), true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var resultsDiv = document.getElementById('results');
                resultsDiv.innerHTML = xhr.responseText;
            } else {
                console.error('Error:', xhr.status);
            }
        }
    };
    xhr.send();
}

function booking()
{
    window.location.href = '/bus/booking';
}