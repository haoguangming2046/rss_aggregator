<template lang="pug">
// Component to Render Feed List in Home Page
div
  template(v-if='getCurrentFeeds.length > 0')
    template(v-for='feed in getCurrentFeeds')
      feed(:feed='feed')
    div.row
      div.col-sm-4.offset-sm-4
        button.btn.btn-lg.btn-outline-primary(@click='loadMoreFeeds()') Load More Feeds ...
  template(v-else)
    div
      div.mb-4.p-2.c-card.c-slide-animated
        div.row.mx-3.mb-3
          div.col-sm-12.text-center
            a(href='/settings')
              h5(v-if='getCommonData.isAdmin') No feeds as of yet, add some Feed Sources to get started
                i.ml-2.fa.fa-arrow-right
              h5(v-else) No feeds to show, wait for a little while
</template>

<script>
import Feed from "./Feed.vue";

export default {
	components: {
		"feed": Feed,
	},
	computed: {
		getCurrentFeeds() {
			return this.$store.state.currentFeeds;
		},
		getCommonData() {
			return this.$store.state.commonData;
		}
	},
	mounted () {
		if (this.$store.getters.totalFeedCount == 0) {
			this.$store.commit("getCustomFeeds");
		}
	},
	methods: {
		loadMoreFeeds() {
			this.$store.commit("getCustomFeeds", {paginate: true});
		}
	}
};
</script>
