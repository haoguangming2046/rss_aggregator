<template lang="pug">
// Component to Render Feed
div
  div.mb-4.p-2.c-card.c-slide-animated
    div.row
      div.col-sm-3
        img.img-fluid.v-img(src='https://priyank.co.uk/img/about-alt.jpg')
      div.col-sm-9
        h4.pt-2 {{feed.title}}
        h5.lead {{feed.content}}
    div.row.pt-2
      div.col-sm-1
        button.btn(@click='bookmark(feed)' :class='feed.isStarred ? "btn-primary" : "btn-secondary" ')
          i.fa.fa-star
      div.col-sm-2
        div(v-if="!feed.showComments")
          button.btn.btn-primary(@click='toggleCommentSection(feed)') Show
            span.ml-2
              i.fa.fa-comments
        div(v-else)
          button.btn.btn-primary(@click='toggleCommentSection(feed)') Hide
            span.ml-2
              i.fa.fa-comments
      div.col-sm-9(v-if="feed.showComments")
        div
          form
            div.row.form-group
              div.col-sm-9
                textarea.form-control(type='text' rows="1" placeholder='Say something in markdown !', v-model='feed.commentText')
              div.col-sm-3
                button.btn.btn-primary(@click='writeComment(feed)' type="button") Comment
        div.col-sm-12
          template(v-for='comment in feed.comments')
            div.mt-2.v-border-custom
              div.ml-2
                h5
                  | {{comment.name}} 
                  span.h6.text-muted {{comment.time}}
                h6.font-italic(v-html='compiledMarkup(comment.content)')
</template>

<script>
import Vue from 'vue';
import marked from 'marked';

import helpers from '../helpers/index';

export default {
  props: {
    feed: {
      type: Object,
      default: {},
    },
  },
  mixins: [helpers],
  created() {
    Vue.set(this.feed, "showComments", false);
    Vue.set(this.feed, "commentText", '');
  },
  computed: {
    getCommonData() {
      return this.$store.state.commonData;
    }
  },
  watch: {
    '$store.state.categoryId': 'updateFeedList',
  },
  methods: {
    toggleCommentSection() {
      this.feed.showComments = !this.feed.showComments;
    },
    bookmark(feed) {
      this.feed.isStarred = !this.feed.isStarred;
    },
    writeComment(feed) {
      if (!this.feed.commentText.trim()) {
        this.createNotification({"message": "Please enter some text."});
      } else {
        this.feed.comments.push({name: this.getCommonData.userName, content: this.feed.commentText});
        this.createNotification({"message": "Replied Successfully", "context": "alert-info"});
        this.feed.commentText = "";
      }
    },
    compiledMarkup(commentText) {
      return marked(commentText, {sanitize: true});
    },
  }
}
</script>

<style lang="scss">
@import "../../static/css/_variables.scss";

.v-img {
  border-radius: 0.5em;
  overflow: hidden;
}

.v-border-custom {
  border-color: $color-muted;
  border-left-width: thick;
  border-left-style: solid;
}
</style>
