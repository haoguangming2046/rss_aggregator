<template lang='pug'>
// Component to Render Notification Alert
div.row.v-notification("v-if"='canShowNotification')
  div.col-sm-12
    div.alert(:class='context' role="alert") {{message}}
</template>

<script>
export default {
	props: {
		message: {
			type: String,
			default: "Unknown Error Occured",
		},
		context: {
			type: String,
			default: "alert-danger",
		},
		time: {
			type: Number,
			default: 4000,
		},
	},
	data() {
		return {
			canShowNotification: true,
		};
	},
	mounted() {
		setTimeout(() => {
			this.canShowNotification = false;
		}, this.time);
	},
};
</script>

<style scoped>
.v-notification {
  display: inline-block; margin: 0 auto;
  transition: all 0.5s ease-in-out;
  z-index: 200;
  animation-iteration-count: 1;
  right: 0;
  top: 0;
  width: 100%;
}
</style>