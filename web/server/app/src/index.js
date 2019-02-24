import Vue from "vue";

import NavBar from "./components/NavBar.vue";
import Home from "./pages/Home.vue";
import Settings from "./pages/Settings.vue";
import FeedDetail from "./pages/FeedDetail.vue";
import store from "./store/index";
import axios from "./globals";

Vue.prototype.$axios = axios;

new Vue({
	el: "#main",
	components: {
		"nav-bar": NavBar,
		"home": Home,
		"detail": FeedDetail,
		"settings": Settings,
	},
	store,
});
