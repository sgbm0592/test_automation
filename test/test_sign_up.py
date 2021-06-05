import pytest

from keywords.demo_blaze.home_actions import HomeActions
from keywords.demo_blaze.main_header_actions import MainHeaderActions
from keywords.demo_blaze.sing_actions import SingUpActions
from factory_driver import factory_driver
from utils_selenium import datafile_handler as data_file
driver = None


#Metodo que se ejecuta siempre, antes de cada caso de prueba.
#Crea la instancia del navegador
def setup():
    global driver
    driver = factory_driver.get_driver()


@pytest.mark.parametrize('title,username,password', data_file.get_data('./input_data/sign_options.csv'))
def test_sign_up_form(title, username, password):
    home_actions = HomeActions(driver)
    home_actions.click_on_home_option()

    main_header_actions = MainHeaderActions(driver)
    main_header_actions.verify_text_title(title)

    sing_actions = SingUpActions(driver)
    sing_actions.click_on_sign_option()
    sing_actions.fill_sign_form(username, password)


#Metodo que se ejecuta siempre, despues de cada caso de prueba.
#Cierra la instancia del navegador
def teardown():
    home_actions = HomeActions(driver)
    home_actions.save_screenshot()
    home_actions.close_browser()
