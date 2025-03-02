import { createRouter, createWebHistory } from 'vue-router';
import Register from '../components/Register.vue';
import Login from '../components/Login.vue';
import CreateOrder from '../components/CreateOrder.vue';
import ProcessPayment from '../components/ProcessPayment.vue';

const routes = [
  { path: '/', component: Register },
  { path: '/login', component: Login },
  { path: '/create-order', component: CreateOrder },
  { path: '/process-payment', component: ProcessPayment },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
