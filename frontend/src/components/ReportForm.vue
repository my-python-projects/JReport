<template>
  <div class="report-form-container">
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="nome">Nome:</label>
        <input type="text" class="form-control" id="nome" v-model="reportData.nome" placeholder="Digite seu nome" required>
      </div>

      <div class="form-group">
        <label for="data">Data:</label>
        <input type="date" class="form-control" id="data" v-model="reportData.data" required>
      </div>

      <div class="form-group">
        <label for="equipamento">Equipamento:</label>
        <input type="text" class="form-control" id="equipamento" v-model="reportData.equipamento" placeholder="Digite o equipamento" required>
      </div>

      <div class="form-row">
        <div class="col-md-6 mb-3">
          <label for="inicio">Início:</label>
          <input type="date" class="form-control" id="inicio" v-model="reportData.inicio" required>
        </div>
        <div class="col-md-6 mb-3">
          <label for="final">Final:</label>
          <input type="date" class="form-control" id="final" v-model="reportData.final" required>
        </div>
      </div>

      <div class="form-group">
        <label for="estoqueUtilizado">Estoque Utilizado:</label>
        <textarea class="form-control" id="estoqueUtilizado" v-model="reportData.estoqueUtilizado" rows="4" placeholder="Digite o estoque utilizado" required></textarea>
      </div>

      <div class="form-group">
        <label>Algo foi removido e voltou ao estoque?</label>
        <div class="form-check">
          <input type="radio" class="form-check-input" name="removidoVoltou" id="sim" value="sim" v-model="reportData.removidoVoltou">
          <label class="form-check-label" for="sim">Sim</label>
        </div>
        <div class="form-check">
          <input type="radio" class="form-check-input" name="removidoVoltou" id="nao" value="nao" v-model="reportData.removidoVoltou">
          <label class="form-check-label" for="nao">Não</label>
        </div>
      </div>

      <div class="form-group" v-if="reportData.removidoVoltou === 'sim'">
        <label for="motivoRemocao">Motivo da remoção:</label>
        <textarea class="form-control" id="motivoRemocao" v-model="reportData.motivoRemocao" rows="3" placeholder="Digite o motivo da remoção"></textarea>
      </div>

      <button type="submit" class="btn btn-primary btn-block">Enviar</button>
    </form>

    <!-- Modal de Sucesso -->
    <div class="modal fade" id="modalSucesso" tabindex="-1" role="dialog" aria-labelledby="modalSucessoLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalSucessoLabel">Sucesso!</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Nome escrito com sucesso no Word.
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de Erro -->
    <div class="modal fade" id="modalErro" tabindex="-1" role="dialog" aria-labelledby="modalErroLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalErroLabel">Erro!</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            Houve um erro ao escrever no Word.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { submitReport } from '@/utils/api';

export default {
  data() {
    return {
      reportData: {
        nome: '',
        data: '',
        equipamento: '',
        inicio: '',
        final: '',
        estoqueUtilizado: '',
        removidoVoltou: '',
        motivoRemocao: ''
      }
    }
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await submitReport(this.reportData);
        if (response.success) {
          $('#modalSucesso').modal('show');
        } else {
          $('#modalErro').modal('show');
        }
      } catch (error) {
        $('#modalErro').modal('show');
      }
    }
  }
}
</script>

<style scoped>
.report-form-container {
  background-color: #ffffff;
  border-radius: 20px;
  padding: 50px;
  box-shadow: 0 0 80px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 1200px;
  margin: 50px auto;
  color: #4a4a4a;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  font-weight: bold;
  color: #3498db;
  margin-bottom: 5px;
  display: block;
}

.form-control {
  border-radius: 25px;
  padding: 10px;
  border: 1px solid #ccc;
  font-size: 16px;
}

.form-check-input {
  margin-right: 10px;
}

.form-check-label {
  font-size: 16px;
}

.btn-primary {
  background-color: #8e44ad;
  border: none;
  padding: 10px;
  border-radius: 25px;
  font-size: 18px;
  width: 100%;
}

.modal-content {
  border-radius: 20px;
}

.modal-header, .modal-body {
  text-align: center;
}
</style>
