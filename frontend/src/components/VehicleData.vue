
<script setup>
import {getVehicleMakes, getVehicleModels} from "@/calculator.js";
import {onMounted, defineComponent} from "vue";

onMounted( () =>
  getVehicleMakes().then((response) => response.json()).then((makes) => {
    let select = document.getElementById("curlocCar");
    for (let i = 0; i < makes.ids.length - 1; i++) {
      let option = document.createElement("option");
      option.value = makes.ids[i];
      option.innerText = makes.names[i];
      select.appendChild(option);
    }
  })
)


function updateModels(event) {
  let make = document.getElementById("curlocCar").value;
  getVehicleModels(make).then((response) => response.json()).then((models) => {
    let select = document.getElementById("deslocCar");
    for (let i = 0; i < models.ids.length - 1; i++) {
      let option = document.createElement("option");
      option.value = models.ids[i];
      option.innerText = models.names[i];
      select.appendChild(option);
    }
  })
}

function borderSuccess(status) {
  const formElement = document.getElementById("carForm");
  if (status === 201) {
    console.log(message.data);
    formElement.style.borderColor = "green";
  }
  else {
    formElement.style.borderColor = "red";
  }
  setTimeout(() => {formElement.style.borderColor = "transparent";}, 2000);
}

function getDriveData() {
  const model = document.getElementById("deslocCar").value;
  const distance = document.getElementById("milDriv").value;
  try {
    const response = fetch(`http://localhost:5000/process-car-data?deslocCar=${model}&milDriv=${distance}`, {
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
  <form action="/process-car-data" method="POST" id="carForm">
    <h2>Miles Driven This Past Month:</h2>
    <label for="curlocCar">Make:</label>
    <div class="select">
      <select @change="updateModels" name="curlocCar" id="curlocCar">
      </select><br><br>
      <span class="focus"></span>
    </div>
    <label for="deslocCar">Model:</label><br>
    <select name="deslocCar" id="deslocCar">
      </select><br><br>
    <label for="milDriv">Miles Driven:</label><br>
    <input type="text" id="milDriv"><br><br>
    <button @click="getDriveData" type="button">Submit</button>
  </form>
</template>

<style scoped>

</style>