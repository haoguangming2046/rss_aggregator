import Vue from 'vue';

import NavBar from './components/NavBar.vue';
import Home from './pages/Home.vue';

new Vue({
  el: '#main',
  components: {
    'navbar': NavBar,
    'home': Home,
  },
});
