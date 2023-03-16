# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
# Bu öğrenci kayıt sistemine;
# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan 
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız) 
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.


studentList = []
def addStudent (nameSurname):
    studentList.append(nameSurname)
    print("Öğrenci eklemesi yapılmıştır...")

def deleteWithName (nameSurname):
    studentList.remove(nameSurname)

def addMoreThanOne ():
    howMany = int(input("Kaç adet öğrenci eklemesi yapılacak ?  "))
    count = 0
    while count < howMany:
        name = input("Kayıt olacak öğrenci adı ve soyadı:  ")
        studentList.append(name)
        print("Kayıt başarılı...")
        count+=1

def showAllStudents ():
    print("Öğrenci isim ve soyisimleri:  ")
    for i in range(len(studentList)):
        print(studentList[i])

def findStudentNumber (nameSurname):
    studentNumber =str(studentList.index(nameSurname))
    print("öğrencinin numarası: " + studentNumber)

def deleteMultiple ():
    howMany =int(input("Kaç adet öğrenci silinecek ?  "))
    count=0
    while count < howMany:
        name = input("Kayıt silinecek öğrenci adı ve soyadı:  ")
        studentList.remove(name)
        count+=1


addStudent("isa")
addStudent("yavuz")
showAllStudents()

print("**************************************************************************************************")

deleteWithName("yavuz")
showAllStudents()

print("**************************************************************************************************")

addMoreThanOne()
showAllStudents()

print("**************************************************************************************************")

findStudentNumber("isa")
showAllStudents()

print("**************************************************************************************************")

deleteMultiple()
showAllStudents()