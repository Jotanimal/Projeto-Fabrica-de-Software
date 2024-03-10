from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response
from .serializers import DigimonSerializer
from ..models import DigimonModel
import requests

class DigimonList(generics.ListAPIView):
    queryset = DigimonModel.objects.all()
    serializer_class = DigimonSerializer

    # Criando o método GET

    def get(self, request, format=None):
        name = request.query_params.get('name')
        print(name)
        
        # Acessando a URL da API da qual quero pegar informações
        
        external_api_url = f'https://digimon-api.vercel.app/api/digimon/name/{name}'
        
        response = requests.get(external_api_url) 


        if response.status_code == 200: # Verificando se o retorno com a API externa está OK
           
            # Fazendo com que a API externa retorne os dados JSON
           
            dados = response.json()
                
            return Response(dados)                       
        else:
            return Response({'Erro': 'Falha ao resgatar dados da API'}, status=response.status_code)

    # Criando o método POST
        
    def post(self, request, format=None):
        name = request.data.get('name')
        print(name)
        external_api_url = f'https://digimon-api.vercel.app/api/digimon/name/{name}'
        
        response = requests.get(external_api_url) 
        
        if response.status_code == 200: # Verificando se o retorno com a API externa está OK
            dados = response.json()
            print(dados)

            if isinstance(dados, list):
                
                # Nesse caso específico, os dados na API externa na verdade eram uma lista JSON e não um único objeto JSON, então precisei fazer um 'workaround' para conseguir ler os dados que o usuário digita, caso o contrário receberia o erro "'list' object has no attribute get json".

                if dados:  # Verifica se a lista não está vazia
                    primeiro_digimon = dados[0]
                    name = primeiro_digimon.get('name', '')
                    imagem_digimon = primeiro_digimon.get('img', '')
                    level_digimon = primeiro_digimon.get('level', '')

                    dados_digitados = {
                        "name": name,
                        "img": imagem_digimon,
                        "level": level_digimon
                    }
                    
                    serializer = DigimonSerializer(data = dados_digitados)
                    
                if serializer.is_valid():
                        digimon_pesquisado = DigimonModel.objects.filter(name = name)

                        digimon_pesquisado_existe = digimon_pesquisado.exists()

                        if digimon_pesquisado_existe:
                            return Response({"Aviso": f'{name} já existe no sistema!!'})
                        
                        serializer.save()
                        return Response(serializer.data)
                else:
                    return Response({"Aviso: Ocorreu algum erro inesperado!!": f'{serializer.errors}'})
        else:
            return Response({'Erro': f'{name} não está no nosso banco de dados!!'})

    # Criando o método PUT

    def put(self, request, format = None):
        name = request.data.get('name')
        print(name)
        external_api_url = f'https://digimon-api.vercel.app/api/digimon/name/{name}'

        response = requests.get(external_api_url)

        if response.status_code == 200: # Verificando se o retorno com a API externa está OK
            dados = response.json()
            print(dados)

            if isinstance(dados, list):
                if dados:  # Verifica se a lista não está vazia
                    primeiro_digimon = dados[0]
                    name = primeiro_digimon.get('name', '')
                    imagem_digimon = primeiro_digimon.get('img', '')
                    level_digimon = primeiro_digimon.get('level', '')

                    dados_digitados = {
                        "name": name,
                        "img": imagem_digimon,
                        "level": level_digimon
                    }
                    
                    serializer = DigimonSerializer(data=dados_digitados)
                    
                    if serializer.is_valid():
                        digimon_pesquisado = DigimonModel.objects.filter(name=name)

                        digimon_pesquisado_existe = digimon_pesquisado.exists()

                        if digimon_pesquisado_existe:
                            return Response({"Aviso": f'{name} já existe no sistema!!'})
                        
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response({"Aviso: Ocorreu algum erro inesperado!!": f'{serializer.errors}'})
            else:
                return Response({'Erro': f'{name} não está no nosso banco de dados!!'})
            
    # Criando o método DELETE
            
    def delete(self, request, format = None):
      name = request.data.get('name')
      print(name)

      # Lógica para deletar o objeto escolhido
      try:
          digimon = DigimonModel.objects.get(name=name)
          digimon.delete()
          return Response({"Mensagem": f'{name} removido com sucesso!!'})
      except DigimonModel.DoesNotExist:
          return Response({'Erro': f'{name} não existe no sistema!!'})  
