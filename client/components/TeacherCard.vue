<template>
  <VCard
    variant="outlined"
    :border="0"
    class="teacher-card d-flex flex-column "
  >
    <VImg
      :width="360"
      :height="500"
      :src="teacher?.photo"
      class="teacher-card__img p-0"
    >
      <template v-slot:placeholder>
        <div class="d-flex align-center justify-center">
          <VProgressCircular
            color="grey-lighten-4"
            indeterminate
          ></VProgressCircular>
        </div>
      </template>
    </VImg>
    <div class="teacher-card__content mt-4 ms-1">
      <p class="teacher-card__title text-h6 text-md-h5 font-weight-bold">
        {{ teacher?.firstName }} {{ teacher?.lastName }}
      </p>
      <p class="teacher-card__position text-subtitle-2 text-md-subtitle-1 font-weight-medium my-4 ">
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
          max-width="940"
          max-height="664"
          class="teacher-modal pa-8 pa-md-10 d-flex flex-column"
        >
          <VRow>
            <VCol
              cols="12"
              class="pa-0 d-flex justify-end"
            >
              <VBtn
                variant="text"
                max-height="30"
                max-width="30"
                icon="true"
                @click="dialog = false"
                class="d-flex d-sm-none"
              >
                <VImg
                  :src="iconClose"
                  width="15"
                  height="15"
                >
                </VImg>

              </VBtn>
            </VCol>
            <VCol
              cols="12"
              class="d-flex flex-row pa-0 pa-md-auto align-start"
            >
              <VImg
                max-width="160"
                max-height="222"
                min-height="100"
                min-width="72"
                :src="teacher?.photo"
              />
              <div class="teacher-modal__personal flex-column ms-4 ms-md-10">
                <p class="teacher-modal__title text-subtitle-1 text-md-h6 font-weight-bold">
                  {{ teacher?.firstName }} {{ teacher?.lastName }}
                </p>
                <p class="teacher-modal__position text-caption text-md-subtitle-1 font-weight-medium my-1 my-md-4 ">
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
                class="mt-2 d-none d-sm-inline"
              >
                <p class="text-capitalize text-medium-emphasis">Закрыть</p>
              </VBtn>

            </VCol>
            <VCol
              cols="12"
              class="teacher-modal__info d-flex flex-column"
            >
              <p class="teacher-modal__info__title font-weight-regular text-h6">Информация</p>
              <div class="teacher-modal__underline my-4 d-none d-md-inline"></div>
              <div class="teacher-modal__info__content mt-4 mt-md-0 text-subtitle-2 text-md-h6">
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
  </VCard>
</template>

<script setup lang="ts">
import facebookIcon from 'images/icon-facebook.svg'
import instIcon from 'images/icon-inst.svg'
import iconClose from 'images/icon_close_modal.svg'
import { Teachers } from 'models/teach_info'
import { PropType } from 'vue'
const dialog = ref(false)

defineProps({
  teacher: Object as PropType<Teachers>
})
</script>