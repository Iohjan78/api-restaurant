<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import useCategoriasStore from '@/stores/categorias'
import type { Categorias } from '@/interfaces/Categorias'
import { Icon } from '@iconify/vue'

const router = useRouter()
const route = useRoute()
const categoriasStore = useCategoriasStore()

const form = ref<Categorias>({
  id: 0,
  nombre: '',
  tipo: 'plato'
})

onMounted(async () => {
  const id = Number(route.params.id)
  const categoria = await categoriasStore.getOne(id)
  
  if (categoria) {
    form.value = { ...categoria }
  }
})

async function handleSubmit() {
  
  // nombre
  if (!form.value.nombre || !form.value.nombre.trim()) {
    alert('El nombre es obligatorio')
    return
  }
  
  if (form.value.nombre.trim().length < 3) {
    alert('El nombre debe tener al menos 3 caracteres')
    return
  }
  
  // tipo
  if (!form.value.tipo) {
    alert('El tipo es obligatorio')
    return
  }
  
  const tiposValidos = ['plato', 'postre', 'bebida']
  if (!tiposValidos.includes(form.value.tipo)) {
    alert('El tipo debe ser: plato, postre o bebida')
    return
  }
  
  try {
    await categoriasStore.update(form.value)
    alert('Categoría actualizada correctamente')
    router.push({ name: 'categorias_list' })
  } catch (error: any) {
    const mensaje = error.response?.data?.mensaje || 'Error al actualizar la categoría'
    alert(mensaje)
  }
}

function handleCancel() {
  router.push({ name: 'categorias_list' })
}
</script>

<template>
  <div class="categorias-update">
    <h1>Editar Categoría</h1>

    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="nombre">Nombre: *</label>
        <input
          id="nombre"
          v-model="form.nombre"
          type="text"
          placeholder="Ej: Carnes"
          maxlength="100"
        />
      </div>

      <div class="form-group">
        <label for="tipo">Tipo: *</label>
        <select id="tipo" v-model="form.tipo">
          <option value="plato">Plato</option>
          <option value="postre">Postre</option>
          <option value="bebida">Bebida</option>
        </select>
      </div>

      <div class="form-actions">
        <button type="submit" class="btn btn-primary">
          <Icon icon="fa:check-circle" width="15" height="15" />
          Actualizar Categoría
        </button>
        <button type="button" class="btn btn-secondary" @click="handleCancel">
          <Icon icon="fa:times-rectangle" width="15" height="15" />
          Cancelar
        </button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.categorias-update {
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>