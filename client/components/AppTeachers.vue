<template>
  <v-container class="teachers pa-16">
    <v-title class="block-title">Профессиональные тренеры</v-title>
    <v-carousel hide-delimiters height="600" class="teachers-carousel mt-15">
      <v-carousel-item cols="4" v-for="teacher in teacherList" :key="teacher.id">
        <TeacherCard :teacher="teacher" />
      </v-carousel-item>
    </v-carousel>
  </v-container>
</template>

<script setup lang="ts">
  import { Teachers } from 'models/teach_info';
  
  const { $api } = useNuxtApp()
  const teacherList = ref<Teachers[]>([])
  const getTrainers = async () => {
    teacherList.value = await $api<Teachers[]>('contentapp/teachers/')
  }
  getTrainers()

</script> 