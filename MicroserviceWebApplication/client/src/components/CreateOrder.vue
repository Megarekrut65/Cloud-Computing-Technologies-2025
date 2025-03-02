<template>
    <div class="container mt-5">
        <h2>Create Order</h2>
        <form @submit.prevent="handleCreateOrder" class="w-50 mx-auto">
            <div class="mb-3">
                <label for="product" class="form-label">Product</label>
                <input
                    v-model="product"
                    type="text"
                    class="form-control"
                    id="product"
                    placeholder="Enter product name"
                    required
                />
            </div>

            <div class="mb-3">
                <label for="price" class="form-label">Price</label>
                <input
                    v-model="price"
                    type="number"
                    step="0.01"
                    class="form-control"
                    id="price"
                    placeholder="Enter price"
                    required
                />
            </div>

            <button type="submit" class="btn btn-success w-100">Create Order</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { createOrder } from '../services/orderService';
import { useRouter } from 'vue-router';

const product = ref('');
const price = ref(0);
const user_id = ref(null);
const router = useRouter();

const handleCreateOrder = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
        alert('Please login first');
        router.push('/login');
        return;
    }

    try {
        const orderData = {
            product: product.value,
            price: price.value,
            user_id: user_id.value,
        };
        const order = await createOrder(orderData, token);
        alert('Order created successfully!');
        router.push('/process-payment');
    } catch (error) {
        alert('Error creating order');
    }
};
</script>
