<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import usePlatosStore from '@/stores/platos'
import type { Platos } from '@/interfaces/Platos'
import { Icon } from '@iconify/vue'

const router = useRouter()
const route = useRoute()
const platosStore = usePlatosStore()

const plato = ref<Platos | null>(null)

onMounted(async () => {
  const id = Number(route.params.id)
  plato.value = await platosStore.getOne(id)
})

function goBack() {
  router.push({ name: 'platos_list' })
}

function goEdit() {
  router.push({ name: 'platos_edit', params: { id: plato.value?.id } })
}
</script>

<template>
  <div class="platos-show">
    <div v-if="plato" class="plato-detail">
      <h1>{{ plato.nombre }}</h1>
      
      <div class="detail-card">
        <div v-if="plato.img" class="image-container">
          <img :src="plato.img" :alt="plato.nombre" />
        </div>

        <div class="info-grid">


          <div class="info-item">
            <span class="label">Nombre:</span>
            <span class="value">{{ plato.nombre }}</span>
          </div>

          <div class="info-item">
            <span class="label">Descripción:</span>
            <span class="value">{{ plato.descripcion }}</span>
          </div>

          <div class="info-item">
            <span class="label">Categoría:</span>
            <span class="value">{{ plato.categoria_nombre }}</span>
          </div>

          <div class="info-item">
            <span class="label">Precio:</span>
            <span class="value price">${{ plato.precio }}</span>
          </div>
        </div>

        <div class="actions">
          <button @click="goEdit" class="btn btn-primary">
            <Icon icon="fa:edit" width="15" height="15" />
            Editar
          </button>
          <button @click="goBack" class="btn btn-secondary">
            <Icon icon="fa:chevron-circle-left" width="15" height="15" />
            Volver
          </button>
        </div>
      </div>
    </div>

    <div v-else class="loading">
      Cargando...
    </div>
  </div>
</template>

<style scoped>
.platos-show {
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>