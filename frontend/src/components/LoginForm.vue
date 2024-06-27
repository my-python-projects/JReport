<template>
  <div class="login-container">
    <img src="/img/avatar.png" alt="Avatar" class="avatar">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="mb-3">
                <input v-model="email" type="text" class="form-control rounded-input" placeholder="Digite seu usuario ou email" required>
            </div>
            
            <div class="mb-3">
                <div class="input-group">
                    <input v-model="password" type="password" class="form-control rounded-input" placeholder="Digite sua senha" required>
                    <span class="input-group-text password-toggle" onclick="togglePassword()">
                        <i class="far fa-eye"></i>
                    </span>
                </div>
            </div>

            <div class="mb-3 remember-forgot">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="rememberMe">
                    <label class="form-check-label" for="rememberMe">
                        Lembrar
                    </label>
                </div>
                <a href="#" class="forgot-password">Esqueceu a senha?</a>
            </div>

            <button type="submit" class="btn btn-primary btn-login" id="btnLogin">Login</button>

            <hr style="margin-top: 20px; margin-bottom: 20px; border-color: #9b59b6;">

            <p class="mb-3" style="color: #9b59b6;">Ainda não tem uma conta?</p>
            <button type="button" class="btn create-account-btn" @click="redirectToSignup">Criar Conta</button>

    </form>
  </div>
</template>

<script>
import { loginUser } from '../utils/api';

export default {
  data() {
    return {
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await loginUser({ email: this.email, password: this.password });
        alert('Login successful:', response);
        // Redirecionar ou fazer algo após login bem-sucedido
      } catch (err) {
        console.log('Login failed');
      }
    },

    redirectToSignup() {
      this.$router.push('/register');
    }
  }
}
</script>
