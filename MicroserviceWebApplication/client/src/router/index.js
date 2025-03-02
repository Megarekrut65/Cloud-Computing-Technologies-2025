import { createRouter, createWebHistory } from 'vue-router';
import Register from '../components/Register.vue';
import Login from '../components/Login.vue';
import CreateOrder from '../components/CreateOrder.vue';
import ProcessPayment from '../components/ProcessPayment.vue';
import OrderPaid from "@/components/OrderPaid.vue";

const routes = [
  { path: '/', component: Register },
  { path: '/login', component: Login },
  { path: '/create-order', component: CreateOrder },
  { path: '/paid', component: OrderPaid },
  {
    path: '/payment/:order_id',  // Route with order_id as a parameter
    name: 'Payment',
    component: ProcessPayment,
    props: true, // Make the route params available as props in the Payment component
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
