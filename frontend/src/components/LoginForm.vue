<template>
  <div class="form-body">
    <div class="container" v-if="!step2fa">
      <img src="/img/avatar.png" alt="Avatar" class="avatar">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div class="mb-3">
          <input v-model="email" type="text" class="form-control rounded-input" placeholder="Digite seu usuário ou email" required>
        </div>
        <div class="mb-3">
          <div class="input-group">
            <input v-model="password" type="password" class="form-control rounded-input" placeholder="Digite sua senha" required>
            <span class="input-group-text password-toggle" @click="togglePassword">
              <i class="far fa-eye"></i>
            </span>
          </div>
        </div>
        <div class="mb-3 remember-forgot">
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="rememberMe">
            <label class="form-check-label" for="rememberMe">Lembrar</label>
          </div>
          <a href="#" class="forgot-password">Esqueceu a senha?</a>
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
        <hr style="margin: 20px 0; border-color: #9b59b6;">
        <p class="mb-3" style="color: #9b59b6;">Ainda não tem uma conta?</p>
        <button type="button" class="btn create-account-btn" @click="redirectToSignup">Criar Conta</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
    <div class="container" v-if="step2fa">
      <img src="/img/avatar.png" alt="Avatar" class="avatar">
      <h2>Autenticação 2FA</h2>
      <form @submit.prevent="verify2fa">
        <div class="mb-3">
          <input v-model="token_2fa" type="text" class="form-control rounded-input" placeholder="Digite seu token 2FA" required>
        </div>
        <button type="submit" class="btn btn-primary">Verificar</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { loginUser } from '../utils/api';

export default {
  data() {
    return {
      email: '',
      password: '',
      token_2fa: '',
      error: '',
      step2fa: false
    }
  },
  methods: {
    async login() {
      try {
        console.log("Sending login data:", this.email, this.password);
        const response = await loginUser({ email: this.email, password: this.password });
        console.log('Login step 1 successful:', response);

        if (response.success) {
          this.step2fa = true;  // Move to 2FA step
        } else {
          this.error = response.message;
        }
      } catch (err) {
        console.log('Login failed:', err);
        this.error = 'Login failed';
      }
    },
    async verify2fa() {
      try {
        console.log("Verifying 2FA token:", this.token_2fa);
        const response = await loginUser({ email: this.email, password: this.password, token_2fa: this.token_2fa });
        console.log('2FA verification successful:', response);

        if (response.success) {
          this.$router.push('/report');
        } else {
          this.error = response.message;
        }
      } catch (err) {
        console.log('2FA verification failed:', err);
        this.error = '2FA verification failed';
      }
    },
    redirectToSignup() {
      this.$router.push('/register');
    },
    togglePassword() {
      const passwordField = this.$el.querySelector('input[type="password"]');
      passwordField.type = passwordField.type === 'password' ? 'text' : 'password';
    }
  }
}
</script>

<style scoped>
.form-body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
}
</style>