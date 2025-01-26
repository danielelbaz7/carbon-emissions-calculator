<script>
import {defineComponent} from "vue";

export default defineComponent({
  methods: {
    async getFlightData() {
      let departure = this.curloc;
      let destination = this.desloc;
      let response = fetch(`http://localhost:5000/process-flight-data?curloc=${departure}&desloc=${destination}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          curloc: departure,
          desloc: destination,
        }),
      });

      this.borderSuccess({code: response});
    },

    borderSuccess(message) {
      if (message.code === 201) {
        console.log(message.data);
        document.getElementById("flightForm").style.borderColor="green";
      }
      else {
        document.getElementById("flightForm").style.borderColor="red";
      }
    }
  }
})

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

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
