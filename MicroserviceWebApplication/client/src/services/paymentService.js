import axios from 'axios';
import {PAYMENT_SERVICE_URL} from "@/services/api.js";

const API_URL = PAYMENT_SERVICE_URL; // Adjust to your Payment Service URL

// Process payment
export const processPayment = async (paymentData, token) => {
    try {
        const response = await axios.post(
            `${API_URL}payment/`,
            paymentData,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }
        );
        return response.data;
    } catch (error) {
        console.log(`Error processing payment: ${error}`);
        throw error;
    }
};
