import json
import os

DATA_DIR = "data"

# O type hint (name: str) e a Docstring ("""...""") são OBRIGATÓRIOS 
# para o Gemini perceber quando e como usar esta função.
def get_employee_info(name: str) -> list:
    """Procura informações de um funcionário no sistema da empresa através do seu nome."""
    filepath = os.path.join(DATA_DIR, "employees.json")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            employees = json.load(file)
    except FileNotFoundError:
        return [{"error": "Ficheiro employees.json não encontrado."}]
    
    # Pesquisa ignorando maiúsculas/minúsculas
    results = [emp for emp in employees if name.lower() in emp.get("name", "").lower()]
    
    if not results:
        return [{"mensagem": f"Nenhum funcionário encontrado com o nome '{name}'."}]
    
    return results

def get_employees() -> list:
    """Devolve todas as informações de todos os trabalhadores em sistema."""
    filepath = os.path.join(DATA_DIR, "employees.json")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            employees = json.load(file)
    except FileNotFoundError:
        return [{"error": "Ficheiro employees.json não encontrado."}]
    return employees


def get_access_policy() -> str:
    """Devolve a access policy que se encontra em access_policy.md"""
    filepath = os.path.join(DATA_DIR, "access_policy.md")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: Não foi possível localizar as politicas da empresa em access_policy."





    
# adicionar mais funções aqui, por exemplo:
# def get_pending_tasks(employee_id: str) -> list:
#    ...