import keyboard
def bank():
    try: 
        account=[] 
        action_dict={
            "D":"",
            "M":"-"
        }
        while True:
            input_num=input("请输入存取数目并用空格分开:")
            if input_num == keyboard.on_press_key("q"):
                raise KeyboardInterrupt
                break
            number=action_dict.get(input_num.split(' ')[0])+input_num.split(' ')[1]
            account.append(number) 
    except KeyboardInterrupt:
        result=[int(i) for  i in account]
        print(f"总数为:{sum(result)}")
        print("end")
if __name__=="__main__":
    bank()