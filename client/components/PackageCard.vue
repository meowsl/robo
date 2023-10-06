<template>
  <VCard
    class="package-card d-flex align-center justify-center mt-16"
    max-width="360"
    max-height="500"
  >
    <div class="package-card__content d-flex flex-column justify-center align-center text-center h-auto">
      <p class="package-card__title">
        {{ pack?.name }}
      </p>
      <p class="package-card__price pt-16">
        {{ pack?.price }} ₽
      </p>
      <VCardText class="package-card__text text-subtitle-1 mt-10 mx-10">
        {{ pack?.descript }}
      </VCardText>
      <VCardActions>
        <NuxtLink to="#feedback">
          <VBtn
            variant="total"
            size="small"
            class="package-card__button pa-1 ma-5 rounded"
          >
            <p class="text-button">Оставить заявку</p>
          </VBtn>
        </NuxtLink>
      </VCardActions>

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