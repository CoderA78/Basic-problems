def funargs(normal_argument, *argsanup, **kwargsanup):
    print(normal_argument)
    for item in argsanup:
        print(item)
    print("Now I'd like to introduce you to some of our heroes:")
    for key, value in kwargsanup.items():
        print(f"{key} is a {value}"+".")
har=("Anup","Swarup","Arpita","Sunita")
normal_argument = ("This is an normal argument and the students are- ")
kw={"Anup":"Programmer","Swarup":"doctor", "Arpita":"Nutritionist", "Sunita":"Medical Technilogist"}
funargs(normal_argument, *har, **kw)
