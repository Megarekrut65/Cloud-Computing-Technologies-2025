import axios from 'axios';

const API_URL = 'https://gateway-production-69da.up.railway.app/api/payment'; // Adjust to your Payment Service URL

// Process payment
export const processPayment = async (paymentData, token) => {
    try {
        const response = await axios.post(
            `${API_URL}/`,
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
