<template>
  <VCard
    class="package-card d-flex align-center justify-center mt-16 "
    variant="outlined"
    width="auto"
    max-width="360"
    height="460"
  >
    <div class="package-card__content d-flex flex-column justify-space-evenly  align-center text-center h-100">
      <p class="package-card__title text-h4">
        {{ pack?.name }}
      </p>
      <p class="package-card__price text-h3 pt-16">
        {{ pack?.price }} ₽
      </p>
      <p class="package-card__text text-subtitle-1 my-10 mx-10">
        {{ pack?.descript }}
      </p>
      <NuxtLink to="#feedback">
        <VBtn
          variant="total"
          size="small"
          width="auto"
          height="auto"
          class="package-card__button py-4 px-14 ma-5 rounded"
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