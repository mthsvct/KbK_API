# KbK_API

API do sistema de gestão de serviços. Para executar:

```bash
uvicorn src.server:app --reload --reload-dir=src
```

- `--reload`: para recarregar o servidor automaticamente.
- `--reload-dir=src`: para recarregar o servidor na pasta src.

Toda rota que precisa de Banco de dados precisa do Depends `get_db`.