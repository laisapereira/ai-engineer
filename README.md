# Case Técnico — Desenvolvedor de IA

## Servidor MCP com Persistência e Busca Vetorial
# MCP CRM Server

Servidor MCP que permite a agentes de IA interagir com um CRM inteligente. Usuários são armazenados no SQLite com suas descrições indexadas no FAISS para busca semântica via embeddings da OpenAI.

---

## Estrutura do Projeto

```
mcp-server/
├── server.py          # Tools MCP e inicialização do servidor
├── database.py        # Operações SQLite
├── embeddings.py      # Geração de embeddings via OpenAI
├── vector_store.py    # Índice FAISS
├── faiss_index/
│   └── index.bin      # Índice FAISS persistido em disco
├── user_database.db   # Banco SQLite
├── .env               # Variáveis de ambiente (não commitar)
└── pyproject.toml
```

---

## Pré-requisitos

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes escolhido)
- [Node.js](https://nodejs.org/) — necessário para o MCP Inspector
- Chave de API da OpenAI

---

## Instalação

```bash
git clone <url-do-repositorio>
cd mcp-server
uv sync
```

Crie o arquivo `.env`:

```env
OPENAI_API_KEY=sk-...
```

---

## Como rodar

```bash
uv run server.py
```

## Testando com MCP Inspector

```bash
npx @modelcontextprotocol/inspector "C:\Users\<SeuUsuario>\.local\bin\uv.exe" --directory "<caminho-do-projeto>" run server.py
```
Pois o inspector precisa de um proxy rodando localmente. Abra a URL gerada no browser para acessar a interface de testes.

<img width="1568" height="862" alt="image" src="https://github.com/user-attachments/assets/4c6638db-dd51-4199-97dc-2ca98afd65eb" />

Obs: Perceba o uso de "\\\" nos argumentos
---

## Tools

### `create_user`
Cria um usuário, gera embedding da descrição e indexa no FAISS.

```json
{ "id": 1, "name": "João Silva" }
```

### `search_users`
Busca usuários semanticamente similares a uma query. Recebe `query` e `top_k`.

```json
[
  {
    "id_user": 1,
    "nm_usuario": "João Silva",
    "email_usuario": "joao@email.com",
    "ds_usuario": "backend developer with Python expertise",
    "similarity_score": 0.42
  }
]
```

### `get_user`
Busca usuário por ID.

```json
{
  "id_user": 1,
  "nm_usuario": "João Silva",
  "email_usuario": "joao@email.com",
  "ds_usuario": "backend developer with Python expertise"
}
```

---

## Referências técnicas

| Item | Detalhe |
|------|---------|
| Modelo de embedding | `text-embedding-3-small` (OpenAI) — 1536 dimensões |
| Índice vetorial | FAISS `IndexFlatL2` — busca exata por distância euclidiana |
| Persistência FAISS | `faiss.write_index` — salvo em disco após cada inserção |
| **fastmcp** | `>=3.1.1` |
| **openai** | `>=2.29.0` |
| **faiss-cpu** | — |
| **numpy** | `>=2.4.3` |
| **python-dotenv** | `>=1.2.2` |
