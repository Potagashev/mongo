from pydantic import BaseModel, Field

from src.exceptions import ExceptionCode


class DetailModel(BaseModel):
    msg: str
    code: str


class BadResponse(BaseModel):
    detail: DetailModel


invalid_auth_token = DetailModel(
    msg=ExceptionCode.invalid_auth_token,
    code=ExceptionCode.invalid_auth_token,
)


class InvalidAuthTokenModel(BadResponse):
    detail: DetailModel = Field(
        example=invalid_auth_token, default=invalid_auth_token
    )


user_with_id_not_found = DetailModel(
    msg=ExceptionCode.user_with_id_not_found,
    code=ExceptionCode.user_with_id_not_found,
)


class UserWithIdNotFoundModel(BadResponse):
    detail: DetailModel = Field(
        example=user_with_id_not_found, default=user_with_id_not_found
    )


user_already_exists = DetailModel(
    msg=ExceptionCode.user_already_exists,
    code=ExceptionCode.user_already_exists,
)


class UserAlreadyExistsModel(BadResponse):
    detail: DetailModel = Field(
        example=user_already_exists, default=user_already_exists
    )


user_with_email_not_found = DetailModel(
    msg=ExceptionCode.user_with_email_not_found,
    code=ExceptionCode.user_with_email_not_found,
)


class UserWithEmailNotFoundModel(BadResponse):
    detail: DetailModel = Field(
        example=user_with_email_not_found, default=user_with_email_not_found
    )


incorrect_password = DetailModel(
    msg=ExceptionCode.incorrect_password,
    code=ExceptionCode.incorrect_password,
)


class IncorrectPasswordModel(BadResponse):
    detail: DetailModel = Field(
        example=incorrect_password, default=incorrect_password
    )


invalid_pw_reset_token = DetailModel(
    msg=ExceptionCode.invalid_pw_reset_token,
    code=ExceptionCode.invalid_pw_reset_token,
)


class InvalidPasswordResetTokenModel(BadResponse):
    detail: DetailModel = Field(
        example=invalid_pw_reset_token, default=invalid_pw_reset_token
    )


incorrect_creds = DetailModel(
    msg=ExceptionCode.incorrect_creds,
    code=ExceptionCode.incorrect_creds,
)


class IncorrectCredsModel(BadResponse):
    detail: DetailModel = Field(
        example=incorrect_creds, default=incorrect_creds
    )


incorrect_reset_code = DetailModel(
    msg=ExceptionCode.incorrect_reset_code,
    code=ExceptionCode.incorrect_reset_code,
)


class IncorrectResetCodeModel(BadResponse):
    detail: DetailModel = Field(
        example=incorrect_reset_code, default=incorrect_reset_code
    )


permission_denied = DetailModel(
    msg=ExceptionCode.permission_denied,
    code=ExceptionCode.permission_denied,
)


class PermissionDeniedModel(BadResponse):
    detail: DetailModel = Field(
        example=permission_denied, default=permission_denied
    )


category_not_found = DetailModel(
    msg=ExceptionCode.category_not_found,
    code=ExceptionCode.category_not_found,
)


class CategoryNotFoundModel(BadResponse):
    detail: DetailModel = Field(
        example=category_not_found, default=category_not_found
    )


category_already_exists = DetailModel(
    msg=ExceptionCode.category_already_exists,
    code=ExceptionCode.category_already_exists,
)


class CategoryAlreadyExistsModel(BadResponse):
    detail: DetailModel = Field(
        example=category_already_exists, default=category_already_exists
    )


project_not_found = DetailModel(
    msg=ExceptionCode.project_not_found,
    code=ExceptionCode.project_not_found,
)


class ProjectNotFoundModel(BadResponse):
    detail: DetailModel = Field(
        example=project_not_found, default=project_not_found
    )


project_already_exists = DetailModel(
    msg=ExceptionCode.project_already_exists,
    code=ExceptionCode.project_already_exists,
)


class ProjectAlreadyExistsModel(BadResponse):
    detail: DetailModel = Field(
        example=project_already_exists, default=project_already_exists
    )


task_not_found = DetailModel(
    msg=ExceptionCode.task_not_found,
    code=ExceptionCode.task_not_found,
)


class TaskNotFoundModel(BadResponse):
    detail: DetailModel = Field(example=task_not_found, default=task_not_found)


task_has_a_parent = DetailModel(
    msg=ExceptionCode.task_has_a_parent,
    code=ExceptionCode.task_has_a_parent,
)


class TaskHasAParentModel(BadResponse):
    detail: DetailModel = Field(
        example=task_has_a_parent, default=task_has_a_parent
    )


task_already_exists = DetailModel(
    msg=ExceptionCode.task_already_exists,
    code=ExceptionCode.task_already_exists,
)


class TaskAlreadyExistsModel(BadResponse):
    detail: DetailModel = Field(
        example=task_already_exists, default=task_already_exists
    )


subtask_already_exists = DetailModel(
    msg=ExceptionCode.subtask_already_exists,
    code=ExceptionCode.subtask_already_exists,
)


class SubtaskAlreadyExistsModel(BadResponse):
    detail: DetailModel = Field(
        example=subtask_already_exists, default=subtask_already_exists
    )


deadline_in_past = DetailModel(
    msg=ExceptionCode.deadline_in_past,
    code=ExceptionCode.deadline_in_past,
)


class DeadlineInPastModel(BadResponse):
    detail: DetailModel = Field(
        example=deadline_in_past, default=deadline_in_past
    )


old_pw_equal_to_new_pw = DetailModel(
    msg=ExceptionCode.old_pw_equal_to_new_pw,
    code=ExceptionCode.old_pw_equal_to_new_pw,
)


class EqualPasswordsModel(BadResponse):
    detail: DetailModel = Field(
        example=old_pw_equal_to_new_pw, default=old_pw_equal_to_new_pw
    )


CATEG_AND_USER_NOT_FOUND_RESPONSES = {
    "description": "Not found",
    "content": {
        "application/json": {
            "examples": {
                "Category not found": {
                    "summary": "Category not found",
                    "value": CategoryNotFoundModel(),
                },
                "User Not Found": {
                    "summary": "User not found",
                    "value": InvalidAuthTokenModel(),
                },
            }
        }
    },
}

PROJ_AND_USER_NOT_FOUND_RESPONSES = {
    "description": "Not found",
    "content": {
        "application/json": {
            "examples": {
                "Project not found": {
                    "summary": "Project not found",
                    "value": ProjectNotFoundModel(),
                },
                "User Not Found": {
                    "summary": "User not found",
                    "value": UserWithIdNotFoundModel(),
                },
            }
        }
    },
}

TASK_AND_USER_NOT_FOUND_RESPONSES = {
    "description": "Not found",
    "content": {
        "application/json": {
            "examples": {
                "Task not found": {
                    "summary": "Task not found",
                    "value": TaskNotFoundModel(),
                },
                "User Not Found": {
                    "summary": "User not found",
                    "value": UserWithIdNotFoundModel(),
                },
            }
        }
    },
}

INVALID_DEADLINE_AND_TASK_HAS_A_PARENT = {
    "description": "Not Acceptable",
    "content": {
        "application/json": {
            "examples": {
                "The task has a parent task": {
                    "summary": "You cannot create a subtask for another "
                    "subtask",
                    "value": TaskHasAParentModel(),
                },
                "Invalid deadline": {
                    "summary": "Deadline of the task cannot be set on a past "
                    "date",
                    "value": DeadlineInPastModel(),
                },
            }
        }
    },
}

CHANGE_PASSWORD_RESPONSES = {
    "description": "Unauthorized",
    "content": {
        "application/json": {
            "examples": {
                "Incorrect password": {
                    "summary": "Incorrect password",
                    "value": IncorrectPasswordModel(),
                },
                "Invalid auth token": {
                    "summary": "Invalid auth token",
                    "value": InvalidAuthTokenModel(),
                },
            }
        }
    },
}
