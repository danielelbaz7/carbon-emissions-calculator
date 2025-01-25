<script setup>

</script>

<template>
  <form action="/process-flight-data" method="POST" id="flightForm">
    <h2>Enter Your Flight Data:</h2>
    <label for="curlocFlight">Departing Airport:</label><br>
    <input type="text" id="curlocFlight"><br>
    <label for="deslocFlight">Destination Airport:</label><br>
    <input type="text" id="deslocFlight"><br><br>
    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>