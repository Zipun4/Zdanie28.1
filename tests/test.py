import time

import pytest
from pages.auth import *
from pages.locators import *
from pages.settings import *

"""
python -m pytest -v --driver Chrome --driver-path chrDrive.exe tests/test.py
"""


# ТЕСТ авторизация по номеру тел., почте, логину, ЛС (с невалидными данными)
@pytest.mark.parametrize('username_form', [invalid_phone, invalid_email, invalid_login, invalid_LS],
                         ids=['invalid_phone & invalid_password',
                              'invalid_email & invalid_password',
                              'invalid_login & invalid_password',
                              'invalid_LS & invalid_password'])
def test_auth_page_invalid_data(browser, username_form):
    page = AuthPage(browser)
    page.enter_username(username_form)
    page.enter_password(password)
    time.sleep(15)  # при необходимости ввести текст с изображения в поле "Символы" и ждать продолжения работы теста
    page.btn_click_enter()

    # browser.implicitly_wait(2)
    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_message.text == 'Неверный логин или пароль' and page.check_color(forgot_pass) == '#ff4f12'  # Сообщение и изменение цвета ссылки "Забыл пароль"
    page.driver.save_screenshot('test_auth_page_invalid_data.png')


 # ТЕСТ авторизация по почте и паролю (валидная почта, невалидный пароль)
def test_auth_page_valid_email_invalid_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(invalid_password)
    time.sleep(15)  # при необходимости ввести текст с изображения в поле "Символы" и ждать продолжения работы теста
    page.btn_click_enter()
    browser.implicitly_wait(2)

    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_message.text == 'Неверный логин или пароль' and page.check_color(forgot_pass) == '#ff4f12' # Сообщение и изменение цвета ссылки "Забыл пароль"
    page.driver.save_screenshot('test_auth_valid_email_invalid_pass.png')


# ТЕСТ авторизация по почте и паролю (невалидная почта, валидный пароль)
def test_auth_page_invalid_email_valid_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(invalid_password)
    time.sleep(15)  # при необходимости ввести текст с изображения в поле "Символы" и ждать продолжения работы теста
    page.btn_click_enter()
    #browser.implicitly_wait(2)
    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_message.text == 'Неверный логин или пароль' and page.check_color(forgot_pass) == '#ff4f12'  # Сообщение и изменение цвета ссылки "Забыл пароль"
    page.driver.save_screenshot('test_auth_invalid_email_valid_pass.png')



# ТЕСТ авторизация по почте и паролю (валидные данные)
def test_auth_page_valid_email_valid_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    time.sleep(15)  # при необходимости ввести текст с изображения в поле "Символы" и ждать продолжения работы теста
    page.btn_click_enter()
    assert page.get_relative_link() == '/account_b2c/page'  # Переход в учетную запись
    page.driver.save_screenshot('test_auth_valid_email_valid_pass.png')


# ТЕСТ авторизация при пустых полях "Телефон" и "Пароль"
def test_auth_page_empty_phone_empty_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username('')
    page.enter_password('')
    page.btn_click_enter()
    error_message = browser.find_element(*AuthLocators.AUTH_MESS_EMPTY_PHONE)
    assert error_message.text == 'Введите номер телефона'  # Сообщение при пустом поле "Телефон" (при пустом пароле сообщения нет)
    page.driver.save_screenshot('test_empty_phone_empty_pass.png')


 # ТЕСТ кнопка перехода на страницу авторизации
def test_reg_page_button(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration' #переход на страницу регистрации пользователя
    page.driver.save_screenshot('test_reg_button.png')


# ТЕСТ кнопка аторизации через вк
def test_VK_button(browser):
    page = AuthPage(browser)
    page.enter_VK()
    assert page.get_relative_link() == '/authorize' #переход на страницу авторизации через соцесть
    page.driver.save_screenshot('test_VK_button.png')


# ТЕСТ кнопка аторизации через одноклассники
def test_OD_button(browser):
    page = AuthPage(browser)
    page.enter_OD()
    assert page.get_relative_link() == '/dk' #переход на страницу авторизации через соцесть
    page.driver.save_screenshot('test_OD_button.png')


 # ТЕСТ кнопка аторизации через mail.ru аккаунт
def test_MAIL_button(browser):
    page = AuthPage(browser)
    page.enter_MAIL()
    assert page.get_relative_link() == '/oauth/authorize' #переход на страницу авторизации через соцесть
    page.driver.save_screenshot('test_MAIL_button.png')


# ТЕСТ кнопка аторизации через google аккаунт
def test_GOOGLE_button(browser):
    page = AuthPage(browser)
    page.enter_GOOGLE()
    assert page.get_relative_link() == '/o/oauth2/auth/identifier' #переход на страницу авторизации через соцесть
    page.driver.save_screenshot('test_GOOGLE_button.png')


# ТЕСТ кнопка аторизации через Yandex аккаунт
def test_YANDEX_button(browser):
    page = AuthPage(browser)
    browser.implicitly_wait(10)
    page.enter_YANDEX()
    browser.implicitly_wait(10)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate' #переход на страницу авторизации через соцесть
    page.driver.save_screenshot('test_YANDEX_button.png')
    #при автотесте отображается базовая страница авторизации, при ручном показывается правильная страница авторизации через яндекс


# ТЕСТ переход на страницу восстановления пароля
def test_to_forgot_pass_page(browser):
    page = AuthPage(browser)
    page.enter_forgot_pass()
    browser.implicitly_wait(3)
    #page.enter_username(valid_email)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials' #переход на страницу восстановления пароля
    page.driver.save_screenshot('test_forgot_pass.png')
    #page.enter_back_from_forgot_pass()
    #assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials' #переход на страницу атворизации


#ТЕСТ регистрация по невалдному email
@pytest.mark.parametrize('email', ['', invalid_email, no_eng_email],
                         ids=['EMPTY_EMAIL', 'INVALID_EMAIL', 'NO_ENG_EMAIL'])
def test_registration_invalid_email(browser, email):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(2)
    page.enter_lastname(lastname)
    browser.implicitly_wait(2)
    page.enter_email(email)
    browser.implicitly_wait(2)
    page.enter_password(valid_password)
    browser.implicitly_wait(2)
    page.enter_pass_again(valid_password)
    browser.implicitly_wait(2)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'#Сообщение об ошибке
    #Отсутсвует сообщение об ошибке при вводе пустого email
    page.driver.save_screenshot('test_registration_invalid_email.png')


#ТЕСТ регистрация с невалдным паролем (короткий, длинный, пустой(пробел), вариации некорректных)
@pytest.mark.parametrize('password', ['', password20, short_pass, long_pass, incorrect_pass1,
                                      incorrect_pass2, incorrect_pass3],
                         ids=['EMPTY_PASS',
                              'password20',
                              'SHORT_PASS',
                              'LONG_PASS',
                              'incorrect_pass1',
                              'incorrect_pass2',
                              'incorrect_pass3'])
def test_registration_invalid_pass(browser, password):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(2)
    page.enter_lastname(lastname)
    browser.implicitly_wait(2)
    page.enter_email(valid_email)
    browser.implicitly_wait(2)
    page.enter_password(password)
    browser.implicitly_wait(2)
    page.enter_pass_again(password)
    browser.implicitly_wait(2)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Длина пароля должна быть не менее 8 символов' or 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or 'Длина' \
    ' пароля должна быть не более 20 символов' or 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or 'Пароль' \
    ' должен содержать хотя бы одну заглавную букву' or 'Пароль должен содержать хотя бы одну заглавную букву' #Сообщение об ошибке
    #Отсутсвует сообщение об ошибке при вводе пустого pass
    page.driver.save_screenshot('test_registration_invalid_pass.png')


#ТЕСТ регистрация с невалдным именем
@pytest.mark.parametrize('name', ['', short_name, long_name, no_rus_name, invalid_name, name31],
                         ids=['EMPTY_NAME', 'SHORT_NAME', 'LONG_NAME', 'NO_RUS_NAME', 'INVALID_NAME', 'NAME31'])
def test_registration_invalid_name(browser, name):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(2)
    page.enter_lastname(lastname)
    browser.implicitly_wait(2)
    page.enter_email(valid_email)
    browser.implicitly_wait(2)
    page.enter_password(valid_password)
    browser.implicitly_wait(2)
    page.enter_pass_again(valid_password)
    browser.implicitly_wait(2)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' #Сообщение об ошибке
    #Отсутсвует сообщение об ошибке при вводе пустого email
    page.driver.save_screenshot('test_registration_invalid_name.png')


#ТЕСТ регистрация с невалидной фамилией
@pytest.mark.parametrize('secondname', ['', short_name, long_name, no_rus_name, invalid_name, name31],
                         ids=['EMPTY_SECONDNAME', 'SHORT_SECONDNAME', 'LONG_SECONDNAME', 'NO_RUS_SECONDNAME', 'INVALID_SECONDNAME', 'SECONDNAMENAME31'])
def test_registration_invalid_secondname(browser, secondname):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(1)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(1)
    page.enter_lastname(secondname)
    browser.implicitly_wait(1)
    page.enter_email(valid_email)
    browser.implicitly_wait(1)
    page.enter_password(valid_password)
    browser.implicitly_wait(1)
    page.enter_pass_again(valid_password)
    browser.implicitly_wait(1)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' #Сообщение об ошибке
    #Отсутсвует сообщение об ошибке при вводе пустого email
    page.driver.save_screenshot('test_registration_invalid_secondname.png')


# ТЕСТ переход на страницу "Пользвательское соглашение"
def test_to_polz_sogl_page(browser):
    page = AuthPage(browser)
    page.enter_polz_sogl()
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth' #переход на страницу пользовательского соглашения
    browser.implicitly_wait(3)
    page.driver.save_screenshot('test_polz_sogl.png')


# ТЕСТ переход на страницу "Политика конфиденциальности"
def test_to_politics_page(browser):
    page = AuthPage(browser)
    page.enter_politics()
    page.driver.save_screenshot('test_pol_conf.png')
    browser.implicitly_wait(3)
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth' #переход на страницу пользовательского соглашения
    #ссылки "Политика конфиденциальности" и "Пользовательское соглашение" ведут на одну страницу



'''
@pytest.mark.parametrize('image_text_form', [invalid_text_image, empty_text_image],
                         ids=['valid_data & invalid_text_image',
                              'valid_data & empty_text_image'])#ТЕСТ авторизация по валидным почте и паролю с некорретным вводом текста с картинки
def test_auth_page_invalid_text_from_image(browser, image_text_form):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    browser.implicitly_wait(2)
    page.text_image(image_text_form) #ИЗОБРАЖЕНИЕ С ТЕКСТОМ ПОЯВЛЯЕТСЯ ПОСЛЕ НЕСКОЛЬКИХ НЕУДАЧНЫХ ПОПЫТОК АВТОРИЗАЦИИ
    browser.implicitly_wait(2)
    page.btn_click_enter()
    browser.implicitly_wait(2)

    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_message.text == 'Неверно введен текст с картинки'#Сообщение о неверно введенных символах с картинки
 # ЗАПУСК  python -m pytest -v --driver Chrome --driver-path chrDrive.exe tests/test.py
'''
