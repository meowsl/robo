<template>
  <div class="request-block">
    <VImg :src="backFoot" class="request-block__img" />
    <v-container class="request pa-16">
      <v-row class="text-white text-left">
        <v-col cols="6">
          <p class="request-block__text mb-3">Запишитесь на курс со скидкой 10%</p>
          Акция действительна до 10 марта 2022 года
        </v-col>
        <v-col cols="6">
        </v-col>
      </v-row>

    </v-container>
  </div>
  <!-- 
  <v-container style="background-color: #141024; he ight: 160px;">
    <v-footer-content class="text-white" style="display: flex; flex-direction: row; justify-content: space-between;">
      <content-first class="d-flex flex-column text-left pa-8">
        <p style="font-size: 30px; font-weight: 700;">ROBO.SCHOOL</p>
        <p style="color: rgba(255, 255, 255, 0.7); font-size: 16px;"></p>© ROBO.SCHOOL
      </content-first>
      <content-second class="d-flex flex-column text-end pa-8">
        <p style="font-size: 30px; font-weight: 700;">+7 800 000 11 22</p>
      </content-second>
    </v-footer-content>
  </v-container>
  -->
</template>


<script setup lang="ts">
import backFoot from 'images/foot-back.png'
</script>