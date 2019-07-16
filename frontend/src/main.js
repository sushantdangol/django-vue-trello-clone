import Vue from 'vue'
import App from './App.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
// import router from './route.js';
import router from './route'

new Vue({
  el: '#app',
  router,
  render: h => h(App),
});
