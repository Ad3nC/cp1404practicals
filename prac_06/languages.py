from prac_06.programming_language import Programming


def main():
    ruby = Programming("Ruby", "Dynamic", True, 1995)
    python = Programming("Python", "Dynamic", True, 1991)
    visual_basic = Programming("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    for language in languages:
        if language.is_dynamic():
            print(language.name)








main()