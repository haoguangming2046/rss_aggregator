<template lang="pug">
// Component to Render Settings View for Settings Page
div.container-fluid.my-3
  div.row
    div.col-sm-2
      left-side-bar(:showFeedNumbers='false')
    div.col-sm-7
      div.mb-4.p-2.c-card.c-slide-animated
        div.row.mx-3
          div.col-sm-12
            h5.text-primary Add New Feed Source
          div.col-sm-6
            input.form-control(v-model='sourceLink' type="text" name="link" placeholder="Source Link ...")
          div.col-sm-3
            button.btn.btn-primary(type="button" @click='addNewSource') Add
      template(v-for='source in feedSourcesList.data')
        div
          div.mb-4.p-2.c-card.c-slide-animated
            div.row
              div.col-sm-3.c-img-div
                a
                  img.img-fluid(:src='source.logoLink' onerror="this.src='../../static/images/logo.png';")
              div.col-sm-6
                h4 {{source.name}}
                h5
                  a(:href='source.link' target="_blank") {{source.link}}
                h6 Added on {{source.lastActiveOn.substring(0, 19)}}
                h6
                  button.btn.btn-primary(type='button' data-toggle='modal' data-target='#modal') Source Details
              div.col-sm-3.c-img-div
                a.v-cursor-pointer(@click='changeSourceStatus(source)' )
                  img.img-fluid(src="../../static/images/logo.png" :class='source.status ? "v-running-img": "" ')
        div#modal.modal.fade(tabindex='-1' role='dialog' aria-labelledby='modalLabel' aria-hidden='true')
          .modal-dialog(role='document')
            .modal-content
              .modal-header
                h5.modal-title Source Feed Details
                button.close(type='button' data-dismiss='modal' aria-label='Close')
                  span(aria-hidden='true') &times;
              .modal-body {{source.details}}
              .modal-footer
                button.btn.btn-secondary(type='button' data-dismiss='modal') Close
    div.col-sm-3
      right-side-bar
</template>

<script>
import LeftSideBar from '../components/LeftSideBar';
import RightSideBar from '../components/RightSideBar';
import FeedList from '../components/FeedList';
import helpers from '../helpers/index';

export default {
  components: {
    'left-side-bar': LeftSideBar,
    'right-side-bar': RightSideBar,
  },
  mixins: [helpers],
  props: {
    commonData: {
      type: Object,
      default: '{}',
    },
    feedSources: {
      type: Object,
      default: '{}',
    }
  },
  data() {
    return {
      sourceLink: '',
      feedSourcesList: this.feedSources,
    }
  },
  created() {
    this.$store.commit('setCommonData', this.commonData);
  },
  methods: {
    changeSourceStatus(source) {
      this.$axios.post(`api/feed/source/${source.id}/update/`, {
        data: {
          source: source,
        }
      }).then(response => {
        if ("opStatus" in response.data) {
          if (response.data.opStatus == "SUCCESS") {
            source.status = !source.status;
            this.createNotification({message: 'Updated Source :)', context: 'alert-success'});
          } else {
            this.createNotification({message: 'Could not update feed source :('});
          }
        } else {
          this.createNotification({message: 'Could not update feed source :('});
        }
      }).catch(error => {
        this.createNotification({message: 'Could not update feed source :('});
        console.log(error);
      });
    },
    addNewSource() {
      this.$axios.post('api/feed/source/create', {
        data: {
          link: this.sourceLink,
        }
      }).then(response => {
        if (response.data.opStatus == "SUCCESS" ){
          this.createNotification({message: 'Added New Source :)', context: 'alert-success'});
        } else {
          response.data.details.errors.data.forEach(errorMsg => {
            this.createNotification({message: errorMsg})
          });
        }
      }).catch(error => {
        this.createNotification({message: 'Could not add new Source :('});
        console.log(error);
      });
    }
  }
}
</script>

<style lang="scss" scoped>
.modal-dialog, .modal-content {
  height: 80%;
}
.modal-body {
  max-height: calc(100% - 120px);
  overflow-y: auto;
}
.v-cursor-pointer {
  cursor: pointer;
}
.v-running-img {
    -webkit-animation:spin 4s linear infinite;
    -moz-animation:spin 4s linear infinite;
    animation:spin 4s linear infinite;
}
@-moz-keyframes spin { 100% { -moz-transform: rotate(360deg); } }
@-webkit-keyframes spin { 100% { -webkit-transform: rotate(360deg); } }
@keyframes spin { 100% { -webkit-transform: rotate(360deg); transform:rotate(360deg); } }
</style>
