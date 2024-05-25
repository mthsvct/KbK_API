from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from src.infra.sqlalchemy import repositorios as rp

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def obter_usuario_logado(
        token: str = Depends(oauth2_schema),
        session: Session = Depends(get_db)
    ):

    print("Passou aqui")

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido!"
    )

    try:
        email = token_provider.verificar_access_token(token)
        print("Email:", email)
    except JWTError:
        raise exception
    
    if not email:
        raise exception
    
    funcionario = rp.Funcionario(session).obterEmail(email)

    if not funcionario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Funcionário não encontrado!"
        )
    
    return funcionario



