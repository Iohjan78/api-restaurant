<script setup lang="ts">
import { onMounted } from 'vue'
import useCategoriasStore from '@/stores/categorias'
import { storeToRefs } from 'pinia'
import { Icon } from '@iconify/vue'

const categoriasStore = useCategoriasStore()
const { categorias } = storeToRefs(categoriasStore)

onMounted(async () => {
  await categoriasStore.getAll()
})

async function handleDelete(id: number) {
  if (confirm('¿Estás seguro de eliminar esta categoría?')) {
    try {
      await categoriasStore.destroy(id)
      await categoriasStore.getAll()
      alert('Categoría eliminada correctamente')
    } catch (error) {
      alert('Error al eliminar la categoría')
    }
  }
}
</script>

<template>
  <div class="categorias-list">
    <h1>Gestión de Categorías</h1>
    
    <router-link :to="{ name: 'categorias_create' }" class="btn btn-primary">
      <Icon icon="fa:plus-square" width="15" height="15" />
      Crear Nueva Categoría
    </router-link>

    <table v-if="categorias.length > 0">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Tipo</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="categoria in categorias" :key="categoria.id">
          <td>{{ categoria.nombre }}</td>
          <td>
            <span class="badge" :class="`badge-${categoria.tipo}`">
              {{ categoria.tipo }}
            </span>
          </td>
          <td class="actions">
            <router-link :to="{ name: 'categorias_show', params: { id: categoria.id } }" class="btn-ver">
              <Icon icon="fa:eye" width="15" height="15" />
              Ver
            </router-link>
            <router-link :to="{ name: 'categorias_edit', params: { id: categoria.id } }" class="btn-editar">
              <Icon icon="fa:edit" width="15" height="15" />
              Editar
            </router-link>
            <button @click="handleDelete(categoria.id)" class="btn-eliminar">
              <Icon icon="fa:times-rectangle" width="15" height="15" />
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else class="empty">No hay categorías disponibles</p>
  </div>
</template>

<style scoped>
.categorias-list {
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}
</style>