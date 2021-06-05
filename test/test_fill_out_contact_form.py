import pytest

from keywords.demo_blaze.home_actions import HomeActions
from keywords.demo_blaze.main_header_actions import MainHeaderActions
from keywords.demo_blaze.contact_actions import ContactActions
from factory_driver import factory_driver, factory_driver_wait
from utils_selenium import datafile_handler as data_file
driver = None


#Metodo que se ejecuta siempre, antes de cada caso de prueba.
#Crea la instancia del navegador
def setup():
    global driver
    driver = factory_driver.get_driver()


@pytest.mark.parametrize('title,option,name,email,message', data_file.get_data('./input_data/contact_options.csv'))
def test_fill_out_contact_form(title, option, name, email, message):
    home_actions = HomeActions(driver)
    home_actions.click_on_home_option()

    main_header_actions = MainHeaderActions(driver)
    main_header_actions.verify_text_title(title)

    contact_actions = ContactActions(driver)
    contact_actions.click_contact_option(option)
    contact_actions.fill_contact_form(name, email, message)



#Metodo que se ejecuta siempre, despues de cada caso de prueba.
#Cierra la instancia del navegador
def teardown():
    home_actions = HomeActions(driver)
    home_actions.save_screenshot()
    home_actions.close_browser()
