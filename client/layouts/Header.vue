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
      <VMenu class="d-inline d-md-none">

        <template v-slot:activator="{ props }">
          <NuxtLink
            class="app-bar__item d-inline d-md-none text-h6 text-sm-h5 font-weight-bold"
            to="/"
          >
            ROBO.SCHOOL
          </NuxtLink>
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
        </template>

        <VList class="">
          <VListItem class="py-0">
            <NuxtLink
              class="app-bar__item-menu text-h6"
              to="/"
            >
              Главная
            </NuxtLink>
          </VListItem>
          <VListItem class="py-0">
            <NuxtLink
              class="app-bar__item-menu text-h6"
              to="/about-page"
            >
              О нас
            </NuxtLink>
          </VListItem>
          <VListItem class="py-0">
            <NuxtLink
              class="app-bar__item-menu text-h6"
              to="/waves-page"
            >
              Направления
            </NuxtLink>
          </VListItem>
          <VListItem class="py-0">
            <NuxtLink
              class="app-bar__item-menu text-h6"
              to="/information-page"
            >
              Полезная информация
            </NuxtLink>
          </VListItem>
          <VListItem class="py-0">
            <NuxtLink
              class="app-bar__item-menu text-h6"
              to="/contacts-page"
            >Контакты</NuxtLink>
          </VListItem>
        </VList>
      </VMenu>
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
</script>