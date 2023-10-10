<template>
  <div
    class="packages default-spacing mt-16"
    id="packages"
  >
    <VContainer class="packages-block pa-4 pa-lg-16 align-center">
      <p class="block-title"> Выберите нужный пакет</p>
      <VRow>
        <VCol
          cols="12"
          sm="6"
          md="4"
          v-for="pack in packList"
          :key="pack.id"
          class="d-flex justify-center"
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