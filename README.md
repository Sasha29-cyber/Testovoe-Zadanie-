Запуск тестов:

pytest chat_test/test_chat_frontend.py
Создадим файл test_chat_backend.py:

# chat_test/test_chat_backend.py
import asyncio
import aiohttp
import pytest

API_URL = "https://api.example.com/chat/send"  # Замените на реальный API endpoint

@pytest.mark.asyncio
async def test_send_message_backend():
    """Проверка отправки сообщения на backend"""
    message_data = {
        "user_id": "test_user",
        "message": "Test message from backend test",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json=message_data) as response:
           assert response.status == 200
           json_data = await response.json()
           assert json_data['status'] == 'success'
           assert json_data['message'] == 'message send'

@pytest.mark.asyncio
async def test_send_message_backend_without_text():
    """Проверка отправки сообщения без текста на backend"""
    message_data = {
        "user_id": "test_user",
        "message": "",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json=message_data) as response:
           assert response.status == 400
           json_data = await response.json()
           assert json_data['status'] == 'error'
           assert json_data['message'] == 'message is empty'

@pytest.mark.asyncio
async def test_send_message_backend_without_user():
    """Проверка отправки сообщения без user на backend"""
    message_data = {
        "message": "Test message from backend test",
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json=message_data) as response:
           assert response.status == 400
           json_data = await response.json()
           assert json_data['status'] == 'error'
           assert json_data['message'] == 'user id is missing'
Запуск тестов:

pytest chat_test/test_chat_backend.py
