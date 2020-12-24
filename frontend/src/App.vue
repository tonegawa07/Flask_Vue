<template>
      <router-view/>
</template>

<script>
// import router from './router'


export default {
  name: "app",
  data: () => ({
    drawer: null
  }),
  components: {},
  props: {
    source: String
  }
};
</script>