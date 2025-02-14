# Car Rental

Este é um projeto em desenvolvimento que utiliza Django e React em uma aplicação de locadora de carros.

A ideia do projeto é permitir que usuários de nível cliente possam visualizar os carros disponíveis com informações
relevantes para o aluguel, alugar estes carros gerando um orçamento e cadastrando o aluguél, e também devolve-los.

Enquanto o usuário administrador herdará as funcionálidades do usuário cliente além de poder gerenciar toda base
de carros cadastrados, usuários cadastrados, e alugueis.

## Estrutura do Projeto

### car-rental-fullstack
- backend/
    - api/
        - migrations/
            - __init__.py
        - __init__.py
        - admin.py
        - apps.py
        - models.py
        - serializers.py
        - tests.py
        - urls.py
        - validators.py
    - backend/
        - __init__.py
        - asgi.py
        - settings.py
        - urls.py
        - wsgi.py
    - media/
        - car_image/
            - honda_civic.jpg
            - toyota_corolla.jpg
    - manage.py
    - requirements.txt
- frontend/
    - public/
        - (imagens, icones, etc.)
    - src/
        - assets/
            - (imagens, ícones, etc.)
        - components/
            - CarList.jsx
            - Form.jsx
            - LoadingIndicator.jsx
            - ProtectedRoute.jsx
        - pages/
            - CarPage.jsx
            - Login.jsx
            - NotFound.jsx
            - Register.jsx
        - styles/
            - Form.css
            - LoadingIndicator.css
        - api.js
        - App.jsx
        - constants.js
        - main.jsx
    - package.json
    - package-lock.json
    - .gitignore
    - eslint.config.js
    - index.html
    - README.md
    - vite.config.js
- .gitattributes
- .gitignore
- README.md

## Configuração do Backend

### Requisitos

- Python 3.x
- Django
- Django REST Framework
- Django CORS Headers
- Django REST Framework SimpleJWT
- Python-dotenv

### Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/LucaBendasoli/car-rental-fullstack.git
    cd backend
    ```

2. Navegue até o diretório backend:
    ```sh
    cd backend
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações:
    ```sh
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

## Configuração do Frontend

### Requisitos

- Node.js
- npm ou yarn

### Instalação

1. Navegue até o diretório frontend:
    ```sh
    cd frontend
    ```

2. Instale as dependências:
    ```sh
    npm install  # ou `yarn install`
    ```

3. Inicie o servidor de desenvolvimento:
    ```sh
    npm run dev  # ou `yarn dev`
    ```

## Funcionalidades (Desenvolvidas até o momento)

### Backend

- **Modelos**: Definição de modelos para Car com validações personalizadas.
- **Serializers**: Serialização de dados para os modelos.
- **Views**: Implementação de views para CRUD de carros e criação de usuários.
- **Autenticação**: Autenticação JWT utilizando SimpleJWT.
- **Permissões**: Utilização do atributo IsAdmin nativo dos usuários Django.

### Frontend

- **Páginas**: Páginas para login, registro, listagem de carros e página de erro 404.
- **Componentes**: Componentes reutilizáveis como CarList, LoadingIndicator e Form.
- **Roteamento**: Roteamento protegido com ProtectedRoute.
- **Estilos**: Estilização básica com CSS.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-nova-funcionalidade`
3. Faça suas alterações e commit: `git commit -m 'Adiciona nova funcionalidade'`
4. Envie para o repositório remoto: `git push origin minha-nova-funcionalidade`
5. Abra um Pull Request.
