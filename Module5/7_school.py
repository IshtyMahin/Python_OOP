
class Student:
    def __init__(self,name,id,current_class) -> None:
        self.name= name 
        self.id = id 
        self.current_class = current_class
        
    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class} , Id: {self.id
    }'
    
    
class Teacher:
    def __init__(self,name,subject,id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
        
    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'
    

class School:
    def __init__(self,name) -> None:
        self.name = name 
        self.teachers = []
        self.students = []
        
    def add_teacher(self,name,subject):
        id = len(self.teachers) +101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
        
    def enroll(self,name,fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students)+1
            student = Student(name,id,'C')
            self.students.append(student)
            return f'{name} is enrolled with id: {id},extra money {fee-6500}'
    
    def __repr__(self) -> str:
        print('Welcome to',self.name)
        print('---------OUR Teachers----------')
        for teacher in self.teachers:
            print(teacher)  
        print('---------OUR Students----------')
        for student in self.students:
            print(student)
            
        return 'All done for now'
    

phitron = School('Phitron')
phitron.enroll('Ishtiaq',7000)
phitron.enroll('Mahin',3456)
phitron.enroll("Maruf",2342543)
phitron.enroll('Miraj',7000)
phitron.enroll('Minhaj',7000)
phitron.enroll('Imtiaz',6500)


phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)