import { defineStore } from "pinia"
import { ref } from 'vue'
import type { Categorias } from '@/interfaces/Categorias'  
import ApiService from "@/services/ApiService"

const useCategoriasStore = defineStore('categorias', () => {
  const categorias = ref<Array<Categorias>>([])  
  const categoria = ref<Categorias>({
    id: 0,
    nombre: '',
    tipo: 'plato'
  })
  const url = 'categorias'

  async function getAll() {
    try {
      const data = await ApiService.getAll('categorias')
      if (data) {
        categorias.value = data
      }
    } catch (error) {
      console.error('Error al cargar categorías:', error)
    }
  }

  async function getOne(id: number): Promise<Categorias | null> {  
    const data = await ApiService.getOne('categorias/', id)
    if (data) {
      categoria.value = data
      return data  
    }
    return null  
  }

  async function create(categoria: Categorias) {
    await ApiService.create(url, categoria)
    const nuevasCategorias = await ApiService.getAll(url)
    categorias.value = nuevasCategorias
  }

  async function update(categoria: Categorias) {
    if (categoria.id) {
      await ApiService.update('categorias/', categoria.id, categoria)
    }
  }

  async function destroy(id: number) {
    try {
      await ApiService.destroy('categorias/', id)
    } catch (error) {
      console.error('Error al eliminar categoría:', error)
      throw error
    }
  }

  return { categorias, categoria, getAll, getOne, create, destroy, update }
})

export default useCategoriasStore