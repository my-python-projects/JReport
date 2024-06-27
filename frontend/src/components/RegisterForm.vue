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
      error: ''
    }
  },
  methods: {
    async register() {
      try {
        const response = await registerUser({ username: this.username, email: this.email, password: this.password });
        alert('Registration successful:', response);
        // Redirecionar ou fazer algo após registro bem-sucedido
      } catch (err) {
        console.log('Registration failed');
      }
    },

    redirectToLogin() {
      this.$router.push('/login');
    }
  }
}
</script>
