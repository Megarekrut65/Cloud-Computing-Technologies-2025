import axios from 'axios';
import {USER_SERVICE_URL} from "@/services/api.js";

const API_URL = USER_SERVICE_URL; // Adjust to your User Service URL

// Register user
export const registerUser = async (userData) => {
    try {
        const response = await axios.post(`${API_URL}register/`, userData);
        return response.data;
    } catch (error) {
        console.log(`Error registering user:${error}`, );
        throw error;
    }
};

// Login user
export const loginUser = async (credentials) => {
    try {
        const response = await axios.post(`${API_URL}login/`, credentials); // Assuming there's a login route in User Service
        return response.data;
    } catch (error) {
        console.log(`Error login user:${error}`, );
        throw error;
    }
};
