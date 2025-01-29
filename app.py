from flask import Flask, jsonify, request, redirect
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)

# Configuração mais específica do CORS
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Origin"],
        "expose_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Configuração do Swagger
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Gerenciamento de Tarefas"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Lista para armazenar as tarefas
tasks = []

@app.route('/')
def home():
    """Redireciona para a documentação."""
    return redirect('/docs')

@app.route('/static/swagger.json')
def swagger_spec():
    """Retorna a especificação Swagger da API."""
    return jsonify({
        "openapi": "3.0.0",
        "info": {
            "title": "API de Gerenciamento de Tarefas",
            "description": "Uma API simples para gerenciar tarefas (To-Do List)",
            "version": "1.0.0"
        },
        "servers": [
            {
                "url": "http://localhost:5000",
                "description": "Servidor de Desenvolvimento"
            }
        ],
        "paths": {
            "/tasks": {
                "get": {
                    "summary": "Lista todas as tarefas",
                    "responses": {
                        "200": {
                            "description": "Lista de tarefas retornada com sucesso"
                        }
                    }
                },
                "post": {
                    "summary": "Cria uma nova tarefa",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "title": {
                                            "type": "string",
                                            "description": "Título da tarefa"
                                        },
                                        "description": {
                                            "type": "string",
                                            "description": "Descrição da tarefa"
                                        }
                                    },
                                    "required": ["title"]
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {
                            "description": "Tarefa criada com sucesso"
                        },
                        "400": {
                            "description": "Dados inválidos"
                        }
                    }
                }
            },
            "/tasks/{task_id}": {
                "get": {
                    "summary": "Retorna uma tarefa específica",
                    "parameters": [
                        {
                            "name": "task_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Tarefa encontrada"
                        },
                        "404": {
                            "description": "Tarefa não encontrada"
                        }
                    }
                },
                "put": {
                    "summary": "Atualiza uma tarefa",
                    "parameters": [
                        {
                            "name": "task_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer"
                            }
                        }
                    ],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "title": {
                                            "type": "string"
                                        },
                                        "description": {
                                            "type": "string"
                                        },
                                        "completed": {
                                            "type": "boolean"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Tarefa atualizada com sucesso"
                        },
                        "404": {
                            "description": "Tarefa não encontrada"
                        }
                    }
                },
                "delete": {
                    "summary": "Remove uma tarefa",
                    "parameters": [
                        {
                            "name": "task_id",
                            "in": "path",
                            "required": True,
                            "schema": {
                                "type": "integer"
                            }
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Tarefa removida com sucesso"
                        },
                        "404": {
                            "description": "Tarefa não encontrada"
                        }
                    }
                }
            },
            "/tasks/completed": {
                "get": {
                    "summary": "Lista todas as tarefas completadas",
                    "responses": {
                        "200": {
                            "description": "Lista de tarefas completadas retornada com sucesso"
                        }
                    }
                }
            }
        }
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retorna todas as tarefas."""
    return jsonify({
        'tasks': tasks,
        'total': len(tasks)
    })

@app.route('/tasks', methods=['POST'])
def add_task():
    """Adiciona uma nova tarefa."""
    data = request.json
    
    if not data or 'title' not in data:
        return jsonify({'error': 'O título da tarefa é obrigatório'}), 400
    
    task = {
        'id': len(tasks),
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Retorna uma tarefa específica."""
    if 0 <= task_id < len(tasks):
        return jsonify(tasks[task_id])
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente."""
    if 0 <= task_id < len(tasks):
        data = request.json
        if not data:
            return jsonify({'error': 'Dados inválidos'}), 400
        
        task = tasks[task_id]
        task['title'] = data.get('title', task['title'])
        task['description'] = data.get('description', task['description'])
        task['completed'] = data.get('completed', task['completed'])
        task['updated_at'] = datetime.now().isoformat()
        
        return jsonify(task)
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Remove uma tarefa."""
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        # Atualiza os IDs das tarefas restantes
        for i, task in enumerate(tasks):
            task['id'] = i
        return jsonify(removed_task)
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/completed', methods=['GET'])
def get_completed_tasks():
    """Retorna todas as tarefas completadas."""
    completed = [task for task in tasks if task['completed']]
    return jsonify({
        'tasks': completed,
        'total': len(completed)
    })

if __name__ == '__main__':
    app.run(debug=True) 