
<script setup>
import {onMounted} from "vue";
import {getVehicleMakes} from "@/calculator.js";

onMounted(() => {
  let makes = getVehicleMakes()
  let select = document.getElementById("curlocCar");
  for (let i = 0; i < 10; i++) {
    let option = document.createElement("option");
    option.value = makes[i];
    option.innerText = makes[i];
    select.appendChild(option);
  }
})
</script>

<template>
  <form action="/process-car-data" method="POST" id="carForm">
    <h2>Have you Driven Recently?</h2>
    <label for="curlocCar">Make:</label>
    <div class="select">
      <select name="curlocCar" id="curlocCar">
        <option value="volvo">Volvo</option>
        <option value="bugatti">Andrew Tate Bugatti</option>
      </select><br><br>
      <span class="focus"></span>
    </div>
    <label for="deslocCar">Model:</label><br>
    <input type="text" id="deslocCar"><br>
    <label for="milDriv">Miles Driven:</label><br>
    <input type="text" id="milDriv"><br><br>
    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>