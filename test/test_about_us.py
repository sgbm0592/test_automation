import pytest

from keywords.demo_blaze.home_actions import HomeActions
from keywords.demo_blaze.main_header_actions import MainHeaderActions
from keywords.demo_blaze.about_actions import AboutActions
from factory_driver import factory_driver, factory_driver_wait
from utils_selenium import datafile_handler as data_file
driver = None


#Metodo que se ejecuta siempre, antes de cada caso de prueba.
#Crea la instancia del navegador
def setup():
    global driver
    driver = factory_driver.get_driver()


def test_about_us():
    home_actions = HomeActions(driver)
    home_actions.click_on_home_option()

    main_header_actions = MainHeaderActions(driver)
    main_header_actions.verify_text_title('PRODUCT STORE')

    about_actions = AboutActions(driver)
    about_actions.click_on_about_option()
    about_actions.click_on_play_option()


#Metodo que se ejecuta siempre, despues de cada caso de prueba.
#Cierra la instancia del navegador
def teardown():
    home_actions = HomeActions(driver)
    home_actions.save_screenshot()
    home_actions.close_browser()
