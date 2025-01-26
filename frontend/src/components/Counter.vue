<template>
  <a @click="fetchValue">
  <div class="fixed">
    Total Emissions:<br>
    {{ emissionCount }}
  </div>
  </a>
</template>

<script>
export default {
  data() {
    return {
      emissionCount: "",
    };
  },
  methods: {
    async fetchValue() {
      try {
        const response = await fetch("http://localhost:5000/get-total-emissions");
        const data = await response.json();
        this.emissionCount = `${data.kg} kg / ${data.lb} lb`;
      } catch (error) {
        const response = await fetch("http://localhost:5000/get-total-emissions");
        const data = await response.json();
        console.log(data);
        console.error("Error fetching value:", error);
      }
    },
  },
  mounted() {
    this.fetchValue();
  },
};
</script>
