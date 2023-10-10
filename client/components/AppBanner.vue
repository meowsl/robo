<template>
  <div class="banner d-flex align-end pt-16 mt-0 mt-md-10 mt-lg-2">
    <VContainer class="banner-block pb-3 px-0">
      <VRow class="text-white d-flex flex-column flex-lg-row">
        <VCol class="d-flex align-center justify-center px-6 px-sm-16 px-lg-0">
          <div class="test-content d-flex flex-column text-center text-lg-start">
            <p class="text-h4 text-md-h3 text-lg-h2 font-weight-bold">ROBO SCHOOL</p>
            <p class="my-5 my-lg-12 text-white text-subtitle-1 text-md-h6">Курсы повышения квалификации по робототехнике
              для
              педагогов начальной школы</p>
            <VBtn
              variant="tonal"
              size="large"
              class="banner-block__btn d-none d-lg-flex text-white mx-auto mx-lg-0"
              :height="80"
              :width="auto"
              max-height="80"
              max-width="260"
            >
              <p class="banner-block__btn__text text-white text-subtitle-1">Записаться
                на курс</p>
            </VBtn>
          </div>
        </VCol>
        <VCol class="pb-6 pb-lg-0 d-flex justify-center px-10 px-lg-0 flex-column">
          <VImg
            class="banner-block__img align-end mx-16 mx-lg-0"
            :src="bannerImage"
            :width="auto"
            :height="auto"
            max-width="700"
            max-height="800"
          />
          <VBtn
            variant="tonal"
            block
            size="large"
            class="banner-block__btn d-flex d-lg-none text-white mx-auto mx-lg-0"
            :height="80"
            :width="auto"
            max-height="80"
            max-width="260"
          >
            <p class="banner-block__btn__text  text-white text-subtitle-1">Записаться
              на курс</p>
          </VBtn>
        </VCol>
      </VRow>
    </VContainer>
  </div>
</template>



<script setup lang="ts">
import bannerImage from 'images/banner-image.svg'
</script>

