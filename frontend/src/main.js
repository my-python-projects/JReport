import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/styles/main.css'; // Importando estilos globais

router.beforeEach((to, from, next) => {
  const body = document.body;
  body.className = ''; // Limpa as classes existentes

  // Adiciona classes específicas com base na rota ativa
  if (to.name === 'login') {
    body.classList.add('login-form-body');
  } else if (to.name === 'register') {
    body.classList.add('register-form-body');
  }
  next();
});



createApp(App)
  .use(router)
  .mount('#app');
