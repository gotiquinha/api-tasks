# API de Gerenciamento de Tarefas (To-Do List) 📝

Uma API simples e fácil de usar para gerenciar suas tarefas diárias! Com ela, você pode criar, visualizar, atualizar e remover tarefas.

## 🚀 O que você pode fazer com esta API?

- ✅ Criar novas tarefas
- 📋 Ver todas as suas tarefas
- 🔍 Buscar uma tarefa específica
- ✏️ Atualizar tarefas existentes
- 🗑️ Remover tarefas
- ✨ Ver tarefas completadas

## 🛠️ Como Instalar e Rodar

### Pré-requisitos
- Python 3.x instalado no seu computador
- Conhecimento básico de terminal/linha de comando

### Passo a Passo

1. **Clone o projeto**
   ```bash
   git clone [URL_DO_SEU_REPOSITÓRIO]
   cd [NOME_DO_DIRETÓRIO]
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Rode a aplicação**
   ```bash
   python app.py
   ```

6. **Acesse a documentação**
   - Abra seu navegador
   - Digite: http://localhost:5000
   - Você será redirecionado para a documentação interativa

## 📖 Como Usar (Com Exemplos)

### 1. Criar uma Nova Tarefa
- Clique em `POST /tasks`
- Clique em "Try it out"
- Cole este exemplo:
  ```json
  {
    "title": "Estudar Python",
    "description": "Aprender sobre APIs com Flask"
  }
  ```
- Clique em "Execute"

### 2. Ver Todas as Tarefas
- Clique em `GET /tasks`
- Clique em "Try it out"
- Clique em "Execute"

### 3. Atualizar uma Tarefa
- Clique em `PUT /tasks/{task_id}`
- Clique em "Try it out"
- Digite o ID da tarefa
- Cole este exemplo para marcar como completada:
  ```json
  {
    "completed": true
  }
  ```
- Clique em "Execute"

### 4. Remover uma Tarefa
- Clique em `DELETE /tasks/{task_id}`
- Clique em "Try it out"
- Digite o ID da tarefa
- Clique em "Execute"

### 5. Ver Tarefas Completadas
- Clique em `GET /tasks/completed`
- Clique em "Try it out"
- Clique em "Execute"

## 📝 Estrutura de uma Tarefa

Quando você cria uma tarefa, ela fica assim:
```json
{
    "id": 0,
    "title": "Estudar Python",
    "description": "Aprender sobre APIs",
    "completed": false,
    "created_at": "2024-01-29T10:00:00",
    "updated_at": "2024-01-29T10:00:00"
}
```

- `id`: Número único da tarefa
- `title`: Título da tarefa (obrigatório)
- `description`: Descrição detalhada (opcional)
- `completed`: Se a tarefa está completa ou não
- `created_at`: Quando a tarefa foi criada
- `updated_at`: Última vez que a tarefa foi modificada

## ❓ Precisa de Ajuda?

Se encontrar algum problema ou tiver dúvidas:
1. Verifique se o servidor está rodando (terminal mostrando mensagens)
2. Confira se digitou o endereço correto no navegador
3. Certifique-se de que preencheu os dados corretamente

## 📚 Tecnologias Utilizadas

- Python 3.x
- Flask (Framework web)
- Swagger (Documentação interativa)
- JSON (Formato dos dados)

## Testes

Você pode testar a API usando ferramentas como:
- Postman
- cURL
- Insomnia
