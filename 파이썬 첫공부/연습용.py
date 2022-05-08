def print_kwargs(**kwargs):  # **() : keysword argument // dictinonary의 형태
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은" + kwargs[k])
print(print_kwargs(a="int 조수", name="2"))