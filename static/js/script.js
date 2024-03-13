$('input[type=radio][name=removidoVoltou]').change(function () {
    if (this.value === 'sim') {
        $('#motivoRemocaoGroup').show();
    } else {
        $('#motivoRemocaoGroup').hide();
    }
});


$(document).ready(function () {
    $("#botaoEnviar").on("click", function () {
        // Adicionar animação de carregamento ao botão
        $(this).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Enviando...').prop('disabled', true);

        // Recuperar o nome do formulário
        var nome = $("#nome").val(),
            equipamento = $("#equipamento").val(),
            inicio = $("#inicio").val(),
            final = $("#final").val(),
            estoqueUtilizado = $("#estoqueUtilizado").val(),
            removidoVoltou = $("[name=removidoVoltou]").val(),
            motivoRemocao = $("[name=motivoRemocao]").val();

        // Simular uma chamada AJAX para o backend
        $.ajax({
            type: "POST",
            url: "/processar_formulario",
            data: { 
                nome: nome,
                equipamento: equipamento,
                inicio: inicio,
                final: final,
                estoqueUtilizado: estoqueUtilizado,
                removidoVoltou: removidoVoltou,
                motivoRemocao: motivoRemocao
            },
            success: function (data) {
                console.log(data);
                // Remover animação de carregamento
                $("#botaoEnviar").html('Enviar').prop('disabled', false);

                // Exibir modal de sucesso
                $("#modalSucesso").modal('show');

                // Ocultar modal de sucesso após 3 segundos
                setTimeout(function () {
                    $("#modalSucesso").modal('hide');
                }, 3000);
            },
            error: function () {
                // Remover animação de carregamento
                $("#botaoEnviar").html('Enviar').prop('disabled', false);

                // Exibir modal de erro
                $("#modalErro").modal('show');
            }
        });
    });
});
