<template lang="pug">
// Component to Render Home View for Home Page
div.container-fluid.my-3
  div.row
    div.col-sm-2
      left-side-bar
    div.col-sm-7
      feed-list
    div.col-sm-3
      right-side-bar
</template>

<script>
import LeftSideBar from "../components/LeftSideBar";
import RightSideBar from "../components/RightSideBar";
import FeedList from "../components/FeedList";

export default {
	components: {
		"left-side-bar": LeftSideBar,
		"right-side-bar": RightSideBar,
		"feed-list": FeedList,
	},
	props: {
		commonData: {
			type: Object,
			default: () => "{}",
		},
	},
	created () {
		this.$store.commit("setCommonData", this.commonData);
	},
};
</script>