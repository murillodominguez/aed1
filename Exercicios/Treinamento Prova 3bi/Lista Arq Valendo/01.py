class Student:
    def __init__(self, nome, matricula, nota1, nota2, nota3):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.calc_media()
        self.calc_situacao()
    
    def calc_media(self):
        try:
            self.media = (float(self.nota1) + float(self.nota2) + float(self.nota3))/3
        except:
            self.media = ""
            print(f"As notas informadas para {self.nome} - {self.matricula} não puderam ser convertidas em número.")
    
    def calc_situacao(self):
        if isinstance(self.media, float):
            if self.media >= 7:
                self.situacao = 'Aprovado'
            else:
                self.situacao = 'Reprovado'
        else:
            self.situacao = 'Reprovado'
            
    
class CsvFile:
    def __init__(self, header, iterable):
        self.header = header
        self.iterable = iterable
        self.rows = []

    def create(self, filename):
        self._mount_rows()
        self._mount_content()
        if not self.content:
            raise ValueError("O conteúdo do arquivo está vazio. Execute _mount_content() antes.")
        with open(filename, 'w', encoding='latin-1') as file:
            file.write(self.content)

    def show_lines(self):
        print(self.content)

    def _mount_rows(self):
        self.rows.append(self.header)
        for item in self.iterable:
            row = f'{item.nome}={item.matricula}={item.nota1}={item.nota2}={item.nota3}={item.media}={item.situacao}'
            self.rows.append(row)

    def _mount_content(self):
        content = ''
        rows_length = len(self.rows)
        for i, row in enumerate(self.rows):
            content += row
            if i != rows_length - 1:
                content += "\n"

        self.content = content


def receive_student_data():
    nome = input("Informe o nome do aluno: (digite 0 para sair): ")
    if nome == '0':
        return nome
    matricula = input(f"Informe a matrícula do aluno {nome}: ")
    nota1 = input(f"Informe a nota de {nome} no primeiro bimestre: ")
    nota2 = input(f"Informe a nota de {nome} no segundo bimestre: ")
    nota3 = input(f"Informe a nota de {nome} no terceiro bimestre: ")

    student = Student(nome, matricula, nota1, nota2, nota3)

    return student

def has_minimum_students(student_list):
    if len(student_list) < 3:
        print('Informe no mínimo 3 estudantes.')
        return False
    return True

student_list = []

while True:
    student = receive_student_data()
    if student != '0':
        student_list.append(student)
        continue
    if not has_minimum_students(student_list):
        continue
    break

file = CsvFile('nome=matricula=n1=n2=n3=media=situacao', student_list)
file.create('example.csv')

file.show_lines()