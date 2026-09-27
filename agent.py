from rich.console import Console
from rich.panel import Panel
from agent_logic import send_message_stream

console = Console()

def main():
    console.print(Panel.fit("[bold blue]🤖 AI Agent - Operações Internas[/bold blue]", border_style="blue"))
    console.print("Escreve [bold red]'sair'[/bold red] para fechar o assistente.\n")

    while True:
        user_input = console.input("[bold green]Tu:[/bold green] ")
        
        if user_input.lower() in ['sair', 'exit', 'quit', 'adeus', 'bye']:
            console.print("[bold yellow]A encerrar o assistente... Até logo![/bold yellow]")
            break
            
        if not user_input.strip():
            continue

        console.print("[bold purple]Agent:[/bold purple] ", end="")
        
        try:
            response_stream = send_message_stream(user_input)

            for chunk in response_stream:
                if chunk.parts:
                    for part in chunk.parts:
                        if part.text:
                            console.print(part.text, end="")
            
            console.print("\n")
            
        except Exception as e:
            console.print(f"\n[bold red]Erro ao comunicar com a API:[/bold red] {e}\n")

if __name__ == "__main__":
    main()