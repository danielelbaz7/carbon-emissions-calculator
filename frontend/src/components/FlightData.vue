<script>
import {defineComponent} from "vue";

export default defineComponent({
  methods: {
    async getFlightData() {
      const departure = this.curloc;
      const destination = this.desloc;
      try {
        const response = await fetch(`http://localhost:5000/process-flight-data?curloc=${departure}&desloc=${destination}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        });
        console.log("Response Status:", response.status);
        this.borderSuccess(response.status);
      } catch (error) {
        console.error("Error fetching flight data:", error);
        this.borderSuccess(500);
      }
    },/*
        body: JSON.stringify({
          curloc: departure,
          desloc: destination,
        }),
      });

      this.borderSuccess({code: response});
    },*/

    borderSuccess(status) {
      const formElement = document.getElementById("flightForm");
      if (status === 201) {
        console.log(message.data);
        formElement.style.borderColor = "green";
      }
      else {
        formElement.style.borderColor = "red";
      }
      setTimeout(() => {formElement.style.borderColor = "transparent";}, 2000);
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
  <form @submit.prevent="getFlightData" method="POST" id="flightForm">
    <h2>Enter Your Flight Data:</h2>
    <label for="curlocFlight">Departing Airport:</label>
    <input v-model="curloc" type="text" id="curlocFlight"><br><br>
    <label for="deslocFlight">Destination Airport:</label>
    <input v-model="desloc" type="text" id="deslocFlight"><br><br>
    <button @click="getFlightData" type="button">Submit</button>
  </form>
</template>

<style scoped>

</style>
