<template>
  <VAppBar
    class="app-bar"
    height="prominent"
    flat="false"
    text-color="#fff"
  >
    <div
      class="app-bar__content w-100 py-2 d-flex justify-space-between align-center text-center text-white text-subtitle-2 pa-4 mx-0 mx-md-4 my-0 my-md-4"
    >
      <v-dialog
        v-model="dialog"
        fullscreen
        :scrim="false"
        transition="dialog-top-transition"
        class="d-inline d-md-none"
      >
        <template v-slot:activator="{ props }">
          <NuxtLink
            class="app-bar__item d-inline d-md-none text-h6 text-sm-h5 font-weight-bold"
            to="/"
          >
            ROBO.SCHOOL
          </NuxtLink>
          <div class="icons">
            <VBtn
              variant="tonal"
              class="d-inline d-md-none me-4"
              min-width="44"
              min-height="44"
              icon="true"
            >
              <VImg
                :src="phoneImg"
                max-width="30"
              >
              </VImg>
            </VBtn>
            <VBtn
              variant="tonal"
              class="d-inline d-md-none"
              v-bind="props"
              min-width="44"
              min-height="44"
              icon="true"
            >
              <VImg
                :src="menuImg"
                max-width="30"
              >
              </VImg>
            </VBtn>
          </div>
        </template>
        <VCard class="app-bar__modal-menu">
          <VRow>
            <VCol
              cols="12"
              class="d-flex justify-end py-5 px-7 h-0"
            >
              <VBtn
                variant="tonal"
                class="d-inline d-md-none"
                v-bind="props"
                min-width="44"
                min-height="44"
                icon="true"
                @click="dialog = false"
              >
                <VImg
                  :src="closeMenu"
                  max-width="30"
                >
                </VImg>
              </VBtn>
            </VCol>
            <VCol cols="12">
              <VContainer class="d-flex text-h4 font-weight-bold text-white text-center flex-column justify-center">
                <NuxtLink
                  class="app-bar__item"
                  to="#descriptions"
                >
                  О школе
                </NuxtLink>
                <NuxtLink
                  class="app-bar__item py-8"
                  to="#teachers"
                >
                  Тренеры
                </NuxtLink>
                <NuxtLink
                  class="app-bar__item"
                  to="#packages"
                >
                  Стоимость
                </NuxtLink>
              </VContainer>
            </VCol>
          </VRow>

        </VCard>
      </v-dialog>

      <VRow class="px-0 px-xl-16 d-none d-md-flex">
        <VCol class="text-start font-weight-bold text-h6 text-md-h5 text-lg-h4 ps-0">
          <NuxtLink
            class="app-bar__item"
            to="/"
          >
            ROBO.SCHOOL
          </NuxtLink>
        </VCol>
        <VCol
          class="d-flex align-center justify-space-between justify-lg-space-evenly text-subtitle-2 text-md-subtitle-1 text-lg-h6"
        >
          <NuxtLink
            class="app-bar__item"
            to="#descriptions"
          >
            О школе
          </NuxtLink>
          <NuxtLink
            class="app-bar__item"
            to="#teachers"
          >
            Тренеры
          </NuxtLink>
          <NuxtLink
            class="app-bar__item"
            to="#packages"
          >
            Стоимость
          </NuxtLink>
        </VCol>
        <VCol class="text-end pe-0 font-weight-bold text-h6 text-md-h5 text-lg-h4">
          <NuxtLink
            class="app-bar__item "
            to="/"
          >+7 800 000 11 22</NuxtLink>
        </VCol>
      </VRow>
    </div>
  </VAppBar>
</template>

<script setup lang="ts">
import menuImg from 'images/icon-menu.svg'
import closeMenu from 'images/icon_close_menu.svg'
import phoneImg from 'images/Call.svg'

const dialog = ref(false)
</script>