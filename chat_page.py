# chat_test/chat_page.py
from playwright.sync_api import Page


class ChatPage:
    def __init__(self, page: Page):
        self.page = page
        self.chat_widget_locator = ".widget-button"  # Замените на реальный селектор
        self.chat_window_locator = ".widget-chat"  # Замените на реальный селектор
        self.message_input_locator = "textarea[placeholder='Write a message']"  # Замените на реальный селектор
        self.send_button_locator = "button:has-text('Send')" # Замените на реальный селектор
        self.close_button_locator = ".close-button" # Замените на реальный селектор
        self.message_locator = ".message-text"  # Замените на реальный селектор

    def open_chat(self):
        self.page.locator(self.chat_widget_locator).click()

    def close_chat(self):
         self.page.locator(self.close_button_locator).click()

    def is_chat_open(self):
        return self.page.locator(self.chat_window_locator).is_visible()

    def enter_message(self, message):
        self.page.locator(self.message_input_locator).fill(message)

    def send_message(self):
        self.page.locator(self.send_button_locator).click()
    
    def get_last_message_text(self):
        return self.page.locator(f"{self.message_locator}:last-of-type").text_content()
    
    def get_chat_widget(self):
      return self.page.locator(self.chat_widget_locator)
    
    def get_chat_window(self):
        return self.page.locator(self.chat_window_locator)

    def is_chat_widget_visible(self):
      return self.get_chat_widget().is_visible()
