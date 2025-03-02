<template>
    <div class="container mt-5">
        <h2>Process Payment</h2>
        <form @submit.prevent="handlePayment" class="w-50 mx-auto">
            <div class="mb-3">
                <label for="amount" class="form-label">Amount</label>
                <input
                    v-model="amount"
                    type="number"
                    class="form-control"
                    id="amount"
                    placeholder="Enter amount"
                    required
                />
            </div>

            <button type="submit" class="btn btn-warning w-100">Process Payment</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { processPayment } from '../services/paymentService';
import { useRouter } from 'vue-router';

const amount = ref(0);
const router = useRouter();

const handlePayment = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
        alert('Please login first');
        router.push('/login');
        return;
    }

    try {
        const paymentData = { order_id: 1, amount: amount.value }; // Example order_id
        const payment = await processPayment(paymentData, token);
        alert('Payment processed successfully!');
        router.push('/');
    } catch (error) {
        alert('Error processing payment');
    }
};
</script>
