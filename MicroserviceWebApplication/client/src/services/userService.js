import axios from 'axios';

const API_URL = 'http://localhost:8001/api/v1/users/'; // Adjust to your User Service URL

// Register user
export const registerUser = async (userData) => {
    try {
        const response = await axios.post(`${API_URL}register/`, userData);
        return response.data;
    } catch (error) {
        console.error('Error registering user:', error);
        throw error;
    }
};

// Login user
export const loginUser = async (credentials) => {
    try {
        const response = await axios.post(`${API_URL}login/`, credentials); // Assuming there's a login route in User Service
        return response.data;
    } catch (error) {
        console.error('Error logging in:', error);
        throw error;
    }
};
