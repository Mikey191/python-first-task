# создаем пустые списки для хранения информации о студентах
student_ivan = []
student_andrey = []
student_ruslan = []
student_arsen = []
result_list = []

# записываем информацию в списки с помощью input

#запрашиваем имя
name = input("Введите имя первого студента: ")
#добавляем имя в список
student_ivan.append(name)
#запрашиваем фамилию
second_name = input("Введите фамилию первого студента: ")
#добавляем фамилию в список
student_ivan.append(second_name)
#запрашиваем первую оценку
first_score = input("Введите первую оценку студента: ")
# добавить оценку в список
student_ivan.append(first_score)

#запрашиваем первую оценку
second_score = input("Введите вторую оценку студента: ")
# добавить оценку в список
student_ivan.append(second_score)

#запрашиваем первую оценку
third_score = input("Введите третью оценку студента: ")
# добавить оценку в список
student_ivan.append(third_score)

# находим среднюю оценку студента
avg_score_first_student = (int(first_score) + int(second_score) + int(third_score))/3
# добавляем среднюю оценку в список
student_ivan.append(avg_score_first_student)

# добавляем первого студента в результирующий массив
result_list.append(student_ivan)