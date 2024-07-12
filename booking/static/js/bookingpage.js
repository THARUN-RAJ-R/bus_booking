document.getElementById('bookingForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const routeId = document.getElementById('routeId').value;
    const seatNumber = parseInt(document.getElementById('seatNumber').value);
    const errorDiv = document.getElementById('error');

    // Clear any previous error message
    errorDiv.textContent = '';

    if (seatNumber > 30) {
        alert('Error: Seat number cannot be greater than 30.');
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
        console.log('Response status:', response.status);
        if (!response.ok) {
            return response.json().then(data => {
                throw new Error(data.detail || 'Unknown error occurred');
            });
        }
        return response.json();
    })
    .then(data => {
        console.log('Response data:', data);
        if (data.error) {
            alert(`Error: ${data.error}`);
        } else {
            alert(`Route ID: ${routeId}, Seat Number: ${seatNumber} booked successfully!`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert(`Error: ${error.message}`);
    });
});
