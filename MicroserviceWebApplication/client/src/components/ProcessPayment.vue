<template>
    <div>
        <h1>Payment for Order #{{ order_id }}</h1>
        <form @submit.prevent="processPaymentBtn">
            <div class="mb-3">
                <label for="paymentAmount" class="form-label">Amount</label>
                <input v-model="payment.amount" type="number" class="form-control" id="paymentAmount" required />
            </div>
            <button type="submit" class="btn btn-success">Pay</button>
        </form>
    </div>
</template>

<script setup>
import { ref, defineProps } from 'vue';
import {processPayment} from "@/services/paymentService.js";
import {useRouter} from "vue-router";

// Extract the order_id from route params using defineProps
const props = defineProps({
    order_id: {
        type: String,
        required: true,
    },
});

const payment = ref({
    amount: '',
    order_id:props.order_id
});

const router = useRouter()

const processPaymentBtn = async () => {
    try {
        const token = localStorage.getItem('token');
        const response = await processPayment(payment.value, token);
        router.push("/paid");
    } catch (error) {
        alert(`Payment failed: ${error}`);
    }
};
</script>
