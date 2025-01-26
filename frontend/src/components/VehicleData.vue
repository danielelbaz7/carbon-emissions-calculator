
<script setup>
import {getVehicleMakes} from "@/calculator.js";
import {onMounted, onUpdated} from "vue";

onMounted( () =>
  getVehicleMakes().then((response) => response.json()).then((makes) => {
    let select = document.getElementById("curlocCar");
    for (let i = 0; i < makes.length - 1; i++) {
      let option = document.createElement("option");
      option.value = makes[i];
      option.innerText = makes[i];
      select.appendChild(option);
    }
  })
)

onUpdated(() => {
  getVehicleModels().then((response) => response.json()).then((models) => {
    let select = document.getElementById("deslocCar");
    for (let i = 0; i < models.length - 1; i++) {
      let option = document.createElement("option");
      option.value = models[i];
      option.innerText = models[i];
      select.appendChild(option);
    }
  })
})

</script>

<template>
  <form action="/process-car-data" method="POST" id="carForm">
    <h2>Have you Driven Recently?</h2>
    <label for="curlocCar">Make:</label>
    <div class="select">
      <select name="curlocCar" id="curlocCar">
      </select><br><br>
      <span class="focus"></span>
    </div>
    <label for="deslocCar">Model:</label><br>
    <div class="select">
      <select name="deslocCar" id="deslocCar">
      </select><br><br>
    </div>
    <label for="milDriv">Miles Driven:</label><br>
    <input type="text" id="milDriv"><br><br>
    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>