# Solução escolhida e implementada
A minha solução começou por focar-se em criar um agente que ajudasse na gestão de tarefas.
No entanto por concluir que a sua performance poderia ficar abaixo das minhas expectativas dedi-lhe funcionalidades extra a custo reduzido.

## Solução principal
O agente criado ligado ao gemini-2.5-flash através de uma API key tem acesso às seguintes funções:
- `get_tasks()` - Devolve todas as tasks atuais.
- `get_employee_tasks(name: str)` - Todas as tarefas de um certo trabalhador.
- `get_employees()` - Devolve todos os trabalhadores, usada quando se quer relacionar um trabalhador a uma tarefa.
- `get_expenses_policy()` - Devolve a politica de gastos pois algumas tarefas têm custos e o user pode querer algum tipo de explicação.


## Implementação extra
Após testar a funcionalidade do agente, considerei que em alguns casos poderia ser útil o agente conseguir ter acesso aos outros ficheiros, por exemplo ao onboarding.md pode ser útil para responder a questões sobre tarefas de onboarding.
Deste modo implementei as seguintes funções que apenas são usadas em casos limite quando o agente considera necessário:
- `get_available_files()` - Devolve todos os ficheiros devolvidos em data.
- `open_file(filename: str)` - Abre o ficheiro cujo nome é dado e devolve os seus dados.

Esta função de abrir qualquer ficheiro pelo nome só é usada em casos necessário, pois assim evitamos usar constatemente o get_available_files(), o que permite poupar tokens.

