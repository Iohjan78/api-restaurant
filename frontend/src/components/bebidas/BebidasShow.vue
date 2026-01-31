<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import useBebidasStore from '@/stores/bebidas'
import type { Bebidas } from '@/interfaces/Bebidas'
import { Icon } from '@iconify/vue'

const router = useRouter()
const route = useRoute()
const bebidasStore = useBebidasStore()

const bebida = ref<Bebidas | null>(null)

onMounted(async () => {
  const id = Number(route.params.id)
  bebida.value = await bebidasStore.getOne(id)
})

function goBack() {
  router.push({ name: 'bebidas_list' })
}

function goEdit() {
  router.push({ name: 'bebidas_edit', params: { id: bebida.value?.id } })
}
</script>

<template>
  <div class="bebidas-show">
    <div v-if="bebida" class="bebida-detail">
      <h1>{{ bebida.nombre }}</h1>
      
      <div class="detail-card">
        <div v-if="bebida.img" class="image-container">
          <img :src="bebida.img" :alt="bebida.nombre" />
        </div>

        <div class="info-grid">
          <div class="info-item">
            <span class="label">Nombre:</span>
            <span class="value">{{ bebida.nombre }}</span>
          </div>

          <div class="info-item">
            <span class="label">Categoría:</span>
            <span class="value">{{ bebida.categoria_nombre }}</span>
          </div>

          <div class="info-item">
            <span class="label">Precio:</span>
            <span class="value price">${{ bebida.precio }}</span>
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
.bebidas-show {
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>