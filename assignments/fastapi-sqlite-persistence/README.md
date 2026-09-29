# 📘 Atividade: Persistência de Dados com SQLite e FastAPI

## 🎯 Objetivo

Substitua o armazenamento em memória da API de tarefas por um banco SQLite usando SQLModel. Você praticará modelagem de tabelas, sessões de banco de dados e operações CRUD que preservam os dados após reiniciar a aplicação.

## 📝 Tarefas

### 🛠️ Criar o modelo e configurar o banco de dados

#### Descrição
Comece pela API funcional em memória fornecida no código inicial. Instale SQLModel e configure um banco SQLite local para armazenar as tarefas.

Instale as dependências e inicie a API:

```bash
pip install fastapi uvicorn sqlmodel
python starter-code.py
```

#### Requisitos
O programa concluído deve:

- Definir um modelo SQLModel de tabela para tarefas com `id`, `title` e `completed`.
- Criar um engine para o arquivo SQLite `tasks.db` com `check_same_thread=False`.
- Criar a tabela ao iniciar a aplicação.
- Manter `GET /health` respondendo com `{"status": "ok"}`.

### 🛠️ Migrar criação e consulta de tarefas

#### Descrição
Substitua o acesso ao dicionário em memória por sessões SQLModel nas rotas de criação e consulta. Preserve os caminhos e formatos de resposta da API anterior.

#### Requisitos
O programa concluído deve:

- Usar uma sessão de banco de dados para cada operação e fechá-la ao terminar.
- Implementar `POST /tasks` persistindo a tarefa e retornando seu identificador.
- Implementar `GET /tasks` consultando as tarefas no SQLite.
- Manter o filtro opcional `completed` em `GET /tasks`.
- Implementar `GET /tasks/{task_id}` e retornar HTTP `404` quando a tarefa não existir.

### 🛠️ Persistir atualizações e exclusões

#### Descrição
Migre as rotas de atualização e exclusão para o banco de dados e confirme que a API mantém os registros entre reinicializações.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar uma tarefa existente no SQLite.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa do SQLite.
- Retornar HTTP `404` ao atualizar ou excluir um identificador inexistente.
- Não depender do dicionário em memória para armazenar tarefas.
- Demonstrar que uma tarefa criada continua disponível após reiniciar o servidor.
