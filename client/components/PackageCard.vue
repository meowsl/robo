<template>
  <VCard
    class="package-card d-flex align-center justify-center mt-4"
    variant="outlined"
    width="360"
    max-width="360"
    height="460"
  >
    <div
      class="package-card__content  text-center d-flex flex-column justify-space-between pa-8 align-center h-100 w-auto"
    >
      <p class="package-card__title text-h4">
        {{ pack?.name }}
      </p>
      <p class="package-card__price text-h3 pt-8 pt-md-16">
        {{ pack?.price }} ₽
      </p>
      <p class="package-card__text text-subtitle-1 my-10 mx-0">
        {{ pack?.descript }}
      </p>
      <NuxtLink to="#feedback">
        <VBtn
          size="small"
          width="auto"
          height="auto"
          class="package-card__button py-4 px-14 px-lg-16 rounded"
        >
          <p class="text-button text-capitalize text-white">Оставить заявку</p>
        </VBtn>
      </NuxtLink>

    </div>
  </VCard>
</template>

<script setup lang="ts">
import { PackagesInfo } from 'models/pack_info'
import { PropType } from 'vue'

defineProps({
  pack: Object as PropType<PackagesInfo>
})
</script>