<template>
  <div
    class="packages default-spacing mt-16"
    id="packages"
  >
    <VContainer class="packages-block pa-4 pa-lg-16 align-center">
      <p class="block-title text-center text-lg-start text-h5 text-md-h4 text-lg-h3 font-weight-bold"> Выберите
        нужный пакет</p>
      <VRow class="mt-4 mt-lg-8">
        <VCol
          cols="12"
          sm="6"
          md="4"
          v-for="pack in packList"
          :key="pack.id"
          class="d-flex justify-center mt-4"
        >
          <PackageCard :pack="pack" />
        </VCol>
      </VRow>
    </VContainer>
  </div>
</template>

<script setup lang="ts">
import { PackagesInfo } from 'models/pack_info'

const { $api } = useNuxtApp()
const packList = ref<PackagesInfo[]>([])
const getPacks = async () => {
  packList.value = await $api<PackagesInfo[]>('contentapp/packages/')
}
getPacks()

</script>