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
  border-radius: 40px;
  padding: 100px;
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.1);
  width: 100%; /* Ajusta a largura para ocupar 90% do viewport */
  max-width: 1000px; /* Define uma largura máxima */
  margin: 70px auto; /* Centraliza o contêiner e ajusta a margem superior */
}


</style>
