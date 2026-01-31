<script setup lang="ts">
import { onMounted } from 'vue'
import usePlatosStore from '@/stores/platos'
import { storeToRefs } from 'pinia'
import { Icon } from '@iconify/vue'

const platosStore = usePlatosStore()
const { platos } = storeToRefs(platosStore)

onMounted(async () => {
  await platosStore.getAll()
})

async function handleDelete(id: number) {
  if (confirm('¿Estás seguro de eliminar este plato?')) {
    try {
      await platosStore.destroy(id)
      await platosStore.getAll()
      alert('Plato eliminado correctamente')
    } catch (error) {
      alert('Error al eliminar el plato')
    }
  }
}
</script>

<template>
  <div class="platos-list">
    <h1>Gestión de Platos</h1>
    
    <router-link :to="{ name: 'platos_create' }" class="btn btn-primary">
      <Icon icon="fa:plus-square" width="15" height="15" />
      Crear Nuevo Plato
    </router-link>

    <table v-if="platos.length > 0">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Descripción</th>
          <th>Categoría</th>
          <th>Precio</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="plato in platos" :key="plato.id">
          <td>{{ plato.nombre }}</td>
          <td>{{ plato.descripcion }}</td>
          <td>{{ plato.categoria_nombre }}</td>
          <td>${{ plato.precio }}</td>
          <td class="actions">
            <router-link :to="{ name: 'platos_show', params: { id: plato.id } }" class="btn-ver">
              <Icon icon="fa:eye" width="15" height="15" />
              Ver
            </router-link>
            <router-link :to="{ name: 'platos_edit', params: { id: plato.id } }" class="btn-editar">
              <Icon icon="fa:edit" width="15" height="15" />
              Editar
            </router-link>
            <button @click="handleDelete(plato.id)" class="btn-eliminar">
              <Icon icon="fa:times-rectangle" width="15" height="15" />
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else class="empty">No hay platos disponibles</p>
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