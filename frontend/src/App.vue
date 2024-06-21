<template>
  <div id="app">
    <!-- <nav>
      <!--<router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
      <router-link to="/report">Report</router-link>
    </nav>-->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
nav {
  margin-bottom: 10px;
}

nav a {
  margin-right: 10px;
  text-decoration: none;
  color: #42b983;
}

nav a.router-link-exact-active {
  font-weight: bold;
}
</style>
