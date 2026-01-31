<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import usePostresStore from '@/stores/postres'
import type { Postres } from '@/interfaces/Postres'
import { Icon } from '@iconify/vue'

const router = useRouter()
const route = useRoute()
const postresStore = usePostresStore()

const postre = ref<Postres | null>(null)

onMounted(async () => {
  const id = Number(route.params.id)
  postre.value = await postresStore.getOne(id)
})

function goBack() {
  router.push({ name: 'postres_list' })
}

function goEdit() {
  router.push({ name: 'postres_edit', params: { id: postre.value?.id } })
}
</script>

<template>
  <div class="postres-show">
    <div v-if="postre" class="postre-detail">
      <h1>{{ postre.nombre }}</h1>
      
      <div class="detail-card">
        <div v-if="postre.img" class="image-container">
          <img :src="postre.img" :alt="postre.nombre" />
        </div>

        <div class="info-grid">
          <div class="info-item">
            <span class="label">ID:</span>
            <span class="value">{{ postre.id }}</span>
          </div>

          <div class="info-item">
            <span class="label">Nombre:</span>
            <span class="value">{{ postre.nombre }}</span>
          </div>

          <div class="info-item">
            <span class="label">Descripción:</span>
            <span class="value">{{ postre.descripcion }}</span>
          </div>

          <div class="info-item">
            <span class="label">Categoría:</span>
            <span class="value">{{ postre.categoria_nombre }}</span>
          </div>

          <div class="info-item">
            <span class="label">Precio:</span>
            <span class="value price">${{ postre.precio }}</span>
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
.postres-show {
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>