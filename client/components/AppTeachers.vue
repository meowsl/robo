<template>
  <div class="teachers default-spacing">
    <VContainer class="teachers-block pa-16">
      <p class="block-title">Профессиональные тренеры</p>
      <VCarousel
        hide-delimiters
        height="600"
        cycle="true"
        hide-delimiter-background="true"
        class="teachers-carousel mt-15"
      >
        <VCarouselItem
          cols="4"
          v-for="teacher in teacherList"
          :key="teacher.id"
        >
          <TeacherCard :teacher="teacher" />
        </VCarouselItem>
      </VCarousel>
    </VContainer>
  </div>
</template>

<script setup lang="ts">
import { Teachers } from 'models/teach_info'

const { $api } = useNuxtApp()
const teacherList = ref<Teachers[]>([])
const getTrainers = async () => {
  teacherList.value = await $api<Teachers[]>('contentapp/teachers/')
}
getTrainers()

</script>