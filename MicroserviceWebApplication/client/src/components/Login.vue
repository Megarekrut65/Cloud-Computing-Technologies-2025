<template>
    <div class="container mt-5">
        <h2>Login</h2>
        <form @submit.prevent="handleLogin" class="w-50 mx-auto">
            <div class="mb-3">
                <label for="email" class="form-label">Username</label>
                <input
                    v-model="email"
                    type="text"
                    class="form-control"
                    id="email"
                    placeholder="Enter username"
                    required
                />
            </div>

            <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input
                    v-model="password"
                    type="password"
                    class="form-control"
                    id="password"
                    placeholder="Password"
                    required
                />
            </div>

            <button type="submit" class="btn btn-primary w-100">Login</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { loginUser } from '../services/userService';
import { useRouter } from 'vue-router';

const email = ref('');
const password = ref('');
const router = useRouter();

const handleLogin = async () => {
    try {
        const credentials = { username: email.value, password: password.value };
        const data = await loginUser(credentials);
        localStorage.setItem('token', data.access); // Save token
        router.push('/create-order');
    } catch (error) {
        alert('Error logging in');
    }
};
</script>
