import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireFoxOption


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке необязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption('--headless', action='store_true', default=False,
                     help="Run browser without UI")


# Запуск браузера (для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    language = request.config.getoption('language')  # получаем параметр командной строки language
    headless = request.config.getoption('headless')  # запуск без окна браузера
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        options.enable_bidi = True  # WebSocket-канал BiDi: нужен для событий консоли и JS-ошибок
        # с BiDi браузер по умолчанию сразу закрывает alert, и тест не успевает его прочитать
        options.unhandled_prompt_behavior = "ignore"
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")  # в headless окно по умолчанию маленькое
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FireFoxOption()
        options.set_preference("intl.accept_languages", language)
        options.enable_bidi = True
        options.unhandled_prompt_behavior = "ignore"
        if headless:
            options.add_argument("-headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


# Проверка JS-ошибок на странице через WebDriver BiDi.
# Подключается явно: def test_x(browser, no_js_errors). Ошибки собираются во время теста,
# и если среди них есть неизвестные, тест падает на этапе teardown.
# Известные ошибки сайта можно пропустить: @pytest.mark.known_js_errors("oscar is not defined")
@pytest.fixture
def no_js_errors(request, browser):
    errors = []
    handler_id = browser.script.add_javascript_error_handler(lambda error: errors.append(error.text))
    yield errors
    browser.script.remove_javascript_error_handler(handler_id)
    marker = request.node.get_closest_marker("known_js_errors")
    known = marker.args if marker else ()
    unexpected = [error for error in errors if not any(text in error for text in known)]
    if unexpected:
        pytest.fail("JS errors on page:\n" + "\n".join(unexpected), pytrace=False)
