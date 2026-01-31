<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import usePostresStore from '@/stores/postres'
import useCategoriasStore from '@/stores/categorias'
import { storeToRefs } from 'pinia'
import type { PostresUpdate } from '@/interfaces/Postres'
import { Icon } from '@iconify/vue'

const router = useRouter()
const route = useRoute()
const postresStore = usePostresStore()
const categoriasStore = useCategoriasStore()
const { categorias } = storeToRefs(categoriasStore)

const form = ref<PostresUpdate>({
  id: 0,
  nombre: '',
  descripcion: '',
  categoria_id: 0,
  precio: 0,
  img: ''
})

onMounted(async () => {
  await categoriasStore.getAll()
  
  const id = Number(route.params.id)
  const postre = await postresStore.getOne(id)
  
  if (postre) {
    form.value = {
      id: postre.id,
      nombre: postre.nombre,
      descripcion: postre.descripcion,
      categoria_id: postre.categoria_id,
      precio: Number(postre.precio),
      img: postre.img
    }
  }
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
  
  try {
    await postresStore.update(form.value)
    alert('Postre actualizado correctamente')
    router.push({ name: 'postres_list' })
  } catch (error: any) {
    const mensaje = error.response?.data?.mensaje || 'Error al actualizar el postre'
    alert(mensaje)
  }
}

function handleCancel() {
  router.push({ name: 'postres_list' })
}
</script>

<template>
  <div class="postres-update">
    <h1>Editar Postre</h1>

    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input
          id="nombre"
          v-model="form.nombre"
          type="text"
          placeholder="Ej: Flan Casero"
          maxlength="100"
          minlength="5"
        />
      </div>

      <div class="form-group">
        <label for="descripcion">Descripción: *</label>
        <textarea
          id="descripcion"
          v-model="form.descripcion"
          rows="3"
          placeholder="Descripción del postre (mínimo 5 caracteres)"
          maxlength="500"
        ></textarea>
      </div>

      <div class="form-group">
        <label for="categoria">Categoría: *</label>
        <select id="categoria" v-model.number="form.categoria_id">
          <option value="0" disabled>Seleccione una categoría</option>
          <option
            v-for="categoria in categorias.filter(c => c.tipo === 'postre')"
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
          Actualizar Postre
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
.postres-update {
  max-width: 600px;
  margin: 0 auto;
}

h1 {
  margin-bottom: 30px;
  color: #333;
}
</style>