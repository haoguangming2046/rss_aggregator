<template lang="pug">
// Component to Render Feed List in Home Page
div
  template(v-for='feed in getCurrentFeeds')
    feed(:feed='feed')
</template>

<script>
import Vue from 'vue';
import marked from 'marked';

import Feed from './Feed.vue';

export default {
  components: {
    'feed': Feed,
  },
  computed: {
    getCurrentFeeds() {
      return this.$store.state.currentFeeds;
    },
  },
}
</script>
