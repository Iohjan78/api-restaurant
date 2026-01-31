import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import platos_routes from './platos_routes'
import postres_routes from './postres_routes'
import bebidas_routes from './bebidas_routes'
import categorias_routes from './categorias_routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/admin',
      redirect: '/categorias',
    },
    ...platos_routes,
    ...postres_routes,
    ...bebidas_routes,
    ...categorias_routes,
  ],
})

export default router