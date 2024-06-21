<template>
  <div class="register-container">
    <img src="/img/avatar.png" alt="Avatar" class="avatar">
    <h2>Cadastro</h2>
  <form @submit.prevent="register">
    <div class="mb-3">
                <input type="text" class="form-control rounded-input" placeholder="Usuario" required>
            </div>

            <div class="mb-3">
              <input type="text" class="form-control rounded-input" placeholder="Email" required>
            </div>

            <div class="mb-3">
              <input type="password" class="form-control rounded-input" placeholder="Digite sua senha" required>
            </div>

            <button type="submit" class="btn btn-primary btn-login" id="btnLogin">Cadastrar</button>

            <hr style="margin-top: 20px; margin-bottom: 20px; border-color: #9b59b6;">

            <p class="mb-3" style="color: #9b59b6;">Já possui uma conta?</p>
            <button type="button" class="btn create-account-btn">Fazer Login</button>
  </form>
</div>
</template>

<script>
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
      const response = await fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: this.username,
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
