from programming_language import ProgrammingLanguage

java = ProgrammingLanguage("Java", "Static", True, 1995)
c = ProgrammingLanguage("C++", "Static", False, 1983)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)

languages_list = [java, c, python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in languages_list:
    if language.is_dynamic():
        print(language.name)