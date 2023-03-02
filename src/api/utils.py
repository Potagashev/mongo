from fastapi import Depends

from src.domain.users.schemas import User
from src.domain.auth.services import AuthService, oauth2_auth_token


async def get_current_user(
    token: str = Depends(oauth2_auth_token),
    service: AuthService = Depends(AuthService),
) -> User:
    return await service.validate_token(token)
