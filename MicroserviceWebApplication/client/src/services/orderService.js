import axios from 'axios';

// Define the backend URL (adjust it based on your setup)
const API_URL = 'http://localhost:8002/api/v1/orders'; // Replace with your API base URL

// Function to create an order
export const createOrder = async (orderData, token) => {
    try {
        const response = await axios.post(`${API_URL}/create/`, orderData, {
            headers: {
                Authorization: `Bearer ${token}`, // Include JWT token for authentication
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error creating order:', error);
        throw error;
    }
};
