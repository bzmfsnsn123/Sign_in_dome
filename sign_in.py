FILE="sign.txt"

def load_sign():
    sign_data={}
    try:
        with open(FILE,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                name,time=line.split("#")
                sign_data[name]=time

    except FileNotFoundError:
        pass
    return sign_data

def save_sign(data):
    with open(FILE,"w",encoding="utf-8") as f:
        for name,time in data.items():
            f.write(f"{name}#{time}\n")

def main():
    sign_list=load_sign()
    while True:
        print("\n=====学生签到系统======")
        print("1.学生签到")
        print("2.查看全部签到人员")
        print("3.查询某人是否签到")
        print("4.删除签到总人数")
        print("5.统计签到人数")
        print("0.退出程序")
        try:
            op=int(input("请输入功能序号："))
            if op==1:
                name=input("请输入功能序号：").strip()
                if name=="":
                    print("姓名不能为空！")
                    continue
                if name in sign_list:
                    print(f"{name}已经签到，签到时间{sign_list[name]}")
                    continue
                clock_time=input("输入签到时间：").strip()
                sign_list[name]=clock_time
                save_sign(sign_list)
                print("签到成功！")

            elif op==2:
                if not sign_list:
                    print("暂无签到记录")
                    continue
                print(f"\n{'姓名':<6}{'签到时间'}")
                print("-"*16)
                for name,time in sign_list.items():
                    print(f"{name:<6}{time}")

            elif op==3:
                find_name=input("输入要查询的姓名").strip()
                if find_name in sign_list:
                    print(f"{find_name}已签到，时间:{sign_list[find_name]}")
                else:
                    print(f"{find_name}未签到")

            elif op==4:
                del_name=input("输入要删除的姓名").strip()
                if del_name in sign_list:
                    print("无该签到记录")
                    continue
                del sign_list[del_name]
                save_sign(sign_list)
                print("记录已删除")

            elif op==5:
                total=len(sign_list)
                print(f"当前签到人数：{total}")

            elif op==0:
                print("程序退出，相关数据已保存")
                break

            else:
                print("请输入0-5有效数字")


        except ValueError:
            print("请输入数字")

if __name__ == "__main__":
    main()


