<script setup lang="ts">
import { onMounted } from 'vue'
import usePostresStore from '@/stores/postres'
import { storeToRefs } from 'pinia'
import { Icon } from '@iconify/vue'

const postresStore = usePostresStore()
const { postres } = storeToRefs(postresStore)

onMounted(async () => {
  await postresStore.getAll()
})

async function handleDelete(id: number) {
  if (confirm('¿Estás seguro de eliminar este postre?')) {
    try {
      await postresStore.destroy(id)
      await postresStore.getAll()
      alert('Postre eliminado correctamente')
    } catch (error) {
      alert('Error al eliminar el postre')
    }
  }
}
</script>

<template>
  <div class="postres-list">
    <h1>Gestión de Postres</h1>
    
    <router-link :to="{ name: 'postres_create' }" class="btn btn-primary">
      <Icon icon="fa:plus-square" width="15" height="15" />
      Crear Nuevo Postre
    </router-link>

    <table v-if="postres.length > 0">
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
        <tr v-for="postre in postres" :key="postre.id">
          <td>{{ postre.nombre }}</td>
          <td>{{ postre.descripcion }}</td>
          <td>{{ postre.categoria_nombre }}</td>
          <td>${{ postre.precio }}</td>
          <td class="actions">
            <router-link :to="{ name: 'postres_show', params: { id: postre.id } }" class="btn-ver">
              <Icon icon="fa:eye" width="15" height="15" />
              Ver
            </router-link>
            <router-link :to="{ name: 'postres_edit', params: { id: postre.id } }" class="btn-editar">
              <Icon icon="fa:edit" width="15" height="15" />
              Editar
            </router-link>
            <button @click="handleDelete(postre.id)" class="btn-eliminar">
              <Icon icon="fa:times-rectangle" width="15" height="15" />
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else class="empty">No hay postres disponibles</p>
  </div>
</template>

<style scoped>
.postres-list {
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}
</style>