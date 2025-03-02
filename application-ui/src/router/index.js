import {createRouter, createWebHashHistory} from 'vue-router';

const routes = [
    {
        path: '/',
        name: 'Main',
        component: () => import('@/views/main/Index.vue')
    },
    {
        path: '/money',
        name: 'Money',
        component: () => import('@/views/main/Money.vue')
    },
    {
        path: '/setting',
        name: 'Setting',
        component: () => import('@/views/main/Setting.vue')
    },
    {
        path: '/ui1',
        name: 'UI1',
        component: () => import('@/views/main/UI1.vue')
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes,
});


export default router
