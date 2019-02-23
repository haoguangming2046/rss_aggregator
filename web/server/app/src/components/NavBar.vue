<template lang="pug">
// Component to Render Nav Bar
nav.navbar.navbar-expand-lg
  a.navbar-brand.my-0.py-0(href='#')
    img(src="../../static/images/logo.png" height="30" width="30")
  button.navbar-toggler(type='button' data-toggle='collapse' data-target='#navbarSupportedContent' aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation')
    span.navbar-toggler-icon
  div#navbarSupportedContent.collapse.navbar-collapse
    ul.navbar-nav.mr-auto.pt-2
      li.nav-item.active
        a.c-navbar-text(href='#')
          h5 Home
    form.form-inline.my-2.my-lg-0
      a.my-2.my-sm-0.c-navbar-text(href='/settings' v-if='getCommonData.isAdmin')
        h5 Admin
      .input-group
      .nav-item.dropdown
        h5.text-right
          a#navbarDropdown.nav-link.dropdown-toggle.c-navbar-text(href='#' role='button' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false')
            | {{getCommonData.userName}}
          .dropdown-menu.text-right(aria-labelledby='navbarDropdown')
            a.dropdown-item.text-right(href='/logout') Logout
</template>

<script>
export default {
  computed: {
    getCommonData() {
      return this.$store.state.commonData;
    }
  }
}
</script>
