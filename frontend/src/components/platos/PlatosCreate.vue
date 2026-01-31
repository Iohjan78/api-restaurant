<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import usePlatosStore from '@/stores/platos'
import useCategoriasStore from '@/stores/categorias'
import { storeToRefs } from 'pinia'
import type { PlatosCreate } from '@/interfaces/Platos' 
const router = useRouter()
const platosStore = usePlatosStore()
const categoriasStore = useCategoriasStore()
const { categorias } = storeToRefs(categoriasStore)
import { Icon } from '@iconify/vue'

const form = ref<PlatosCreate>({
  nombre: '',
  descripcion: '',
  categoria_id: 0,
  precio: 0,
  img: ''
})

onMounted(async () => {
  await categoriasStore.getAll()
})

async function handleSubmit() {
  // nombre
  if (!form.value.nombre || !form.value.nombre.trim()) {
    alert('El nombre es obligatorio')
    return
  }
  
  if (form.value.nombre.trim().length < 5) {
    alert('El nombre debe tener al menos 5 caracteres')
    return
  }
  
  // descripción
  if (!form.value.descripcion || !form.value.descripcion.trim()) {
    alert('La descripción es obligatoria')
    return
  }
  
  if (form.value.descripcion.trim().length < 5) {
    alert('La descripción debe tener al menos 5 caracteres')
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
  
  // ========================================
  // SI TODO ES VÁLIDO, ENVIAR AL BACKEND
  // ========================================
  
  try {
    await platosStore.create(form.value)
    alert('Plato creado correctamente')
    router.push({ name: 'platos_list' })
  } catch (error: any) {
    // Mostrar error del backend si existe
    const mensaje = error.response?.data?.mensaje || 'Error al crear el plato'
    alert(mensaje)
  }
}

function handleCancel() {
  router.push({ name: 'platos_list' })
}
</script>

<template>
  <div class="platos-create">
    <h1>Crear Nuevo Plato</h1>

    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="nombre">Nombre: *</label>
        <input
          id="nombre"
          v-model="form.nombre"
          type="text"
          placeholder="Ej: Milanesa Napolitana"
          maxlength="100"
        />
      </div>

      <div class="form-group">
        <label for="descripcion">Descripción: *</label>
        <textarea
          id="descripcion"
          v-model="form.descripcion"
          rows="3"
          placeholder="Descripción del plato (mínimo 5 caracteres)"
          maxlength="500"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="categoria">Categoría: *</label>
        <select id="categoria" v-model.number="form.categoria_id">
          <option value="0" disabled>Seleccione una categoría</option>
          <option
            v-for="categoria in categorias.filter(c => c.tipo === 'plato')"
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
          Crear Plato
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
.platos-create {
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>