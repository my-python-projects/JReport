<template>

<div class="container mt-5 form-container">
  <form @submit.prevent="submitReport">
      <div class="form-group">
          <label for="nome">Nome:</label>
          <input type="text" class="form-control" id="nome" name="nome" placeholder="Digite seu nome" required>
      </div>

      <div class="form-group">
          <label for="data">Data:</label>
          <input type="date" class="form-control" id="data" name="data" required>
      </div>

      <div class="form-group">
          <label for="equipamento">Equipamento:</label>
          <input type="text" class="form-control" id="equipamento" name="equipamento" placeholder="Digite o equipamento" required>
      </div>

      <div class="form-row">
          <div class="col-md-6">
              <label for="inicio">Início:</label>
              <input type="date" class="form-control" id="inicio" name="inicio" required>
          </div>
          <div class="col-md-6">
              <label for="final">Final:</label>
              <input type="date" class="form-control" id="final" name="final" required>
          </div>
      </div>

      <br/>

      <div class="form-group">
          <label for="estoqueUtilizado">Estoque Utilizado:</label>
          <textarea class="form-control" id="estoqueUtilizado" name="estoqueUtilizado" rows="4" placeholder="Digite o estoque utilizado" required></textarea>
      </div>

      <div class="form-row">
          <label>Algo foi removido e voltou ao estoque?</label>
          <div class="form-check">
              <input type="radio" class="form-check-input" name="removidoVoltou" id="sim" value="sim">
              <label class="form-check-label" for="sim">Sim</label>
          </div>
          <div class="form-check">
              <input type="radio" class="form-check-input" name="removidoVoltou" id="nao" value="nao">
              <label class="form-check-label" for="nao">Não</label>
          </div>
      </div>

      <div class="form-group" id="motivoRemocaoGroup" style="display: none;">
          <label for="motivoRemocao">Motivo da remoção:</label>
          <textarea class="form-control" id="motivoRemocao" name="motivoRemocao" rows="3" placeholder="Digite o motivo da remoção"></textarea>
      </div>

      <button type="button" class="btn btn-primary" id="botaoEnviar">Enviar</button>
  </form>
</div>

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

</template>
  
<script>
  export default {
    data() {
      return {
        title: '',
        content: '',
        error: ''
      }
    },
    methods: {
      async submitReport() {
        const response = await fetch('http://localhost:5000/api/report', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            title: this.title,
            content: this.content
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

<style>
        body {
            background: linear-gradient(135deg, #3498db, #9b59b6);
        }

        .form-container {
            background-color: #ffffff;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }


</style>
  