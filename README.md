# Projeto de Envio de E-mails Automatizado

Este projeto é um script Python simples que envia e-mails automaticamente para um endereço de e-mail especificado.
## Aviso Importante e Responsabilidade

Este script foi desenvolvido com o objetivo de servir como uma ferramenta para aprendizado e testes de funcionalidades relacionadas ao envio de e-mails. É importante usá-lo de maneira responsável e ética.

**ATENÇÂO**: O uso deste script para enviar spam ou para qualquer outra atividade maliciosa ou antiética é estritamente proibido. Esteja ciente de que o envio de e-mails em massa não solicitados pode violar as políticas de seu provedor de serviços de e-mail e/ou leis locais.

Ao utilizar este script, você assume total responsabilidade pelo seu uso. O autor deste código não se responsabiliza por qualquer uso indevido, danos, ou consequências legais decorrentes do uso deste script. Use-o por sua conta e risco, e sempre com responsabilidade.
## Descrição

O script permite ao usuário enviar múltiplas cópias de uma mensagem de e-mail para um endereço de e-mail definido. É
ideal para testes de funcionalidades de e-mail ou para uso pessoal.

## Configuração

Antes de começar a usar o script, você precisa configurar algumas coisas:

### Pré-requisitos

- Python 3
- Bibliotecas Python: `smtplib`, `os`, `random`, `email.mime`
- Uma conta Gmail

### Instalação

1. Clone o repositório para a sua máquina local.
2. Instale as dependências necessárias com o comando:

``` pip install python-dotenv ```

### Configuração do Ambiente

1. Crie um arquivo `.env` na raiz do projeto.
2. Adicione as seguintes variáveis ao arquivo `.env`:

```
EMAIL_ADDRESS=seuemail@gmail.com
EMAIL_PASSWORD=suasenha
SUBJECT=Assunto do Email
MESSAGE=Sua mensagem aqui
MESSAGE_RELOAD=10
```

## Uso

Execute o script com o comando:
```python disparador.py```

## Segurança e Autenticação

**Importante**: Para a segurança da sua conta de e-mail, é altamente recomendável que você utilize a opção "Fazer login
com senhas de app" providenciada pelo Google. Isso permite que você crie uma senha específica para este script, sem
expor a senha da sua conta de e-mail.

Para mais informações e instruções sobre como configurar uma senha de app,
visite [Fazer login com senhas de app](https://support.google.com/accounts/answer/185833?hl=pt-BR).

## Contribuições

Contribuições são sempre bem-vindas. Sinta-se à vontade para clonar, forkar ou enviar pull requests.

## Licença

Este projeto está sob a licença MIT.