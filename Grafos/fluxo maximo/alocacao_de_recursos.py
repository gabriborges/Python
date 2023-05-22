def alocar_professores(disciplinas):
    # Ordena as disciplinas com base na preferência dos professores
    disciplinas_ordenadas = sorted(disciplinas, key=lambda x: sum([preferencia for _, preferencia in x[1]]))

    # Inicializa uma lista vazia para armazenar as disciplinas alocadas para cada professor
    alocacao_professores = []

    # Itera sobre as disciplinas ordenadas
    for disciplina, preferencias in disciplinas_ordenadas:
        professor_preferido = None
        preferencia_preferido = float('inf')

        # Encontra o professor mais preferido que ainda não possui duas disciplinas alocadas
        for professor, preferencia in preferencias:
            if not any(disciplina == disc for prof, disc in alocacao_professores) and (professor_preferido is None or preferencia < preferencia_preferido):
                if sum(1 for prof, _ in alocacao_professores if prof == professor) < 2:
                    professor_preferido = professor
                    preferencia_preferido = preferencia

        # Atribui a disciplina ao professor encontrado
        if professor_preferido is not None:
            alocacao_professores.append((professor_preferido, disciplina))

    return alocacao_professores


# Define as disciplinas e preferências dos professores
disciplinas = [
    ("cc34", [("Francois", 1), ("Jorge", 4)]),
    ("cc45", [("Francois", 4), ("Jorge", 2)]),
    ("cc32", [("Francois", 2), ("Jorge", 1)]),
    ("cc03", [("Francois", 3), ("Jorge", 3), ("Fernando", 3), ("Josenilson", 2)]),
    ("cc17", [("Fernando", 4), ("Josenilson", 1)]),
    ("cc05", [("Fernando", 2), ("Josenilson", 3)]),
    ("cc22", [("Fernando", 1), ("Josenilson", 4)])
]

# Aloca professores para as disciplinas
alocacao = alocar_professores(disciplinas)

# Imprime os resultados da alocação
for professor, disciplina_atribuida in alocacao:
    print(f"O professor {professor} está atribuído à disciplina {disciplina_atribuida}")
