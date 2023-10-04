<template>
  <div class="request-block">
    <VImg
      :src="backFoot"
      class="request-block__img"
    />
    <VContainer class="default-spacing  px-16 py-6">
      <VRow class="text-white text-left py-16 ps-14">
        <VCol cols="7">
          <p class="request-block__text mb-3">Запишитесь на курс со скидкой 10%</p>
          Акция действительна до 10 марта 2022 года
        </VCol>
        <VCol cols="5">
          <VForm
            @submit.prevent
            class="form-input"
          >
            <VTextField
              v-model="firstName"
              :rules="nameRules"
              label="Имя"
              class="form-input"
            ></VTextField>
            <VTextField
              model="number"
              :rules="rules"
              label="Телефон"
            ></VTextField>
            <VTextField
              v-model="EMail"
              :rules="rules"
              label="E-mail"
            ></VTextField>
            <VBtn
              type="submit"
              block
              variant="tonal"
              rounded="xs"
              height="64"
              class="form-input__btn text-none"
            >
              <p class="form-input__btn__text text-white text-subtitle-1">Оформить заявку</p>
            </VBtn>
          </VForm>
        </VCol>
      </VRow>

    </VContainer>
  </div>
</template>


<script setup lang="ts">
import { email } from '@vuelidate/validators'
import backFoot from 'images/foot-back.png'
</script>