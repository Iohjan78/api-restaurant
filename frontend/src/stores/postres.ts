import { defineStore } from "pinia"
import { ref } from 'vue'
import type { Postres, PostresCreate, PostresUpdate } from '@/interfaces/Postres'  
import ApiService from "@/services/ApiService"

const usePostresStore = defineStore('postres', () => {
  const postres = ref<Array<Postres>>([])
  const postre = ref<Postres>({
    id: 0,
    nombre: '',
    descripcion: '',
    categoria_id: 0,
    precio: '0',
    img: '',
    categoria_nombre: '',
    categoria_tipo: ''
  })
  const url = 'postres'

  async function getAll() {
    try {
      const data = await ApiService.getAll('postres')
      if (data) {
        postres.value = data
      }
    } catch (error) {
      console.error('Error al cargar postres:', error)
    }
  }

  async function getOne(id: number): Promise<Postres | null> {  
    const data = await ApiService.getOne('postres/', id)
    if (data) {
      postre.value = data
      return data  
    }
    return null  
  }

  async function create(postre: PostresCreate) {
    await ApiService.create(url, postre)
    const nuevosPostres = await ApiService.getAll(url)
    postres.value = nuevosPostres
  }

  async function update(postre: PostresUpdate) {
    if (postre.id) {
      await ApiService.update('postres/', postre.id, postre)
    }
  }

  async function destroy(id: number) {
    try {
      await ApiService.destroy('postres/', id)
    } catch (error) {
      console.error('Error al eliminar postre:', error)
      throw error
    }
  }

  return { postres, postre, getAll, getOne, create, destroy, update }
})

export default usePostresStore