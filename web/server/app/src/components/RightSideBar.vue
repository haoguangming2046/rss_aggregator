<template lang="pug">
// Component to Render Right Side Bar Advertisements
div.text-center
  template(v-for="ad in ads")
    div.mb-2.c-card.c-slide-animated
      h6.text-left.pl-2.pt-2 Ads by Priyank
      div.mx-4.py-2
        h5
          a.c-navbar-text-underline.c-black-text(:href="ad.link" target="_blank") {{ad.name}}
        a(:href="ad.link" target="_blank")
          img.v-ad-img.rounded-circle(:src="ad.background")
</template>

<script>
export default {
	data() {
		return {
			ads: [
				{name: "Pyfiddle.io", "link": "https://pyfiddle.io", background: "https://zappa-rhv3u5qby.s3.amazonaws.com/images/python-logo.png"},
				{name: "Priyank's Humble Adobe", "link": "https://priyank.co.uk", background: "https://priyank.co.uk/img/about-alt.jpg"},
				{name: "Clarion Call", "link": "https://clarioncall.in", background: "http://clarioncall.in/assets/images/section-13.jpg"}
			],
		};
	}
};
</script>

<style lang="scss" scoped>
@import "../../static/css/_variables.scss";

.v-ad-img {
  height: 6rem;
  width: 6rem;
}
</style>
