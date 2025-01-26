<script setup>
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

  <section class="content">
    <h3>This webpage was made for the SwampHacks X Hackathon!</h3>
    <p>
      We developed this website to help track people's carbon emissions. Regular activities can often be
      detrimental to the environment, so we developed a calculator to help people see just how
      much impact their trips and electricity can have.
    </p>
  </section>
</template>

<style scoped>
/* Basic resets (optional) */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* A clean sans-serif font for a modern look */
:root {
  font-family: Arial, Helvetica, sans-serif;
  /* Primary color for header background */
  --primary-color: #27ae60;
  /* Secondary/hover color */
  --secondary-color: #2ecc71;
  /* Text color for header links */
  --header-text-color: #ffffff;
  /* Body background color */
  --body-bg: #f9f9f9;
  /* General text color */
  --text-color: #333;
}

/* Body styling */
body {
  background-color: var(--body-bg);
  color: var(--text-color);
}

/* Header container */
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #4CAF50;
  padding: 1rem 2rem;
}

/* Logo or brand name */
.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

/* Logo link styling */
.homelink {
  text-decoration: none;
  color: var(--header-text-color);
}

.homelink:hover {
  text-decoration: underline;
}

/* Navigation links */
.links a {
  margin-left: 2rem;
  color: var(--header-text-color);
  text-decoration: none;
  font-weight: 500;
}

.links a:hover {
  text-decoration: underline;
}

/* Main content section */
.content {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.content h3 {
  margin-bottom: 1rem;
  text-align: center;
}

.content p {
  line-height: 1.6;
  font-size: 1.1rem;
}
</style>
