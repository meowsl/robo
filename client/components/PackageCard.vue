<template>
  <v-card class="package-card d-flex align-center justify-center mt-16">
    <v-card-content class="package-card__content d-flex flex-column justify-center align-center text-center pa-10">
      <p class="package-card__title">
        {{ pack?.name }}
      </p>
      <p class="package-card__price pt-16">
        {{ pack?.price }} ₽
      </p>
      <v-card-text class="package-card__text mt-10">
        {{ pack?.descript }}
      </v-card-text>
      <v-card-actions>
        <v-btn variant="total" size="small" class="package-card__button pa-1 ma-5">
          <p class="text-button">Оставить заявку</p>
        </v-btn>
      </v-card-actions>

    </v-card-content>
  </v-card>
</template>

<script setup lang="ts">
import { PackagesInfo } from 'models/teach_info';
import { PropType } from 'vue';


defineProps({
  pack: Object as PropType<PackagesInfo>
});
</script>