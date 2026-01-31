

const platos_routes = [
    {
    path: '/platos',
    name: 'platos',
    component: () => import('../views/PlatosView.vue'),
    redirect: { name: 'platos_list'},
    children: [
        {
            path:'',
            name:'platos_list',
            component: () => import('../components/platos/PlatosList.vue'),
        },
        {
            path: ':id/show',
            name: 'platos_show',
            component : () => import('../components/platos/PlatosShow.vue'),
        },
        {
            path: 'create',
            name: 'platos_create',
            component: () => import('../components/platos/PlatosCreate.vue'),
        },
        {
            path: ':id/edit',
            name: 'platos_edit',
            component: () => import ('../components/platos/PlatosUpdate.vue')
        },
        ]
    }
]

export default platos_routes