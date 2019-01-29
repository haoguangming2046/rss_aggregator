<template lang="pug">
nav.navbar.navbar-expand-lg.navbar-light.bg-light
  a.navbar-brand(href='#')
    img(src="/static/logo.png" height="30" width="30")
  button.navbar-toggler(type='button' data-toggle='collapse' data-target='#navbarSupportedContent' aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation')
    span.navbar-toggler-icon
  #navbarSupportedContent.collapse.navbar-collapse
    ul.navbar-nav.mr-auto
      li.nav-item.active
        a.nav-link(href='#')
          | Home
          span.sr-only (current)
      li.nav-item
        a.nav-link(href='#') Link
    form.form-inline.my-2.my-lg-0
      button.btn.btn-outline-success.my-2.my-sm-0 Search
</template>

<script>
export default {}
</script>