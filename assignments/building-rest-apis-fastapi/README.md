# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para gerenciar tarefas, praticando rotas HTTP, modelos de dados, operações CRUD e filtros. Ao final, você poderá executar a API localmente e explorar sua documentação interativa.

## 📝 Tarefas

### 🛠️ Configurar a API e listar tarefas

#### Descrição
Instale FastAPI e Uvicorn, execute o código inicial e estenda a aplicação para representar e listar tarefas. Cada tarefa deve ter um identificador, um título e um estado de conclusão.

Para instalar as dependências e iniciar a aplicação:

```bash
pip install fastapi uvicorn
python starter-code.py
```

#### Requisitos
O programa concluído deve:

- Criar um modelo Pydantic para representar uma tarefa.
- Manter as tarefas em uma coleção em memória.
- Implementar `GET /tasks` para retornar todas as tarefas como JSON.
- Manter `GET /health` respondendo com `{"status": "ok"}`.
- Permitir explorar a documentação interativa em `http://127.0.0.1:8000/docs`.

### 🛠️ Implementar operações CRUD

#### Descrição
Adicione rotas para criar, consultar, atualizar e excluir tarefas. Use os identificadores das tarefas para acessar um item específico e retorne um erro HTTP apropriado quando ele não existir.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa e retornar o recurso criado com um identificador.
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica.
- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão.
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa.
- Retornar o status HTTP `404` ao consultar, atualizar ou excluir um identificador inexistente.

### 🛠️ Filtrar tarefas por estado

#### Descrição
Estenda a listagem para aceitar um filtro opcional pelo estado de conclusão, sem alterar o comportamento quando nenhum filtro for informado.

#### Requisitos
O programa concluído deve:

- Aceitar o parâmetro de consulta opcional `completed` em `GET /tasks`.
- Retornar somente as tarefas que correspondam ao filtro quando ele for informado.
- Continuar retornando todas as tarefas quando o parâmetro não for informado.
- Demonstrar os resultados usando `/docs` ou requisições para `GET /tasks?completed=true` e `GET /tasks?completed=false`.
