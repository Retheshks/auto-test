from argparse import ArgumentParser
from selenium.webdriver import Chrome, Firefox, Ie


def get_browser_instance():
    parser = ArgumentParser()
    parser.add_argument("--browser", default='chrome')
    parser.add_argument("--url", default='test')
    parser.add_argument('--env', default='windows')

    options, arg = parser.parse_known_args()
    browser = options.browser.lower()
    url_info = options.url.lower()
    env = options.env.lower()

    if browser == 'chrome':
        driver = Chrome('./browser-servers/chromedriver.exe')
    elif browser == 'firefox':
        driver = Chrome('./browser-servers/geckodriver.exe')
    elif browser == 'ie':
        driver = Ie('./browser-servers/iedriver.exe')
    else:
        print('------------------Error------------------')
        print('Select brower value peoperly using --browser with chrome/firefox/ie')
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url_info == 'prod':
        driver.get('https://demo.actitime.com/login.do')
    else:
        driver.get('http://localhost/login.do')
    return driver