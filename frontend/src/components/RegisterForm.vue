<template>
  <div class="register-container">
    <img src="/img/avatar.png" alt="Avatar" class="avatar">
    <h2>Cadastro</h2>
    <form @submit.prevent="register">
      <div class="mb-3">
        <input v-model="username" type="text" class="form-control rounded-input" placeholder="Usuario" required>
      </div>

      <div class="mb-3">
        <input v-model="email" type="text" class="form-control rounded-input" placeholder="Email" required>
      </div>

      <div class="mb-3">
        <input v-model="password" type="password" class="form-control rounded-input" placeholder="Digite sua senha" required>
      </div>

      <button type="submit" class="btn btn-primary btn-login" id="btnLogin">Cadastrar</button>

      <hr style="margin-top: 20px; margin-bottom: 20px; border-color: #9b59b6;">

      <p class="mb-3" style="color: #9b59b6;">Já possui uma conta?</p>
      <button type="button" class="btn create-account-btn" @click="redirectToLogin">Fazer Login</button>
    </form>
    <div v-if="qr_code">
      <h3>Escaneie o QR Code com seu aplicativo de autenticação:</h3>
      <img :src="qr_code" alt="QR Code">
    </div>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import { registerUser } from '../utils/api';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      error: '',
      qr_code: ''
    }
  },
  methods: {
    async register() {
      try {
        const response = await registerUser({ username: this.username, email: this.email, password: this.password });
        if (response.success) {
          this.qr_code = response.qr_code;  // Aqui, recebemos a string completa data:image/png;base64,
          alert('Registration successful');
        } else {
          this.error = response.message;
        }
      } catch (err) {
        console.log('Registration failed');
        this.error = 'Registration failed';
      }
    },

    redirectToLogin() {
      this.$router.push('/login');
    }
  }
}
</script>
