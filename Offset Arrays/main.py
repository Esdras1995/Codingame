def transform_notation(notation):
    # Séparer la partie indices et la partie valeurs
    indices_part, values_part = notation.split('=')
    indices_range = indices_part.strip()[indices_part.index('[')+1:-1]  # Enlever 'A[' et ']'
    start_index, end_index = map(int, indices_range.split('..'))  # Obtenir les indices de début et de fin
    values = list(map(int, values_part.strip().split()))  # Obtenir les valeurs sous forme de liste d'entiers
    
    # Créer le dictionnaire
    result_dict = {i: values[i - start_index] for i in range(start_index, end_index + 1)}

    # Formater le résultat
    result_string = f"{notation[0:indices_part.index('[')]} = {result_dict}"
    return result_string

n = int(input())
for i in range(n):
    assignment = input()
    exec(transform_notation(assignment))
x = input()

print(eval(x))