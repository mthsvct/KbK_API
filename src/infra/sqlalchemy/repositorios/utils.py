from fastapi import HTTPException



def verificarObjeto(func):
    def wrapper(*args, **kwargs):
        if args[1] == None:
            return None
        instancia = args[0] # Instancia da Classe. Self
        obj = args[1] # Objeto a ser verificado. Id ou Email
        return func(instancia, obj)
    return wrapper

def busca(instancia, id):
    obj = instancia.obter(id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Objeto não encontrado!")
    return obj

def obterObjeto(func):
    def wrapper(*args, **kwargs):
        repo = args[0]
        id = args[1]
        if len(args) > 2:
            data = args[2]
        else:
            data = None
        obj = busca(repo, id)
        aux = func(repo, id, data, obj)
        repo.db.commit()
        return aux
    return wrapper

def buscaObjeto(func):
    def wrapper(*args, **kwargs):
        repo, id = args[0], args[1]
        obj = busca(repo, id)
        return func(repo, id, obj)
    return wrapper

