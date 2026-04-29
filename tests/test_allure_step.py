import allure


@allure.step("Building API client")
def build_api_client():
    with allure.step("Get user authentication tokens"):
        ...

    with allure.step("Create new API client"):
        ...


@allure.step("Creating course with title {title}")
def create_course(title: str):
    ...


@allure.step("Deleting course")
def delete_course():
    ...


def test_feature():
    build_api_client()
    create_course(title="New Course 1")
    create_course(title="New Course 2")
    create_course(title="New Course 3")
    create_course(title="New Course 4")
    delete_course()
