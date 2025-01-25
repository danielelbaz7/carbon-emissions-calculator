<script setup>

</script>

<template>
  <form action="/process-car-data" method="POST" id="carForm">
    <h2>Enter your Car Information:</h2>
    <label for="curlocCar">Make:</label><br>
    <input type="text" id="curlocCar"><br>
    <label for="deslocCar">Model:</label><br>
    <input type="text" id="deslocCar"><br><br>
    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>

</style>