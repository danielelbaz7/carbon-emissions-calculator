// JavaScript function to handle form submission
function submitForm(event) {
    // Prevent the form from refreshing the page
    event.preventDefault();

    // Get the input values
    const currentLocation = document.getElementById('curloc').value;
    const destination = document.getElementById('desloc').value;

    // Create the data to send to the backend
    const data = {
        curloc: currentLocation,
        desloc: destination
    };

    // Use fetch to send a POST request
    fetch('/process-data', { // Update with your Flask route
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(result => {
        console.log('Success:', result);
        alert('Data submitted successfully!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error submitting the data.');
    });
}

// Attach the event listener to the form
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('carbonForm');
    form.addEventListener('submit', submitForm);
});
