<template>
  <VAppBar
    class="app-bar"
    height="prominent"
    flat="false"
    text-color="#fff"
  >
    <div class="app-bar__content w-100 py-2">
      <VContainer class="text-center text-white text-subtitle-2 d-flex justify-space-between pa-4">
        <VRow class="px-16">
          <VCol class="text-start font-weight-bold text-h4 ps-0">
            <NuxtLink
              class="app-bar__item"
              to="/"
            >
              ROBO.SCHOOL
            </NuxtLink>
          </VCol>
          <VCol class="d-flex align-center justify-space-evenly text-h6">
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
          <VCol class="text-end pe-0 font-weight-bold text-h4">
            <NuxtLink
              class="app-bar__item "
              to="/"
            >+7 800 000 11 22</NuxtLink>
          </VCol>
        </VRow>
      </VContainer>
    </div>
  </VAppBar>
</template>

<script setup lang="ts"></script>