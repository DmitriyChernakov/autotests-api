import allure
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    @allure.step("Get user me")
    def get_user_me_api(self) -> Response:
        """
        Метод получает текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.USERS}/me")

    @allure.step("Get user by id {user_id}")
    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получает пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.USERS}/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод получает пользователя по идентификатору и возвращает декодированный ответ.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными пользователя.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"{APIRoutes.USERS}/{user_id}",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.USERS}/{user_id}")


def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PrivateUsersClient.
    """
    return PrivateUsersClient(client=get_private_http_client(user))
