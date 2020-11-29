def move(players, step):
    num = step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num - 1
    return players


def play(players, step, alive):
    list1 = [i for i in range(1,players + 1)]
    # 进入游戏循环，每次数到step淘汰，step之前的元素移动到列表末尾
    # 游戏结束的条件，列表剩余人数小于alive

    while len(list1) > alive:
        # 移动step前的元素到列表末尾
        list1 = move(list1, step)
        list1.pop(0)
    return list1


players = int(input("请输入参加游戏的人数"))
step = int(input("请输入淘汰的字数"))
alive = int(input("请输入幸存人数")
alive_list = play(players_num, step_num, alive_num)
print(alive_list)