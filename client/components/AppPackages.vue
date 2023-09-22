<template>
  <v-container class="packages pa-16 align-center">
    <v-title class="block-title"> Выберите нужный пакет</v-title>
    <v-row>
      <v-col cols="4" v-for="pack in packList" :key="pack.id">
        <PackageCard :pack="pack" />
      </v-col>

    </v-row>

  </v-container>
</template>

<script setup lang="ts">
  import { PackagesInfo } from 'models/teach_info';

  const { $api } = useNuxtApp()
  const packList = ref<PackagesInfo[]>([])
  const getPacks = async () => {
    packList.value = await $api<PackagesInfo[]>('contentapp/packages/')
  }
  getPacks()

</script>