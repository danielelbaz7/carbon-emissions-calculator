<script>

</script>

<template>
  <form action="getElectricData" method="POST" id="elecForm">
    <h2>What's Your Electric Usage?</h2>
    <label for="resState">State:</label>
    <div class="select">
      <select name="resState" id="resState">
      </select><br><br>
      <span class="focus"></span>
    </div>
    <label for="kwh">Kwh of electricity used:</label><br>
    <input type="text" id="kwh"><br><br>
    <button type="submit">Submit</button>
  </form>
</template>

<style scoped>
</style>