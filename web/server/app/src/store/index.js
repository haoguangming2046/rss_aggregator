import Vue from 'vue';
import Vuex from 'vuex';

import helpers from '../helpers/index';
import axios from '../globals';

Vue.use(Vuex);

const state = {
  feeds: [],
  currentFeeds: [],
  categoryFeedCount: {},
  commonData: {},
};

const mutations = {
  setCommonData (state, payload) {
    Vue.set(state.commonData, 'userName', payload.user_name);
    Vue.set(state.commonData, 'userId', payload.user_id);
    Vue.set(state.commonData, 'isLoggedIn', payload.is_logged_in);
    Vue.set(state.commonData, 'isAdmin', payload.is_admin);
  },
  setCategory (state, payload) {
    if (payload == -1) {
      state.currentFeeds = state.feeds;
    } else if (payload == 0) {
      state.currentFeeds = state.feeds.filter(feed => feed.isStarred === true);
    } else {
      state.currentFeeds = state.feeds.filter(feed => feed.source.id == payload );
    }
  },
  updateCategoryCount (state, payload) {
    state.categoryCount = payload;
  },
  getFeeds() {
    axios.get('/api/feeds').then(response => {
      if ("data" in response.data) {
        state.feeds = response.data.data;
        state.feeds.forEach(feed => {
          Vue.set(feed, "isStarred", false);
          Vue.set(feed, "comments", []);
          if (feed.source.id in state.categoryFeedCount) {
            Vue.set(state.categoryFeedCount, feed.source.id, state.categoryFeedCount[feed.source.id] + 1);
          } else {
            Vue.set(state.categoryFeedCount, feed.source.id, 1);
          }
        });
        state.currentFeeds = state.feeds;
        axios.get('/api/user/bookmarks').then(response => {
          if ("data" in response.data) {
            response.data.data.forEach(bookmark => {
              let feed = state.feeds.find(feed => feed.id == bookmark.id);
              if (feed) {
                feed.isStarred = true;
              }
            });
          }
        }).catch(error => {
          helpers.methods.createNotification({message: "Could not get bookmarks :("});
          console.log(error);
        });
      }
    }).catch(error => {
      helpers.methods.createNotification({message: "Could not get feeds :("});
      console.log(error);
    });
  },
  bookmarkFeed(state, payload) {
    let feed = state.feeds.find(feed => feed.id == payload.id);
    axios.post('/api/user/bookmark/create', {
      data: {
        feed: payload,
      },
    }).then(() => {
      helpers.methods.createNotification({message: "Bookmark Added :)", context: "alert-success"});
    }).catch(error => {
      if (feed) feed.isStarred = false;
      helpers.methods.createNotification({message: "Could not add bookmark :("});
      console.log(error);
    });
    if (feed) feed.isStarred = true;
  },
};

const getters = {
  totalFeedCount: state => {
    return state.feeds.length;
  },
  favouriteFeedCount: state => {
    return state.feeds.filter(feed => feed.isStarred === true).length;
  },
};

export default new Vuex.Store({
  state,
  mutations,
  getters,
});
