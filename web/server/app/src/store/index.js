import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const state = {
  categoryId: -1,
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
    if (payload === -1) {
      state.currentFeeds = state.feeds;
    } else if (payload === 0) {
      state.currentFeeds = state.feeds.filter(feed => feed.isStarred === true);
    } else {
      state.currentFeeds = state.feeds.filter(feed => feed.source === payload );
    }
  },
  updateCategoryCount (state, payload) {
    state.categoryCount = payload;
  },
  getFeeds() {
    const response = [
      {id: 1, title: 'First Article', content: 'First Article Content ...', source: 1, isStarred: true, comments: [{name: 'PK', content: 'First Arcticle Comment', time: 'Today 12:10'}] },
      {id: 2, title: 'Second Article', content: 'Second Article Content ...', source: 2, isStarred: true, comments: [{name: 'PK', content:  'Second Article Comment', time: 'Today 12:10'}] },
      {id: 3, title: 'Third Article', content: 'Third Article Content ...', source: 2, isStarred: false, comments: [{name: 'PK', content: '## Third Article Heading', time: 'Today 12:10'}, {name: 'PK', content: '```Third Article Code Block```', time: 'Today 12:10'}] },
    ];
    state.feeds = response;
    state.currentFeeds = response;
    state.feeds.forEach(feed => {
      if (feed.source in state.categoryFeedCount) {
        Vue.set(state.categoryFeedCount, feed.source, state.categoryFeedCount[feed.source] + 1);
      } else {
        Vue.set(state.categoryFeedCount, feed.source, 1);
      }
    });
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
