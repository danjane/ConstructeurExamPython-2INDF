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
    f"\\question[3] Créez une variable appelée \\texttt{{{n}}} et attribuez-lui la valeur \\texttt{{{v}}}, "
    r" et puis écrire son type.\fillwithgrid{8mm}\fillwithdottedlines{10mm}"
    for n, v in zip(names, values)
]

latex_code = latex_code.replace("OTHERQUESTIONS", "".join(random.sample(basic_questions, 3)))

task_loop = random.choice([
    "de 1 à 5",
    "pairs de 2 à 10",
    "impairs de 1 à 9"
])
latex_code = latex_code.replace("TASKLOOP", task_loop)

print(latex_code)
latex_file = 'examen_python.tex'
with open(latex_file, 'w') as f:
    f.write(latex_code)
print(f"TeX generated and saved as {latex_file}")

pdf_file = 'examen_python.pdf'
pdf = build_pdf(latex_code)
pdf.save_to(pdf_file)

print(f"PDF generated and saved as {pdf_file}")
