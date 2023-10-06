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
      <p class="teacher-card__position text-subtitle-1 font-weight-medium my-4 ">
        {{ teacher?.position }}
      </p>
      <VBtn
        class="teacher-card__more text-capitalize ps-0 text-subtitle-1 font-weight-medium"
        color="#D52027"
        v-bind="props"
        variant="text"
        @click="dialog = true"
      >Подробнее
      </VBtn>
      <VDialog
        v-model="dialog"
        width="auto"
      >
        <VCard
          width="940"
          height="664"
          class="teacher-modal pa-10 d-flex flex-column"
        >
          <VRow>
            <VCol
              cols="12"
              class="d-flex flex-row"
            >
              <VImg
                :max-width="160"
                :max-height="222"
                :src="teacher?.photo"
              />
              <div class="teacher-modal__personal flex-column ms-10 mt-2">
                <p class="teacher-modal__title text-h5 font-weight-bold">
                  {{ teacher?.firstName }} {{ teacher?.lastName }}
                </p>
                <p class="teacher-modal__position text-subtitle-1 font-weight-medium my-4 ">
                  {{ teacher?.position }}
                </p>
                <VBtn
                  variant="tonal"
                  icon="true"
                  width="30"
                  height="30"
                  class="teacher-modal__contacts"
                >
                  <VImg
                    :src="facebookIcon"
                    width="17"
                    height="17"
                  ></VImg>
                </VBtn>
                <VBtn
                  variant="tonal"
                  icon="true"
                  width="30"
                  height="30"
                  class="teacher-modal__contacts ms-2"
                >
                  <VImg
                    :src="instIcon"
                    width="17"
                    height="17"
                  ></VImg>
                </VBtn>
              </div>
              <v-spacer />
              <VBtn
                color="primary"
                variant="text"
                @click="dialog = false"
                class="mt-2"
              >
                <p class="text-capitalize text-medium-emphasis">Закрыть</p>
              </VBtn>

            </VCol>
            <VCol
              cols="12"
              class="teacher-modal__info d-flex flex-column"
            >
              <p class="teacher-modal__info__title font-weight-regular text-h6">Информация</p>
              <div class="teacher-modal__underline my-4"></div>
              <div class="teacher-modal__info__content text-h6">
                <p>{{ teacher?.dateStart }} — {{ teacher?.dateEnd }}</p>
                <p>{{ teacher?.studyPlace }}</p>
                <p>Факультет: {{ teacher?.studyFacult }}</p>
                <p>Специальность: {{ teacher?.studySpec }}</p>
                <p>Форма обучения: {{ teacher?.studyForm }}</p>
              </div>
            </VCol>
          </VRow>

        </VCard>
      </VDialog>
    </div>
  </v-card>
</template>

<script setup lang="ts">
import facebookIcon from 'images/icon-facebook.svg'
import instIcon from 'images/icon-inst.svg'
import { Teachers } from 'models/teach_info'
import { PropType } from 'vue'
const dialog = ref(false)

defineProps({
  teacher: Object as PropType<Teachers>
})
</script>