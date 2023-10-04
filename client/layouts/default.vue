<template>
  <VLayout>
    <Header />
    <VMain class="">
      <slot />
    </VMain>

  </VLayout>
  <Footer />
</template>

<script setup lang="ts">
// import rsueLogo from 'images/rsue_logo.svg'
import Footer from '../layouts/Footer.vue'
import Header from '../layouts/Header.vue'
</script>
