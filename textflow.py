from docx import Document

def criar_documento_word(texto):
    # Criar um novo documento Word
    doc = Document()

    # Adicionar o texto ao documento
    doc.add_paragraph(texto)

    # Salvar o documento
    doc.save('documento_word.docx')
    print('Documento Word criado com sucesso!')

if __name__ == "__main__":
    # Solicitar ao usuário que insira o texto
    texto_usuario = input("Digite o texto que deseja inserir no documento Word: ")

    # Criar o documento Word com o texto inserido
    criar_documento_word(texto_usuario)
