<template>
  <div class="form-body">
    <div class="container">
      <img src="/img/avatar.png" alt="Avatar" class="avatar">
      <h2>Cadastro</h2>
      <form @submit.prevent="register" v-if="!qr_code">
        <div class="mb-3">
          <input v-model="username" type="text" class="form-control rounded-input" placeholder="Usuário" required>
        </div>
        <div class="mb-3">
          <input v-model="email" type="text" class="form-control rounded-input" placeholder="Email" @blur="validateEmailField" required>
          <span v-if="emailError" class="text-danger">{{ emailError }}</span>
        </div>
        <div class="mb-3">
          <input v-model="password" type="password" class="form-control rounded-input" placeholder="Digite sua senha" @blur="validatePasswordField" required>
          <span v-if="passwordError" class="text-danger">{{ passwordError }}</span>
        </div>
        <button type="submit" class="btn btn-primary">Cadastrar</button>
        <hr style="margin: 20px 0; border-color: #9b59b6;">
        <p class="mb-3" style="color: #9b59b6;">Já possui uma conta?</p>
        <button type="button" class="btn create-account-btn" @click="redirectToLogin">Fazer Login</button>
      </form>
      <div v-if="qr_code" class="qr-code-container">
        <h3 class="qr-code-instructions">Escaneie o QR Code com seu aplicativo de autenticação:</h3>
        <img :src="qr_code" alt="QR Code">
        <p class="qr-code-instructions">Depois de escanear, use o aplicativo para obter seu token 2FA.</p>
      </div>
      <p v-if="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { registerUser } from '../utils/api';
import { validateEmail, validatePassword } from '@/utils/validation';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      error: '',
      qr_code: '',
      emailError: '',
      passwordError: ''
    }
  },
  methods: {
    async register() {
      try {
        if(!this.emailError && !this.passwordError){
          const response = await registerUser({ username: this.username, email: this.email, password: this.password });
         
          if (response.success) {
            this.qr_code = response.qr_code;  // Recebemos a string completa data:image/png;base64,
          } else {
            this.error = response.message;
          }
        }else{
          this.error = '[ERRO] Verifique o email ou a senha informada!';
        }

      } catch (err) {
        console.log('Registration failed');
        this.error = 'Registration failed';
      }
    },
    redirectToLogin() {
      this.$router.push('/login');
    },
    validateEmailField() {
      this.emailError = !validateEmail(this.email) ? 'Email inválido.' : '';
    },
    validatePasswordField() {
      if (!validatePassword(this.password)) {
        this.passwordError = 'A senha deve ter pelo menos 6 caracteres, uma letra maiúscula, um número e um símbolo especial.';
      } else {
        this.passwordError = '';
      }
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

.text-danger {
  color: red;
}
</style>