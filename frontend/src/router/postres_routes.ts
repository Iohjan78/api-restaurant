const postres_routes = [
  {
    path: '/postres',
    name: 'postres',
    component: () => import('../views/PostresView.vue'),
    redirect: { name: 'postres_list' },
    children: [
      {
        path: '',
        name: 'postres_list',
        component: () => import('../components/postres/PostresList.vue'),
      },
      {
        path: ':id/show',
        name: 'postres_show',
        component: () => import('../components/postres/PostresShow.vue'),
      },
      {
        path: 'create',
        name: 'postres_create',
        component: () => import('../components/postres/PostresCreate.vue'),
      },
      {
        path: ':id/edit',
        name: 'postres_edit',
        component: () => import('../components/postres/PostresUpdate.vue'),
      },
    ]
  }
]

export default postres_routes