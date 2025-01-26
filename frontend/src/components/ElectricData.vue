<script setup>
function borderSuccess(status) {
  const formElement = document.getElementById("elecForm");
  if (status === 201) {
    console.log(message.data);
    formElement.style.borderColor = "green";
  }
  else {
    formElement.style.borderColor = "red";
  }
  setTimeout(() => {formElement.style.borderColor = "transparent";}, 2000);
}

function getElectricData() {
  const state = document.getElementById("resState").value;
  const kWh = document.getElementById("kwh").value;
  try {
    const response = fetch(`http://localhost:5000/process-electricity-data?state=${state}&kwh=${kWh}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    console.log("Response Status:", response.status);
    borderSuccess(response.status);
  } catch (error) {
    console.error("Error fetching drive data:", error);
    borderSuccess(500);
  }
}
</script>

<template>
  <form action="/process-electricity-data" method="POST" id="elecForm">
    <h2>What's Your Electric Usage?</h2>
    <label for="resState">State:</label>
    <div class="select">
      <select name="resState" id="resState">
        <option>AL</option>
        <option>AK</option>
        <option>AZ</option>
        <option>AR</option>
        <option>CA</option>
        <option>CO</option>
        <option>CT</option>
        <option>DE</option>
        <option>FL</option>
        <option>GA</option>
        <option>HI</option>
        <option>ID</option>
        <option>IL</option>
        <option>IN</option>
        <option>IA</option>
        <option>KS</option>
        <option>KY</option>
        <option>LA</option>
        <option>ME</option>
        <option>MD</option>
        <option>MA</option>
        <option>MI</option>
        <option>MN</option>
        <option>MS</option>
        <option>MO</option>
        <option>MT</option>
        <option>NE</option>
        <option>NV</option>
        <option>NH</option>
        <option>NJ</option>
        <option>NM</option>
        <option>NY</option>
        <option>NC</option>
        <option>ND</option>
        <option>OH</option>
        <option>OK</option>
        <option>OR</option>
        <option>PA</option>
        <option>RI</option>
        <option>SC</option>
        <option>TN</option>
        <option>TX</option>
        <option>UT</option>
        <option>VT</option>
        <option>VA</option>
        <option>WA</option>
        <option>WV</option>
        <option>WI</option>
        <option>WY</option>
      </select><br><br>
      <span class="focus"></span>
    </div>
    <label for="kwh">Kwh of electricity used:</label>
    <input type="text" id="kwh"><br><br>
    <button @click="getElectricData" type="button">Submit</button>
  </form>
</template>

<style scoped>
</style>