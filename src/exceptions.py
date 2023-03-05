import enum

from fastapi import HTTPException
from starlette import status


@enum.unique
class ExceptionCode(str, enum.Enum):
    bad_request = "Bad Request"
    unauthorized = "Unauthorized"
    forbidden = "Forbidden"
    not_found = "Not Found"
    not_acceptable = "Not Acceptable"
    conflict = "Conflict"

    # 400
    old_pw_equal_to_new_pw = "the new password is equal to the old one"
    invalid_pw_reset_token = "token for password reset is invalid"

    # 401
    invalid_auth_token = "authentication token is invalid"
    incorrect_creds = "incorrect authentication credentials"
    incorrect_password = "incorrect password"

    # 403
    incorrect_reset_code = "code for password reset is incorrect"
    permission_denied = "no permissions to perform the action"

    # 404
    user_with_email_not_found = "user with this email not found"
    user_with_id_not_found = "user with this id not found"
    category_not_found = "category not found"
    project_not_found = "project not found"
    task_not_found = "task not found"

    # 406
    task_has_a_parent = "subtasks cannot have their own subtasks"
    deadline_in_past = "deadline cannot be set on a past date"

    # 409
    user_already_exists = "user with this email already exists"
    category_already_exists = "you already have a category with this name"
    project_already_exists = (
        "the category already has a project with this " "name"
    )
    task_already_exists = "the project already has a task with this name"
    subtask_already_exists = "the task already has a subtask with this name"


class ExceptionBase(HTTPException):
    status_code = None
    code: ExceptionCode | None = None
    detail = None

    def __init__(
        self,
        status_code: status = status_code,
        detail: str = detail,
        code: ExceptionCode = code,
    ):
        self.status_code = status_code
        self.detail = detail
        self.code = code


class BadRequestError(ExceptionBase):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Bad Request"
    code = ExceptionCode.bad_request

    def __init__(
        self, detail: str | dict = detail, code: ExceptionCode = code
    ):
        super().__init__(
            status_code=self.status_code, detail=detail, code=code
        )


class UnauthorizedError(ExceptionBase):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized"
    code = ExceptionCode.unauthorized

    def __init__(
        self, detail: str | dict | dict = detail, code: ExceptionCode = code
    ):
        super().__init__(
            status_code=self.status_code, detail=detail, code=code
        )


class ForbiddenError(ExceptionBase):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Forbidden"
    code = ExceptionCode.forbidden

    def __init__(
        self, detail: str | dict = detail, code: ExceptionCode = code
    ):
        super().__init__(
            status_code=self.status_code, detail=detail, code=code
        )


class NotFoundError(ExceptionBase):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Not Found"
    code = ExceptionCode.not_found

    def __init__(
        self, detail: str | dict = detail, code: ExceptionCode = code
    ):
        super().__init__(
            status_code=self.status_code, detail=detail, code=code
        )


class NotAcceptable(ExceptionBase):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    detail = "Not Acceptable"
    code = ExceptionCode.not_acceptable

    def __init__(
        self, detail: str | dict = detail, code: ExceptionCode = code
    ):
        super().__init__(
            status_code=self.status_code, detail=detail, code=code
        )


class ConflictError(ExceptionBase):
    status_code = status.HTTP_409_CONFLICT
    detail = "Conflict"
    code = ExceptionCode.conflict

    def __init__(
        self, detail: str | dict = detail, code: ExceptionCode = code
    ):
        super().__init__(
            status_code=self.status_code, detail=detail, code=code
        )
