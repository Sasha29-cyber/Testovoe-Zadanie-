# chat_test/test_chat_frontend.py
import pytest
from playwright.sync_api import Page
from chat_page import ChatPage

URL = "https://autofaq.ai"

@pytest.fixture(scope="function")
def chat_page(page: Page):
  page.goto(URL)
  return ChatPage(page)

def test_chat_widget_visibility(chat_page: ChatPage):
    """Проверка видимости виджета чата"""
    assert chat_page.is_chat_widget_visible()

def test_chat_opens_on_click(chat_page: ChatPage):
    """Проверка открытия чата при клике на виджет"""
    chat_page.open_chat()
    assert chat_page.is_chat_open()

def test_chat_closes_on_click(chat_page: ChatPage):
     """Проверка закрытия чата при клике на кнопку закрытия"""
     chat_page.open_chat()
     chat_page.close_chat()
     assert not chat_page.is_chat_open()

def test_send_message(chat_page: ChatPage):
    """Проверка отправки сообщения и его отображения в чате"""
    chat_page.open_chat()
    message = "test message"
    chat_page.enter_message(message)
    chat_page.send_message()
    assert chat_page.get_last_message_text() == message

def test_input_is_empty_after_message_send(chat_page: ChatPage):
    """Проверка, что поле ввода становится пустым после отправки сообщения"""
    chat_page.open_chat()
    message = "test message"
    chat_page.enter_message(message)
    chat_page.send_message()
    message_input_text = chat_page.page.locator(chat_page.message_input_locator).input_value()
    assert  message_input_text == ""
