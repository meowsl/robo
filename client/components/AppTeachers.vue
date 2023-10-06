<template>
  <div
    class="teachers default-spacing"
    id="teachers"
  >
    <VContainer class="teachers-block pa-16">
      <p class="block-title">Профессиональные тренеры</p>
    </VContainer>
  </div>
  <VContainer class="d-flex justify-center align-center">
    <VSlideGroup
      height="600"
      class="teachers-carousel mx-16 px-16"
    >
      <VSlideGroupItem
        v-for="teacher in teacherList"
        :key="teacher.id"
      >
        <TeacherCard
          :teacher="teacher"
          class="me-16"
        />
      </VSlideGroupItem>
    </VSlideGroup>
  </VContainer>
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