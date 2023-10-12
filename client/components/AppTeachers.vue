<template>
  <div
    class="teachers default-spacing mt-12"
    id="teachers"
  >
    <VContainer class="teachers-block text-center text-lg-start text-center text-lg-start pa-4 pa-lg-16 ">
      <p class="block-title text-h5 text-md-h4 text-lg-h3 font-weight-bold ">Профессиональные тренеры</p>
    </VContainer>
  </div>
  <VContainer class="d-flex justify-center align-center pa-0 pa-md-4">
    <VSlideGroup
      height="600"
      class="teachers-carousel mx-2 px-2 mx-xl-16 px-xl-16"
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