from fastapi import HTTPException


def verificarObjeto(func):
    def wrapper(*args, **kwargs):
        if args[1] == None:
            return None
        instancia = args[0] # Instancia da Classe. Self
        obj = args[1] # Objeto a ser verificado. Id ou Email
        return func(instancia, obj)
    return wrapper
