<template>
    <v-container fluid style="height: 100vh; background-color: #141024;">
      <v-row class="text-white text-center align-center px-5" style="font-size: 30px; font-weight: 700;">
        <v-col cols="4" class="text-start">
          <a href="#">ROBO.SCHOOL</a>
        </v-col>
        <v-col cols="4">
          <v-row style="font-size: 20px; font-weight: 400;">
            <v-col link cols="4"> <a href="#about">О школе</a></v-col>
            <v-col cols="4"><a href="#teachers">Тренеры</a></v-col>
            <v-col cols="4"><a href="#price">Стоимость</a></v-col>
          </v-row>
        </v-col>
        <v-col cols="4" class="text-end">
          +7 800 000 11 22
        </v-col>
      </v-row>
      <v-container class="d-flex flex-row px-16">
            <v-row class="d-flex text-white align-center">
              <v-col cols="6" class="px-16">
                <p class="text-h3" style="font-weight: 600;">ROBO SCHOOL</p>
                <p class="my-12 text-white" style="font-size: 20px;">Курсы повышения квалификации по робототехнике для
                  педагогов начальной школы</p>
                <v-btn variant="tonal" size="large" class="text-white"
                  style="width: 260px !important; height: 80px !important; border-radius: 5px; background-color: #D52027; color:#ffffff !important;">Записаться
                  на курс</v-btn>
              </v-col>
              <v-col cols="6">
                <VImg :src="bannerImage" style="width: 91%;" />
              </v-col>
            </v-row>
        </v-container>
      </v-container>
</template>



<script setup lang="ts">
import bannerImage from 'images/banner-image.svg'
</script>

