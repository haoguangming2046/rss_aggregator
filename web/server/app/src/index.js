import Vue from 'vue';

import NavBar from './components/NavBar.vue';
import Home from './pages/Home.vue';
import store from './store/index';

new Vue({
  el: '#main',
  components: {
    'nav-bar': NavBar,
    'home': Home,
  },
  store,
});
