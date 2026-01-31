import type { Categorias } from './Categorias'

export interface Postres {
  id: number
  nombre: string
  descripcion: string
  categoria_id: number
  precio: string
  img: string
  categoria_nombre?: string
  categoria_tipo?: string
}


export interface PostresCreate {
  nombre: string
  descripcion: string
  categoria_id: number
  precio: number
  img: string
}


export interface PostresUpdate {
  id: number
  descripcion: string
  nombre: string
  categoria_id: number
  precio: number
  img: string
}