<template>
  <v-card
    variant="outlined"
    :border="0"
    class="teacher-card d-flex flex-column "
  >
    <v-img
      :width="360"
      :height="500"
      :src="teacher?.photo"
      class="teacher-card__img p-0"
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
    <div class="teacher-card__content mt-4 ms-1">
      <p class="teacher-card__title text-h5 font-weight-bold">
        {{ teacher?.firstName }} {{ teacher?.lastName }}
      </p>
      <p class="teacher-card__text text-subtitle-1 font-weight-medium my-4 ">
        {{ teacher?.position }}
      </p>
      <VDialog>
        <template v-slot:activator="{ props }">
          <VBtn
            class="teacher-card__more text-capitalize ps-0 text-subtitle-1 font-weight-medium"
            color="#D52027"
            v-bind="props"
            variant="text"
          >Подробнее </VBtn>
        </template>
      </VDialog>
    </div>
  </v-card>
</template>

<script setup lang="ts">
import { Teachers } from 'models/teach_info'
import { PropType } from 'vue'
// import { VDialog } from 'vuetify/lib/components'


defineProps({
  teacher: Object as PropType<Teachers>
})
</script>