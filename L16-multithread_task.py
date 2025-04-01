import threading

values = input("Enter the values: ").strip().split(",")
values = list(map(lambda x: int(x), values))

def get_max(list):
    print(max(list))

def get_min(list):
    print(min(list))

threadMaxValue = threading.Thread(target=get_max,args=(values,))
threadMinValue = threading.Thread(target=get_min,args=(values,))

threadMaxValue.start()
threadMinValue.start()

threadMaxValue.join()
threadMinValue.join()

print("Finished threads.")