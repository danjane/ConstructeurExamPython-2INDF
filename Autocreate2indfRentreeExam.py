import random
from latex import build_pdf

with open('2indfRentreeBlankExam.tex', 'r') as f:
    latex_code = f.read()

for i, variable in enumerate(random.sample("rstwxyz", 3)):
    latex_code = latex_code.replace(f"VARIABLE{i}", variable)
latex_code = latex_code.replace("BIGINT", str(random.randint(5, 10)))
latex_code = latex_code.replace("SMALLINT", str(random.randint(1, 5)))
latex_code = latex_code.replace("PM", random.choice("+-"))

names = random.sample("abcdef", 3)
values = [random.randint(1, 10), random.randint(2, 8) + 0.5, random.choice(["True", "False"])]
basic_questions = [
    f"\\question[2] Affectez la valeur \\texttt{{{v}}} à une variable nommé \\texttt{{{n}}}."
    f"\n\\fillwithgrid{{14mm}}"
    f'\nQuel est le type de la variable :\\dotfill'
    for n, v in zip(names, values)
]

latex_code = latex_code.replace("AFFECTATIONQUESTIONS", "".join(random.sample(basic_questions, 3)))

task_loops = random.sample([
    "les nombres de 1 à 50",
    "les nombres pairs de 2 à 100",
    "les nombres impairs de 1 à 499",
    "les multiples de 5 de 5 à 1005",
    "les multiples positifs de 13 moins que 5000",
    "les entiers décroissants de 50 à 1",
    "les entiers décroissants de 200 à 0",
], 2)
latex_code = latex_code.replace("TASKLOOP1", task_loops[0])
latex_code = latex_code.replace("TASKLOOP2", task_loops[1])

task_conditions = random.choice([
    ["le groupe d'âge d'une personne",
     "`Enfant' si son âge est inférieur à 13",
     "`Adolescent' si son âge est entre 13 et 17",
     "`Adulte' si son âge est 18 ou plus",
     "age"],

    ["la catégorie d'un prix",
     "`Bon marché' si son prix est inférieur à 10",
     "`Moyen' si son prix est entre 10 et 100",
     "`Cher' si son prix est supérieur à 100",
     "prix"],

    ["la taille d'un animal",
     "`Petit' si son poids est inférieur à 5",
     "`Moyen' si son poids est entre 5 et 20",
     "`Grand' si son poids est supérieur à 20",
     "poids"],

    ["le niveau de compétence d'un joueur",
     "`Débutant' si son score est inférieur à 1000",
     "`Intermédiaire' si son score est entre 1000 et 5000",
     "`Expert' si son score est supérieur à 5000",
     "score"],

    ["l'évaluation d'un élève",
     "`Insuffisant' si la note est inférieure à 4",
     "`Bon' si la note est entre 4 et 5,5",
     "`Excellent' si la note est supérieure à 5,5",
     "note"],

    ["le niveau de risque d'une entreprise",
     "`Faible risque' si la dette est inférieure à 100000",
     "`Risque moyen' si la dette est entre 100000 et 500000",
     "`Haut risque' si la dette est supérieure à 500000",
     "dette"],

    ["la vitesse d'un véhicule",
     "`Lent' si la vitesse est inférieure à 30",
     "`Modéré' si la vitesse est entre 30 et 100",
     "`Rapide' si la vitesse est supérieure à 100",
     "vitesse"],

    ["la catégorie d'une température",
     "`Froid' si la température est inférieure à 5",
     "`Tempéré' si la température est entre 5 et 28",
     "`Chaud' si la température est supérieure à 28",
     "temp"]
])

for i, key_word in enumerate(["TASKCONDITIONNELLE", "TASKC1", "TASKC2", "TASKC3", "TASKVAR"]):
    latex_code = latex_code.replace(key_word, task_conditions[i])

names = ["Harry", "Hermione", "Ron", "Drago", "Neville", "Ginny", "Luna", "Cedric"]
chosens = random.sample(names, 4)
for i, name in enumerate(chosens):
    latex_code = latex_code.replace(f'NAME{i}', name)
for i, name in enumerate(random.sample(names, 2)):
    latex_code = latex_code.replace(f'TEST{i}', name)

latex_code = latex_code.replace('NAMEREPLACED', random.choice(chosens))
latex_code = latex_code.replace('NIEME', random.choice(
    ["premier", "deuxième", "troisième", "quatrième"]))

print(latex_code)
latex_file = 'examen_python.tex'
with open(latex_file, 'w') as f:
    f.write(latex_code)
print(f"TeX generated and saved as {latex_file}")

pdf_file = 'examen_python.pdf'
pdf = build_pdf(latex_code)
pdf.save_to(pdf_file)

print(f"PDF generated and saved as {pdf_file}")
