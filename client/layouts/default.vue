<template>
  <VLayout>
    <VMain>
      <slot />
    </VMain>
    
  </VLayout>
  <Footer/>
</template>

<script setup lang="ts">
// import rsueLogo from 'images/rsue_logo.svg'
import Footer from '../layouts/Footer.vue'
</script>
