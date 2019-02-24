<template lang="pug">
// Component to Render Left Side Bar
div.c-card.c-slide-animated
  div.mx-4.py-2
    h5
      a.c-navbar-text-underline.c-black-text(href="#" @click='getAllFeed()') All Feeds
    h6
      a(href="#" @click='setCategory(-1)').c-navbar-text-underline.c-black-text Current
        span(v-if='showFeedNumbers').badge.badge-secondary.ml-2 {{getTotalFeedCount}}
    template(v-for="category in categories")
      h6(v-if='category.id == 0')
        a(href="#" @click='setCategory(category.id)').c-navbar-text-underline.c-black-text {{category.name}}
          span(v-if='showFeedNumbers').badge.badge-secondary.ml-2 {{getFavouriteFeedCount}}
      h6(v-else)
        a(href="#" @click='setCategory(category.id)').c-navbar-text-underline.c-black-text {{category.name}}
          span(v-if='showFeedNumbers').badge.badge-secondary.ml-2 {{$store.state.categoryFeedCount[category.id]}}
</template>

<script>
import helpers from "../helpers/index";

export default {
	mixins: [helpers],
	props: {
		showFeedNumbers: {
			type: Boolean,
			default: true,
		}
	},
	data() {
		return {
			categories: [],
		};
	},
	computed: {
		getTotalFeedCount() {
			return this.$store.getters.totalFeedCount;
		},
		getFavouriteFeedCount() {
			return this.$store.getters.favouriteFeedCount;
		}
	},
	created() {
		this.$axios.get("/api/feed/sources").then(response => {
			const categories = [{
				id: "0",
				name: "Favourites",
			}];
			if ("data" in response.data) {
				response.data.data.forEach(category => {
					categories.push({
						id: category.id,
						name: category.name,
					});
				});
				this.categories = categories;
			}
		}).catch(() => {
			this.createNotification({context: "alert-danger", message: "Could not contact server :("});
		});
	},
	methods: {
		setCategory(categoryId) {
			this.$store.commit("setCategory", categoryId);
		},
		getAllFeed() {
			this.$store.commit("getFeeds");
		}
	},
};
</script>
