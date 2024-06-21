import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/styles/main.css'; // Importando estilos globais

createApp(App)
  .use(router)
  .mount('#app');
