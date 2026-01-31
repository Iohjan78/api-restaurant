<script setup lang="ts">
import { onMounted } from 'vue'
import useBebidasStore from '@/stores/bebidas'
import { storeToRefs } from 'pinia'
import { Icon } from '@iconify/vue'

const bebidasStore = useBebidasStore()
const { bebidas } = storeToRefs(bebidasStore)

onMounted(async () => {
  await bebidasStore.getAll()
  //debugger
})

async function handleDelete(id: number) {
  if (confirm('¿Estás seguro de eliminar esta bebida?')) {
    try {
      await bebidasStore.destroy(id)
      await bebidasStore.getAll()
      alert('Bebida eliminada correctamente')
    } catch (error) {
      alert('Error al eliminar la bebida')
    }
  }
}
</script>

<template>
  <div class="bebidas-list">
    <h1>Gestión de Bebidas</h1>
    
    <router-link :to="{ name: 'bebidas_create' }" class="btn btn-primary">
      <Icon icon="fa:plus-square" width="15" height="15" /> 
      Crear Nueva Bebida
    </router-link>

    <table v-if="bebidas.length > 0">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Categoría</th>
          <th>Precio</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="bebida in bebidas" :key="bebida.id">
          <td>{{ bebida.nombre }}</td>
          <td>{{ bebida.categoria_nombre }}</td>
          <td>${{ bebida.precio }}</td>
          <td class="actions">
            <router-link :to="{ name: 'bebidas_show', params: { id: bebida.id } }" class="btn-ver">
              <Icon icon="fa:eye" width="15" height="15" />
              Ver
            </router-link>
            <router-link :to="{ name: 'bebidas_edit', params: { id: bebida.id } }" class="btn-editar">
              <Icon icon="fa:edit" width="15" height="15" />
              Editar
            </router-link>
            <button @click="handleDelete(bebida.id)" class="btn-eliminar">
              <Icon icon="fa:times-rectangle" width="15" height="15" />
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else class="empty">No hay bebidas disponibles</p>
  </div>
</template>

<style scoped>
.bebidas-list {
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}
</style>