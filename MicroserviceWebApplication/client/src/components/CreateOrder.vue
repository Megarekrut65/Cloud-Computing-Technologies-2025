<template>
    <div>
        <h1>Create Order</h1>
        <form @submit.prevent="createOrderBtn">
            <div class="mb-3">
                <label for="product" class="form-label">Product</label>
                <input v-model="order.product" type="text" class="form-control" id="product" required />
            </div>
            <div class="mb-3">
                <label for="price" class="form-label">Price</label>
                <input v-model="order.price" type="number" class="form-control" id="price" required />
            </div>
            <button type="submit" class="btn btn-primary">Submit Order</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import {createOrder} from "@/services/orderService.js";

const router = useRouter();

const order = ref({
    product: '',
    price: 0,
});

const createOrderBtn = async () => {
    try {
        const token = localStorage.getItem('token');
        const response = await createOrder(order.value, token);
        const order_id = response.id;  // Assuming the backend response includes the order_id

        // Navigate to the Payment page with the order_id as a route param
        router.push({ name: 'Payment', params: { order_id } });
    } catch (error) {
        console.error('Error creating order:', error);
    }
};
</script>
