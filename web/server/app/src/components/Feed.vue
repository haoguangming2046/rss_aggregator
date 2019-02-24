<template lang="pug">
// Component to Render Feed
div
  div.mb-4.p-2(:class='isFeedList ? "c-card c-slide-animated" : "" ')
    div.row
      div.col-sm-3.c-img-div
        a
          img.img-fluid(:src='feed.link' onerror="this.src='imagefound.gif';")
      div.col-sm-9
        div.row.pt-2
          div.col-sm-1
            template(v-if='getCommonData.isLoggedIn')
              button.btn.btn-secondary.btn-sm(v-if='!dataFeed.isStarred' @click='bookmark()' )
                i.fa.fa-star
              button.btn.btn-primary.btn-sm(v-else)
                i.fa.fa-star
          div.col-sm-11
            a.text-primary(:href='`/feed/${dataFeed.slug}/`')
              h4.text-primary {{dataFeed.title}}
        h6.v-word-break(v-html='dataFeed.summary')
</template>

<script>
import Vue from "vue";

export default {
	props: {
		feed: {
			type: Object,
			default: () => {},
		},
		isFeedList: {
			type: Boolean,
			default: true,
		},
	},
	data() {
		return {
			dataFeed: this.feed,
		};
	},
	computed: {
		getCommonData() {
			return this.$store.state.commonData;
		}
	},
	created() {
		Vue.set(this.dataFeed, "isStarred", false);
	},
	methods: {
		bookmark() {
			if (!this.isFeedList) Vue.set(this.dataFeed, "isStarred", true);
			this.$store.commit("bookmarkFeed", this.dataFeed);
		},
	}
};
</script>

<style lang="scss">
.v-word-break {
  word-break: break-all;
}
</style>
