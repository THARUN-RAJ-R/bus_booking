document.getElementById('bookingForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const routeId = document.getElementById('routeId').value;
    const seatNumber = parseInt(document.getElementById('seatNumber').value);
    const messageDiv = document.getElementById('message');

    if (seatNumber > 30) {
        messageDiv.innerHTML = '<p>Error: Seat number cannot be greater than 30.</p>';
        return;
    }

    const formData = new FormData();
    formData.append('route_id', routeId);
    formData.append('seat_number', seatNumber);

    fetch('/bus/booking', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.detail);
            });
        }
        return response.json();
    })
    .then(data => {
        messageDiv.innerHTML = `<p>Route ID: ${routeId}, Seat Number: ${seatNumber} booked successfully!</p>`;
    })
    .catch(error => {
        messageDiv.innerHTML = `<p> ${error.message}</p>`;
    });
});
