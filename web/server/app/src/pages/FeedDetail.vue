<template lang="pug">
// Component to Render Feed Detail View for Feed Page
div.container-fluid.my-3
  div.row
    div.col-sm-2
      left-side-bar(v-if='getCommonData.isLoggedIn' :showFeedNumbers='false')
    div.col-sm-7
      div.mb-4.c-card.c-slide-animated
        feed(:feed='dataFeed', :isFeedList='false')
        div.row
          div.col-sm-9.offset-sm-3
            h6.c-navbar-text Links:
        template(v-for='(linkKey, linkValue) in dataFeed.links')
          div.row.pt-2
            div.col-sm-9.offset-sm-3
              a(:href='linkValue' target="_blank") {{linkValue}}
        div.row.pt-2
          div.col-sm-3.ml-2.mt-5
            button.btn.btn-primary(v-if='getCommonData.isAdmin' type='button' data-toggle='modal' data-target='#modal') Source Details
          template(v-if='getCommonData.isLoggedIn')
            div.col-sm-8.mt-5
              form
                div.row.form-group
                  div.col-sm-9
                    textarea.form-control(type='text' rows="1" placeholder='Say something in markdown !', v-model='dataFeed.commentText')
                  div.col-sm-3
                    button.btn.btn-primary(@click='writeComment()' type="button") Comment
            div.col-sm-9.offset-sm-3.p-2
              template(v-for='comment in dataFeed.commentData')
                div.mt-2.v-border-custom
                  div.ml-2
                    h5
                      | {{comment.user.username}}
                      span.h6.ml-2.text-muted {{comment.addedOn.substring(0, 19)}}
                    h6.font-italic(v-html='compiledMarkup(comment.text)')
    div#modal.modal.fade(tabindex='-1' role='dialog' aria-labelledby='modalLabel' aria-hidden='true')
      .modal-dialog(role='document')
        .modal-content
          .modal-header
            h5.modal-title Source Feed Details
            button.close(type='button' data-dismiss='modal' aria-label='Close')
              span(aria-hidden='true') &times;
          .modal-body {{dataFeed.details}}
          .modal-footer
            button.btn.btn-secondary(type='button' data-dismiss='modal') Close
    div.col-sm-3
      right-side-bar
</template>

<script>
import Vue from "vue";
import marked from 'marked';

import helpers from '../helpers/index';
import LeftSideBar from '../components/LeftSideBar';
import RightSideBar from '../components/RightSideBar';
import Feed from '../components/Feed';

export default {
  components: {
    'left-side-bar': LeftSideBar,
    'right-side-bar': RightSideBar,
    'feed': Feed,
  },
  mixins: [helpers],
  props: {
    commonData: {
      type: Object,
      default: () => {},
    },
    feed: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      dataFeed: this.feed,
    }
  },
  created() {
    this.$store.commit('setCommonData', this.commonData);
    Vue.set(this.dataFeed, "commentText", '');
    if (!this.dataFeed.hasOwnProperty("commentData")) {
      Vue.set(this.dataFeed, "commentData", []);
    }
  },
  computed: {
    getCommonData() {
      return this.$store.state.commonData;
    }
  },
  methods: {
    bookmark() {
      this.$store.commit('bookmarkFeed', this.dataFeed);
    },
    writeComment(feed) {
      if (!this.feed.commentText.trim()) {
        this.createNotification({message: "Please enter some text.", context: "alert-info"});
      } else {
        this.$axios.post('/api/user/comment/create', {
          data: {
            feed: this.dataFeed,
          },
        }).then(response => {
          this.dataFeed.commentData.push({user: {username: this.$store.state.commonData.userName}, text:this.dataFeed.commentText, addedOn: 'Now'});
          this.dataFeed.commentText = "";
          helpers.methods.createNotification({message: "Comment Added :)", context: "alert-success"});
        }).catch(error =>{
          helpers.methods.createNotification({message: "Could not add comment :("});
          console.log(error);
        });
      }
    },
    compiledMarkup(commentText) {
      return marked(commentText, {sanitize: true});
    },
  }
}
</script>

<style lang="scss" scoped>
@import "../../static/css/_variables.scss";
.v-border-custom {
  border-color: $color-muted;
  border-left-width: thick;
  border-left-style: solid;
}
.modal-dialog, .modal-content {
  height: 80%;
}
.modal-body {
  max-height: calc(100% - 120px);
  overflow-y: auto;
}
</style>
