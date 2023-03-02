from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src import responses
from src.api.utils import get_current_user
from src.responses import CHANGE_PASSWORD_RESPONSES
from src.domain.users.schemas import (ChangePassword, SignInForm, Token, User,
                                      UserCreate, UserHashPw, UserUpdate)
from src.domain.auth.services import AuthService
from src.domain.users.services import UserService

router = APIRouter()


@router.post(
    "/sign-up",
    response_model=Token,
    responses={409: {"model": responses.UserAlreadyExistsModel}},
)
async def sign_up(
    user_data: UserCreate, service: AuthService = Depends()
) -> Token:
    user = await service.user_service.register(user_data)
    return service.create_token(user.id)


@router.post(
    "/sign-in",
    response_model=Token,
    responses={401: {"model": responses.IncorrectCredsModel}},
)
async def sign_in(
    creds: SignInForm,
    service: AuthService = Depends(),
) -> Token:
    return await service.authenticate_user(creds.email, creds.password)


@router.post(
    "/sign-in-swagger",
    response_model=Token,
    responses={401: {"model": responses.IncorrectCredsModel}},
)
async def sign_in_swagger(
    # in fact there are email and password
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(),
) -> Token:
    return await service.authenticate_user(
        form_data.username, form_data.password
    )


@router.get(
    "/me",
    response_model=User,
    responses={
        401: {"model": responses.InvalidAuthTokenModel},
        # 404: {"model": responses.UserWithIdNotFoundModel}
    },
)
async def get_user(user: UserHashPw = Depends(get_current_user)) -> User:
    return User.from_orm(user)


@router.patch(
    "/change-password",
    response_model=User,
    responses={
        400: {"model": responses.EqualPasswordsModel},
        401: CHANGE_PASSWORD_RESPONSES,
        404: {"model": responses.UserWithIdNotFoundModel},
    },
)
async def change_password(
    change_password_data: ChangePassword,
    user: UserHashPw = Depends(get_current_user),
    service: UserService = Depends(),
) -> User:
    return await service.change_password(
        user=user, change_password_data=change_password_data
    )


@router.put(
    "/me",
    response_model=User,
    responses={
        401: {"model": responses.InvalidAuthTokenModel},
        404: {"model": responses.UserWithIdNotFoundModel},
        409: {"model": responses.UserAlreadyExistsModel},
    },
)
async def update_user(
    update_profile_data: UserUpdate,
    user: UserHashPw = Depends(get_current_user),
    service: UserService = Depends(),
) -> User:
    return await service.update_profile(
        user=user, update_profile_data=update_profile_data
    )
