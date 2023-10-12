<template>
  <div
    class="feedback-block mt-16 w-100 h-auto"
    id="feedback"
  >
    <VImg
      :src="backFoot"
      class="feedback-block__img"
      cover
    />
    <VContainer class="default-spacing-feedback">
      <VRow class="text-white text-center text-lg-start d-flex justify-center py-6 py-lg-16">
        <VCol
          lg="7"
          cols="12"
        >
          <p class="feedback-block__text text-h4 font-weight-bold my-4">Запишитесь на курс со скидкой 10%</p>
          Акция действительна до 10 марта 2022 года
        </VCol>
        <VCol
          lg="5"
          cols="12"
        >
          <VForm
            @submit.prevent
            class="form-input"
          >
            <VTextField
              v-model="state.name"
              :error-messages="v$.name.$errors.map(e => e.$message)"
              single-line
              placeholder="Имя"
            ></VTextField>
            <VTextField
              v-model="state.phone"
              :error-messages="v$.phone.$errors.map(e => e.$message)"
              single-line
              placeholder="Телефон"
            ></VTextField>
            <VTextField
              v-model="state.email"
              :error-messages="v$.email.$errors.map(e => e.$message)"
              single-line
              placeholder="E-mail"
            ></VTextField>
            <VBtn
              @click="handleSubmit"
              block
              variant="tonal"
              rounded="xs"
              height="64"
              class="form-input__btn text-none"
            >
              <p class="form-input__btn__text text-white text-subtitle-1">Оформить заявку</p>
            </VBtn>
            <v-snackbar
              v-model="snackbar"
              :timeout="5000"
              location="bottom"
              color="green"
            >
              Заявка оформлена!
            </v-snackbar>
          </VForm>
        </VCol>
      </VRow>

    </VContainer>
  </div>
</template>


<script setup lang="ts">
import backFoot from 'images/foot-back.png'
import { reactive, ref } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { email, required, helpers } from '@vuelidate/validators'
import type { Applications } from 'models/applications'

const { $api } = useNuxtApp()

const snackbar = ref(false)

const initialState = {
  name: '',
  phone: '',
  email: '',
}

const state = reactive({
  ...initialState,
})

const rules = {
  name: { required: helpers.withMessage('Это обязательное поле', required) },
  phone: { required: helpers.withMessage('Это обязательное поле', required) },
  email: { required: helpers.withMessage('Это обязательное поле', required), email: helpers.withMessage('Пожалуйста, введите действительный адрес эл. почты', email) },
}

const v$ = useVuelidate(rules, state)

const handleSubmit = async () => {
  const isFormCorrect = await v$.value.$validate()

  if (isFormCorrect === false)
    return

  const data = {
    name: state.name,
    phone: state.phone,
    email: state.email,
  }
  await $api('/contentapp/applications/', { method: 'POST', body: data })
  v$.value.$reset()
  state.name = ''
  state.phone = ''
  state.email = ''
  snackbar.value = true
}

</script>