import { defineStore } from "pinia"
import { ref } from 'vue'
import type { Platos, PlatosCreate, PlatosUpdate } from '@/interfaces/Platos'
import ApiService from "@/services/ApiService"

const usePlatosStore = defineStore('platos', () => {
  const platos = ref<Array<Platos>>([])
  const plato = ref<Platos>({
    id: 0,
    nombre: '',
    descripcion: '',
    categoria_id: 0,
    precio: '0',
    img: '',
    categoria_nombre: '',
    categoria_tipo: ''
  })
  const url = 'platos'

  async function getAll() {
    try {
      const data = await ApiService.getAll('platos')
      if (data) {
        platos.value = data
      }
    } catch (error) {
      console.error('Error al cargar platos:', error)
    }
  }

  async function getOne(id: number): Promise<Platos | null> {  
    const data = await ApiService.getOne('platos/', id)
    if (data) {
      plato.value = data
      return data  
    }
    return null  
  }

  async function create(plato: PlatosCreate) {
    await ApiService.create(url, plato)
    const nuevosPlatos = await ApiService.getAll(url)
    platos.value = nuevosPlatos
  }

  async function update(plato: PlatosUpdate) {
    if (plato.id) {
      await ApiService.update('platos/', plato.id, plato)
    }
  }

  async function destroy(id: number) {
    try {
      await ApiService.destroy('platos/', id)
    } catch (error) {
      console.error('Error al eliminar plato:', error)
      throw error
    }
  }

  return { platos, plato, getAll, getOne, create, destroy, update }
})

export default usePlatosStore