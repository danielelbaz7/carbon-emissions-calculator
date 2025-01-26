<script setup>
import FlightData from "@/components/FlightData.vue";
import VehicleData from "@/components/VehicleData.vue";
import Counter from "@/components/Counter.vue";
</script>

<template>
  <div class="header">
    <div class="logo">
      <a href="/" class="homelink">Carbon Calculator</a>
    </div>
    <div class="links">
      <a href="/about">About Us</a>
    </div>
  </div>
  <Counter/>
  <FlightData/>

  <VehicleData/>
</template>