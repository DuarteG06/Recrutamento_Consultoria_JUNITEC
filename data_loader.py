import json
import os

DATA_DIR = "data"

def get_tasks() -> list:
    """Devolve todas as tarefas da empresa."""
    filepath = os.path.join(DATA_DIR, "tasks.json")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        return [{"Error: Não foi possível localizar as tarefas da empresa em tasks.json."}]

    return tasks

def get_employee_tasks(employee_id: str)-> list:
    """Devolve todas as tarefas de um trabalhador."""
    filepath = os.path.join(DATA_DIR, "tasks.json")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        return [{"Error: Não foi possível localizar as tarefas da empresa em tasks.json."}]

    employee_tasks = [task for task in tasks if employee_id == task.get("assignee_id", "")]

    if not employee_tasks:
        return [{"mensagem": f"Nenhuma tarefa encontrada para o trabalhador com id '{employee_id}'."}]

    return employee_tasks

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


def get_available_files() -> list:
    """Devolve uma lista com todos os ficheiros da empresa disponíveis."""
    try:
        return os.listdir(DATA_DIR)
    except FileNotFoundError:
        return ["Erro: A pasta de dados não foi encontrada."]

    

def open_file(filename: str) -> str:
    """Lê o ficheiro pedido e devolve o seu conteúdo."""

    filepath = os.path.join(DATA_DIR, filename)

    try:
        if filename.endswith(".json"):
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return json.dumps(data, indent=2, ensure_ascii=False)
        elif filename.endswith(".md") or filename.endswith(".txt"):
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            return f"Erro: Formato de ficheiro não suportado para '{filename}'."
    except FileNotFoundError:
        return f"Erro: O ficheiro '{filename}' não existe na pasta de dados."
      
    
