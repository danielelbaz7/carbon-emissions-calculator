
<script setup>
import {getVehicleMakes} from "@/calculator.js";
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
    <input type="text" id="deslocCar">
    <label for="milDriv">Miles Driven:</label><br>
    <input type="text" id="milDriv"><br><br>
    <button @click="" type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>