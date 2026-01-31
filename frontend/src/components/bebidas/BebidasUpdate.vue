<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import useBebidasStore from '@/stores/bebidas'
import useCategoriasStore from '@/stores/categorias'
import { storeToRefs } from 'pinia'
import type { BebidasUpdate } from '@/interfaces/Bebidas'
import { Icon } from '@iconify/vue'

const router = useRouter()
const route = useRoute()
const bebidasStore = useBebidasStore()
const categoriasStore = useCategoriasStore()
const { categorias } = storeToRefs(categoriasStore)

const form = ref<BebidasUpdate>({
  id: 0,
  nombre: '',
  categoria_id: 0,
  precio: 0,
  img: ''
})

onMounted(async () => {
  await categoriasStore.getAll()
  
  const id = Number(route.params.id)
  const bebida = await bebidasStore.getOne(id)
  
  if (bebida) {
    form.value = {
      id: bebida.id,
      nombre: bebida.nombre,
      categoria_id: bebida.categoria_id,
      precio: Number(bebida.precio),
      img: bebida.img
    }
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
  
  // precio
  if (!form.value.precio || form.value.precio <= 0) {
    alert('El precio debe ser mayor a 0')
    return
  }
  
  // categoría
  if (!form.value.categoria_id || form.value.categoria_id === 0) {
    alert('Debe seleccionar una categoría')
    return
  }
  
  try {
    await bebidasStore.update(form.value)
    alert('Bebida actualizada correctamente')
    router.push({ name: 'bebidas_list' })
  } catch (error: any) {
    const mensaje = error.response?.data?.mensaje || 'Error al actualizar la bebida'
    alert(mensaje)
  }
}

function handleCancel() {
  router.push({ name: 'bebidas_list' })
}
</script>

<template>
  <div class="bebidas-update">
    <h1>Editar Bebida</h1>

    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="nombre">Nombre: *</label>
        <input
          id="nombre"
          v-model="form.nombre"
          type="text"
          placeholder="Ej: Coca Cola"
          maxlength="100"
        />
      </div>

      <div class="form-group">
        <label for="categoria">Categoría: *</label>
        <select id="categoria" v-model.number="form.categoria_id">
          <option value="0" disabled>Seleccione una categoría</option>
          <option
            v-for="categoria in categorias.filter(c => c.tipo === 'bebida')"
            :key="categoria.id"
            :value="categoria.id"
          >
            {{ categoria.nombre }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="precio">Precio: *</label>
        <input
          id="precio"
          v-model.number="form.precio"
          type="number"
          step="0.01"
          min="0.01"
          placeholder="0.00"
        />
      </div>

      <div class="form-actions">
        <button type="submit" class="btn btn-primary">
          <Icon icon="fa:check-circle" width="15" height="15" />
          Actualizar Bebida
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
.bebidas-update {
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>