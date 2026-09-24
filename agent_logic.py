import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from data_loader import get_employee_info, get_employees, get_access_policy

load_dotenv()

# Inicializa o cliente do novo SDK (ele procura a GEMINI_API_KEY automaticamente no .env)
client = genai.Client()

system_instruction = (
    "És um Assistente de Operações Internas e RH de uma empresa em rápido crescimento. "
    "A tua função é ajudar com dúvidas de onboarding, gestão de tarefas e procurar informações de colaboradores usando as ferramentas que te foram fornecidas."
    "Estás a ser usado num CLI no terminal, não formates texto com bold e outros para não desformatar o output. Apenas newlines ou tabs que ajudem a ler o output, é preferível usar mias newlines para o texto ser legível em terminal."
)

# A configuração agora é feita num objeto próprio
config = types.GenerateContentConfig(
    system_instruction=system_instruction,
    tools=[get_employee_info, get_employees, get_access_policy],
)

# Inicia a sessão de chat
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=config
)

def send_message_stream(message):
    """
    O novo SDK tem um método nativo para streaming que funciona 
    perfeitamente em conjunto com as tools.
    """
    return chat.send_message_stream(message)