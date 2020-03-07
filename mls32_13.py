# Попробуйте оформить тесты из первого модуля в стиле unittest.
#
# Возьмите тесты из шага - https://stepik.org/lesson/138920/step/11?unit=196194 Создайте новый файл Создайте в нем
# класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом Перепишите в
# стиле unittest тест для страницы http://suninjuly.github.io/registration1.html Перепишите в стиле unittest второй
# тест для страницы http://suninjuly.github.io/registration2.html Оформите финальные проверки в тестах в стиле
# unittest, например, используя проверочный метод assertEqual Запустите получившиеся тесты из файла Просмотрите отчёт
# о запуске и найдите последнюю строчку Отправьте эту строчку в качестве ответа на это задание Обратите внимание,
# что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали
# конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!
#
# Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного
# исключения.
#
# Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.

import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
	def test_in_first_page(self):
		URL = 'http://suninjuly.github.io/registration1.html'
		browser = webdriver.Chrome()
		browser.get(URL)
		browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys("Ivan")
		browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Petrov")
		browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("IP@kuku.ru")
		browser.find_element_by_css_selector("button.btn").click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test was failed")

	def test_in_second_page(self):
		URL = 'http://suninjuly.github.io/registration2.html'
		browser = webdriver.Chrome()
		browser.get(URL)
		browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys("Ivan")
		browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Petrov")
		browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("IP@kuku.ru")
		browser.find_element_by_css_selector("button.btn").click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test was failed")


if __name__ == "__main__":
	unittest.main()
