from pathlib import Path

import allure
from allure_commons.types import Severity
from selene import have


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Vadim Korolev")
@allure.feature("Регистрация")
@allure.story("Проверка заполнения формы регистрации")
def test_complete_todo(setup_browser):
    browser = setup_browser
    browser.driver.execute_script("document.body.style.zoom='90%'")
    with allure.step("Открыть форму"):
        browser.open('automation-practice-form/')
    with allure.step("Заполнить имя"):
        browser.element('#firstName').type('Vadim')
    with allure.step("Заполнить фамилию"):
        browser.element('#lastName').type('Korolev')
    with allure.step("Заполнить email"):
        browser.element('#userEmail').type('v@gmail.com')
    with allure.step("Заполнить пол"):
        browser.element('.custom-control-label').click()
    with allure.step("Заполнить номер телефона"):
        browser.element('#userNumber').type('7915141114')
    with allure.step("Заполнить дату рождения"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element(
            '[value="11"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="1998"]').click()
        browser.element('.react-datepicker__day--027').click()
    with allure.step("Заполнить изображение"):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/img.jpg')))
    with allure.step("Заполнить темы"):
        browser.element('#subjectsInput').type('Ph').press_enter()
    with allure.step("Заполнить хобби"):
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-2]').click()
    with allure.step("Заполнить текущий адрес"):
        browser.element("#currentAddress").type("Test, 65")
    with allure.step("Заполнить страну"):
        browser.element("#react-select-3-input").type("NCR").press_enter()
        browser.element("#react-select-4-input").type("Delhi").press_enter()
        browser.element('#submit').click()
    with allure.step("Проверить форму"):
        browser.element("#example-modal-sizes-title-lg").should(have.text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(have.exact_texts('Vadim Korolev', 'v@gmail.com', 'Male',
                                                                         '7915141114', '27 December,1998', 'Physics',
                                                                         'Sports, Reading',
                                                                         'img.jpg', 'Test, 65', 'NCR Delhi'))
