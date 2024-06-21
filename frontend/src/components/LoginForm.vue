<template>
  <div class="login-container">
    <img src="/img/avatar.png" alt="Avatar" class="avatar">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="mb-3">
                <input type="text" class="form-control rounded-input" placeholder="Digite seu usuario ou email" required>
            </div>
            
            <div class="mb-3">
                <div class="input-group">
                    <input type="password" class="form-control rounded-input" placeholder="Digite sua senha" required>
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
            <button type="button" class="btn create-account-btn">Criar Conta</button>

    </form>
  </div>
</template>

<script>
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
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password
        })
      })
      const data = await response.json()
      if (response.ok) {
        alert(data.message)
      } else {
        this.error = data.error
      }
    }
  }
}
</script>
