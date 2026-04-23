from clients.files.files_schema import (
    CreateFileRequestSchema,
    CreateFileResponseSchema,
    FileSchema,
    GetFileResponseSchema
)
from tools.assertions.base import assert_equal


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")


def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет корректность данных файла.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Проверяет, что данные файла при создании и запросе совпадают.

    :param get_file_response: Структура ответа получения файла с его данными.
    :param create_file_response: Структура ответа создания файла с его данными.
    :raises AssertionError: Если данные файла не совпадают.
    """
    assert_file(get_file_response.file, create_file_response.file)
