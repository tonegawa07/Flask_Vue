<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <!--  -->
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Flask_Vue</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <!--  -->
    </v-main>
    <v-footer padless>
      <v-col
        class="text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>©Yusuke Fukuda</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data: () => ({ drawer: null }),
  }
</script>