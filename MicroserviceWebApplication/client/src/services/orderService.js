import axios from 'axios';
import {ORDER_SERVICE_URL} from "@/services/api.js";

// Define the backend URL (adjust it based on your setup)
const API_URL = ORDER_SERVICE_URL; // Replace with your API base URL

// Function to create an order
export const createOrder = async (orderData, token) => {
    try {
        const response = await axios.post(`${API_URL}orders/`, orderData, {
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
