import Vue from 'vue'
import vuetify from './plugins/vuetify'
import App from './App.vue'
import store from './store'
import router from './router/index'
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader
import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader
import '@fortawesome/fontawesome-free/css/all.css' // Ensure you are using css-loader

Vue.config.productionTip = false

// Vue使います
new Vue({
  // Appコンポーネントを埋め込みます
  render: h => h(App),
  ei: '#app',
  // Vuetify 使います
  vuetify, 
  // Vue router 
  router,
  // Vuex store 使います
  store,
  data: {}
}).$mount('#app')
