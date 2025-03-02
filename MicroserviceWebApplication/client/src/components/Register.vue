<template>
    <div class="container mt-5">
        <h2>Register</h2>
        <form @submit.prevent="handleRegister" class="w-50 mx-auto">
            <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input
                    v-model="username"
                    type="text"
                    class="form-control"
                    id="username"
                    placeholder="Enter username"
                    required
                />
            </div>

            <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input
                    v-model="email"
                    type="email"
                    class="form-control"
                    id="email"
                    placeholder="Enter email"
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

            <button type="submit" class="btn btn-primary w-100">Register</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { registerUser } from '../services/userService';
import { useRouter } from 'vue-router';

const username = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();

const handleRegister = async () => {
    try {
        const userData = { username: username.value, email: email.value, password: password.value };
        const data = await registerUser(userData);
        alert('User registered successfully!');
        router.push('/login');
    } catch (error) {
        alert('Error registering user');
    }
};
</script>
