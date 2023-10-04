<template>
  <div class="banner default-spacing d-flex align-end pt-16">
    <VContainer class="banner-block d-flex flex-row pb-3">
      <VRow class="d-flex text-white">
        <VCol
          cols="6"
          class="pb-0 d-flex flex-row justify-center align-center"
        >
          <div class="test-content d-flex flex-column">
            <p class="text-h2 font-weight-bold">ROBO SCHOOL</p>
            <p class="my-12 text-white text-h6">Курсы повышения квалификации по робототехнике для
              педагогов начальной школы</p>
            <VBtn
              variant="tonal"
              size="large"
              class="banner-block__btn text-white "
              height="80"
              width="260"
            >
              <p class="banner-block__btn__text text-white text-subtitle-1">Записаться
                на курс</p>

            </VBtn>
          </div>
        </VCol>
        <VCol
          cols="6"
          class="pb-0"
        >
          <VImg
            class="banner-block__img align-end"
            :src="bannerImage"
            width="auto"
            height="auto"
            max-width="700"
            max-height="800"
          />
        </VCol>
      </VRow>
    </VContainer>
  </div>
</template>



<script setup lang="ts">
import bannerImage from 'images/banner-image.svg'
</script>

