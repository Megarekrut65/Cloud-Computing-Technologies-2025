import axios from 'axios';

const API_URL = 'https://payments-service-production.up.railway.app/api/v1/payments/'; // Adjust to your Payment Service URL

// Process payment
export const processPayment = async (paymentData, token) => {
    try {
        const response = await axios.post(
            `${API_URL}process/`,
            paymentData,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }
        );
        return response.data;
    } catch (error) {
        console.error('Error processing payment:', error);
        throw error;
    }
};
