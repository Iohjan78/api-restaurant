<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import useCategoriasStore from '@/stores/categorias'
import type { Categorias } from '@/interfaces/Categorias'
import { Icon } from '@iconify/vue'

const router = useRouter()
const route = useRoute()
const categoriasStore = useCategoriasStore()

const categoria = ref<Categorias | null>(null)

onMounted(async () => {
  const id = Number(route.params.id)
  categoria.value = await categoriasStore.getOne(id)
})

function goBack() {
  router.push({ name: 'categorias_list' })
}

function goEdit() {
  router.push({ name: 'categorias_edit', params: { id: categoria.value?.id } })
}
</script>

<template>
  <div class="categorias-show">
    <div v-if="categoria" class="categoria-detail">
      <h1>{{ categoria.nombre }}</h1>
      
      <div class="detail-card">
        <div class="info-grid">

          <div class="info-item">
            <span class="label">Nombre:</span>
            <span class="value">{{ categoria.nombre }}</span>
          </div>

          <div class="info-item">
            <span class="label">Tipo:</span>
            <span class="badge" :class="`badge-${categoria.tipo}`">
              {{  categoria.tipo }}
            </span>
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
.categorias-show {
  max-width: 800px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>