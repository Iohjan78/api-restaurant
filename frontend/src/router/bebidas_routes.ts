const bebidas_routes = [
  {
    path: '/bebidas',
    name: 'bebidas',
    component: () => import('../views/BebidasView.vue'),
    redirect: { name: 'bebidas_list' },
    children: [
      {
        path: '',
        name: 'bebidas_list',
        component: () => import('@/components/bebidas/BebidasList.vue'),
      },
      {
        path: ':id/show',
        name: 'bebidas_show',
        component: () => import('@/components/bebidas/BebidasShow.vue'),
      },
      {
        path: 'create',
        name: 'bebidas_create',
        component: () => import('@/components/bebidas/BebidasCreate.vue'),
      },
      {
        path: ':id/edit',
        name: 'bebidas_edit',
        component: () => import('@/components/bebidas/BebidasUpdate.vue'),
      },
    ]
  }
]

export default bebidas_routes