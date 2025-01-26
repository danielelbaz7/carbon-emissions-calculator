// JavaScript function to handle form submission
function submitForm(event) {
    // Prevent the form from refreshing the page
    event.preventDefault();

    // Use fetch to send a POST request
    console.log("Test")
    fetch(`localhost:5000/process-data?curloc=${this.curloc}&desloc=${this.desloc}`, { // Update with your Flask route
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
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

function borderSuccess(code) {
    if (code == 200) {
        document.getElementById("flightForm").style.borderColor="green";
    }
    else {
        document.getElementById("flightForm").style.borderColor="red";
    }
}