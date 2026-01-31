import { defineStore } from "pinia"
import { ref } from 'vue'
import type { Bebidas, BebidasCreate, BebidasUpdate } from '@/interfaces/Bebidas'  
import ApiService from "@/services/ApiService"

const useBebidasStore = defineStore('bebidas', () => {
  const bebidas = ref<Array<Bebidas>>([])
  const bebida = ref<Bebidas>({
    id: 0,
    nombre: '',
    categoria_id: 0,
    precio: '0',
    img: '',
    categoria_nombre: '',
    categoria_tipo: ''
  })
  const url = 'bebidas'

  async function getAll() {
    try {
      const data = await ApiService.getAll('bebidas')
      if (data) {
        bebidas.value = data
      }
    } catch (error) {
      console.error('Error al cargar bebidas:', error)
    }
  }

  async function getOne(id: number): Promise<Bebidas | null> {  
    const data = await ApiService.getOne('bebidas/', id)
    if (data) {
      bebida.value = data
      return data  
    }
    return null  
  }

  async function create(bebida: BebidasCreate) {
    await ApiService.create(url, bebida)
    const nuevasBebidas = await ApiService.getAll(url)
    bebidas.value = nuevasBebidas
  }

  async function update(bebida: BebidasUpdate) {
    if (bebida.id) {
      await ApiService.update('bebidas/', bebida.id, bebida)
    }
  }

  async function destroy(id: number) {
    try {
      await ApiService.destroy('bebidas/', id)
    } catch (error) {
      console.error('Error al eliminar bebida:', error)
      throw error
    }
  }

  return { bebidas, bebida, getAll, getOne, create, destroy, update }
})

export default useBebidasStore