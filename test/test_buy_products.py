import pytest

from keywords.demo_blaze.home_actions import HomeActions
from keywords.demo_blaze.main_header_actions import MainHeaderActions
from keywords.demo_blaze.prod_actions import ProdActions
from keywords.demo_blaze.categories_actions import CategoriesActions
from factory_driver import factory_driver, factory_driver_wait
from utils_selenium import datafile_handler as data_file
driver = None


#Metodo que se ejecuta siempre, antes de cada caso de prueba.
#Crea la instancia del navegador
def setup():
    global driver
    driver = factory_driver.get_driver()


@pytest.mark.parametrize('title, name, price', data_file.get_data('./input_data/phones_options.csv'))
def test_buy_phone(title, name, price):
    home_actions = HomeActions(driver)
    home_actions.click_on_home_option()

    main_header_actions = MainHeaderActions(driver)
    main_header_actions.verify_text_title(title)

    home_actions.click_prod_option(name)
    prod_actions = ProdActions(driver)
    prod_actions.click_on_prod_option(name, price)


@pytest.mark.parametrize('title, name, price', data_file.get_data('./input_data/laptops_options.csv'))
def test_buy_laptop(title, name, price):
    home_actions = HomeActions(driver)
    home_actions.click_on_home_option()

    main_header_actions = MainHeaderActions(driver)
    main_header_actions.verify_text_title(title)

    categories_actions = CategoriesActions(driver)
    categories_actions.verify_cat_title()
    categories_actions.click_on_laptops_option()

    home_actions.click_prod_option(name)
    prod_actions = ProdActions(driver)
    prod_actions.click_on_prod_option(name, price)

@pytest.mark.parametrize('title, name, price', data_file.get_data('./input_data/monitors_options.csv'))
def test_buy_monitor(title, name, price):
    home_actions = HomeActions(driver)
    home_actions.click_on_home_option()

    main_header_actions = MainHeaderActions(driver)
    main_header_actions.verify_text_title(title)

    categories_actions = CategoriesActions(driver)
    categories_actions.verify_cat_title()
    categories_actions.click_on_monitors_option()

    home_actions.click_prod_option(name)
    prod_actions = ProdActions(driver)
    prod_actions.click_on_prod_option(name, price)



#Metodo que se ejecuta siempre, despues de cada caso de prueba.
#Cierra la instancia del navegador
def teardown():
    home_actions = HomeActions(driver)
    home_actions.save_screenshot()
    home_actions.close_browser()
