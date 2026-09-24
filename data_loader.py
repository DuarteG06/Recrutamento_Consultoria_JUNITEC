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


def get_expenses_policy() -> str:
    """Devolve a política de gastos da empresa que se encontra em expenses_policy.md"""
    filepath = os.path.join(DATA_DIR, "expenses_policy.md")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: Não foi possível localizar as políticas de gastos da empresa em expenses_policy."

def get_tasks() -> list:
    """Devolve todas as tarefas da empresa."""
    filepath = os.path.join(DATA_DIR, "tasks.json")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        return "Error: Não foi possível localizar as tarefas da empresa em tasks.json."

    return tasks

    






    
# adicionar mais funções aqui, por exemplo:
# def get_pending_tasks(employee_id: str) -> list:
#    ...