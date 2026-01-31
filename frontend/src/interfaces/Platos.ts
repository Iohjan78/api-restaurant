import type { Categorias } from './Categorias'

export interface Platos {
  id: number
  nombre: string
  descripcion: string
  categoria_id: number
  precio: string
  img: string
  categoria_nombre?: string
  categoria_tipo?: string
}


export interface PlatosCreate {
  nombre: string
  descripcion: string
  categoria_id: number
  precio: number
  img: string
}


export interface PlatosUpdate {
  id: number
  descripcion: string
  nombre: string
  categoria_id: number
  precio: number
  img: string
}