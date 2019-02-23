<template lang="pug">
// Component to Render Left Side Bar
div.c-card.c-slide-animated
  div.mx-4.py-2
    h5
      a(href="#" @click='setCategory(-1)').c-navbar-text-underline.c-black-text Feeds
        span.badge.badge-secondary.ml-2 {{getTotalFeedCount}}
    template(v-for="category in categories")
      h6(v-if='category.id === 0')
        a(href="#" @click='setCategory(category.id)').c-navbar-text-underline.c-black-text {{category.name}}
          span.badge.badge-secondary.ml-2 {{getFavouriteFeedCount}}
      h6(v-else)
        a(href="#" @click='setCategory(category.id)').c-navbar-text-underline.c-black-text {{category.name}}
          span.badge.badge-secondary.ml-2 {{$store.state.categoryFeedCount[category.id]}}
</template>

<script>
export default {
  data() {
    return {
      categories: [
        {name: 'Favourites', id: 0},
        {name: 'reddit', id: 1},
        {name: 'medium', id: 2},
      ],
    }
  },
  computed: {
    getTotalFeedCount() {
      return this.$store.getters.totalFeedCount;
    },
    getFavouriteFeedCount() {
      return this.$store.getters.favouriteFeedCount;
    }
  },
  methods: {
    setCategory(categoryId) {
      this.$store.commit('setCategory', categoryId);
    },
  },
}
</script>
