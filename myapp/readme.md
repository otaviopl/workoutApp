Workout App
O Workout App é uma aplicação simples desenvolvida com Kivy e MongoDB para gerenciar diferentes treinos e exercícios.

Funcionalidades
Visualizar diferentes treinos (Push e Pull).
Visualizar exercícios associados a cada treino.
Atualizar o peso dos exercícios.
Pré-requisitos
Python 3.x
Kivy
MongoDB
Instalação
Clone o repositório:

bash
Copy code
git clone https://github.com/seu-usuario/workout-app.git
Navegue até o diretório do projeto:

bash
Copy code
cd workout-app
Instale as dependências:

bash
Copy code
pip install -r requirements.txt
Configuração do MongoDB
Certifique-se de ter o MongoDB instalado e em execução.

Configure a URL de conexão com o MongoDB no arquivo config/config.py.

python
Copy code
MONGODB_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "meu_banco_de_dados"
COLLECTION_NAME = "minha_colecao"
Executando o Projeto
Para executar a aplicação, execute o seguinte comando no terminal:

bash
Copy code
python main_view.py
Como Contribuir
Se você gostaria de contribuir para este projeto, siga os passos abaixo:

Faça um fork do repositório.
Crie uma nova branch com a sua feature ou correção de bug: git checkout -b nome-da-sua-feature
Faça commit das suas mudanças: git commit -m 'Descrição da sua mudança'
Faça push para a branch: git push origin nome-da-sua-feature
Abra um Pull Request no GitHub.