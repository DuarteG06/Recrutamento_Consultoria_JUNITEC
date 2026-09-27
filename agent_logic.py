import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from data_loader import get_tasks,  get_employee_tasks, get_employees, get_expenses_policy, get_available_files, open_file

load_dotenv()


client = genai.Client()

system_instruction = (
    "És um Assistente de Operações Internas e RH de uma empresa em rápido crescimento. "
    "A tua função é ajudar com dúvidas de onboarding, gestão de tarefas e procurar informações de colaboradores usando as ferramentas que te foram fornecidas."
    "Estás a ser usado num CLI no terminal, não formates texto com bold e outros para não desformatar o output. Apenas newlines ou tabs que ajudem a ler o output, é preferível usar mias newlines para o texto ser legível em terminal."
)


config = types.GenerateContentConfig(
    system_instruction=system_instruction,
    tools=[get_tasks,  get_employee_tasks, get_employees, get_expenses_policy, get_available_files, open_file],
)


chat = client.chats.create(
    model="gemini-3.1-flash-lite",
    config=config
)

def send_message_stream(message):
    """
    O novo SDK tem um método nativo para streaming que funciona 
    perfeitamente em conjunto com as tools.
    """
    return chat.send_message_stream(message)