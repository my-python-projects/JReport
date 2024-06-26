import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/views/Login.vue';
import Register from '@/views/Register.vue';
import Report from '@/views/Report.vue';

const routes = [
    {   
        path: '/', 
        redirect: '/login' 
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
    },
    {
        path: '/report',
        name: 'report',
        component: Report,
    },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
