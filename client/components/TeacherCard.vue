<template>
  <v-card class="d-flex flex-column">
    <v-img
      :width="300"
      :height="440"
      :src="teacher?.photo"
      class="teacher-card__img px-3"
    >
      <template v-slot:placeholder>
        <div class="d-flex align-center justify-center">
          <v-progress-circular
            color="grey-lighten-4"
            indeterminate
          ></v-progress-circular>
        </div>
      </template>
    </v-img>
    <div class="teach-card__content">
      <p class="teach-card__title">
        {{ teacher?.firstName }} {{ teacher?.lastName }}
      </p>
      <p class="teach-card__text mt-3">
        {{ teacher?.position }}
      </p>
      <a
        class="teach-card__more mt-3"
        href=""
      >Подробнее</a>
    </div>
  </v-card>
</template>

<script setup lang="ts">
import { Teachers } from 'models/teach_info'
import { PropType } from 'vue'


defineProps({
  teacher: Object as PropType<Teachers>
})
</script>