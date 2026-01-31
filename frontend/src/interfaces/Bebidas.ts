import type { Categorias } from './Categorias'

export interface Bebidas {
  id: number
  nombre: string
  categoria_id: number
  precio: string
  img: string
  categoria_nombre?: string
  categoria_tipo?: string
}


export interface BebidasCreate {
  nombre: string
  categoria_id: number
  precio: number
  img: string
}


export interface BebidasUpdate {
  id: number
  nombre: string
  categoria_id: number
  precio: number
  img: string
}