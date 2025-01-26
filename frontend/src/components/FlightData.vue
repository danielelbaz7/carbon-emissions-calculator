<script>
import {getFlightData} from "@/calculator.js";
import {defineComponent} from "vue";

export default defineComponent({
  methods: {getFlightData}
})

export let curloc = null
export let desloc = null
</script>

<template>
  <form @action="getFlightData" method="POST" id="flightForm">
    <h2>Enter Your Flight Data:</h2>
    <label for="curlocFlight">Departing Airport:</label><br>
    <input v-model="curloc" type="text" id="curlocFlight"><br>
    <label for="deslocFlight">Destination Airport:</label><br>
    <input v-model="desloc" type="text" id="deslocFlight"><br><br>
    <button @click="getFlightData" type="button">Submit</button>
  </form>
</template>

<style scoped>

</style>