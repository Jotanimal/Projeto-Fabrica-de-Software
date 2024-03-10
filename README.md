# Projeto-Fabrica-de-Software
API do projeto da fábrica de software - Unipê

Link da API: https://digimon-api.vercel.app/

*DIGIMON API:*

Essa API realiza simples buscas no banco de dados da API externa para validar os dados digitados pelo usuário e adicionar, remover ou atualizar Digimons no banco de dados atual e exibi-los no display do usuário.

- Instruções (utilizando Insomnia):

Para utilizar o método GET:

Na área de 'Parametros' do Insomnia digite o nome do Digimon desejado na área 'Value'.

Para utilizar o método POST: 

Adicione um 'Multipart' e preencha os campos 'name' com 'name' e 'value' com o nome do Digimon desejado.

Para utilizar o método PUT e DELETE:

Siga os mesmos passos do método POST.

- URL da API local: http://127.0.0.1:8000/api/digimon/

# Notas

Alguns erros continuaram presentes, pois não consegui consertar tudo até o dia final, porém o conceito base está funcionando.

-- Problemas presentes:

- Caso deixe a área de nome em branco, ao invés de retornar "Nenhum digimon digitado", é retornado " "" não está no nosso banco de dados!!" pois não consegui criar uma exceção apenas para quando o nome estivesse vazio e quando o nome não estivesse presente no BD.

- As imagens dos digimons aparecem como URL.

--- Usuário e senha para acesso da página Admin:

Usuário: admin
Senha: senha123