print("2016113519 유지훈")

def func(*args, **kwargs):
    for x in args:
        print(x)
    print('My Name :', kwargs["name"], ' & My Age :', kwargs["age"])
    
func(1, 2, 3, 4, name="Jihoon", age=25)