import random

SHA_TILE_NUM = 108

def shagua(round: int):
    player_virus = [0, 0, 0, 0]
    palyer_recev_count = [0, 0, 0, 0]
    tile_virus = [0] * SHA_TILE_NUM

    first_player = random.randint(0, 3)
    
    infect_player = 0

    def handle_tile(player_index, tile_index):
        if player_index == infect_player:
            tile_virus[tile_index] = min(10, tile_virus[tile_index] + 1)
        else:
            player_virus[player_index] += tile_virus[tile_index]

    
    for i in range(round):
        tiles = list(range(SHA_TILE_NUM))
        random.shuffle(tiles)
        hands = [[] for _ in range(4)]
        
        # 初始发牌
        for player in range(4):
            hands[player] = [tiles.pop() for _ in range(13)]

        # 初始感染牌
        for t in hands[infect_player]:
            handle_tile(infect_player, t)

        current_player = first_player
        need_draw = True
        while(True):
            if need_draw:
                # 玩家需要抽牌
                new_tile = tiles.pop()
                hands[current_player].append(new_tile)
                handle_tile(current_player, new_tile)

            # 下面，玩家随机打出一张牌
            hand_num = len(hands[current_player])
            out_index = random.randrange(hand_num)    # 打出第几张牌
            out_tile = hands[current_player][out_index]  # 打出牌的牌面

            if random.random() < 0.5:
                # 有人接收
                # receiver = (current_player + random.randint(1, 3)) % 4
                # 接收概率为：3：2：2
                temp = random.randint(0, 6)
                if temp <= 2:
                    receiver = current_player + 1
                elif temp <= 4:
                    receiver = current_player + 2
                elif temp <= 6:
                    receiver = current_player + 3

                receiver = receiver % 4

                # 接收次数+1， 感染病毒， 加入手牌，设置下一轮的玩家，不需要抽牌
                palyer_recev_count[receiver] += 1
                handle_tile(receiver, out_tile)
                hands[receiver].append(out_tile)
                next_player = receiver
                need_draw = False

                # 接收达到4次，则游戏结束（认为胡牌）
                if palyer_recev_count[receiver] >= 4:
                    break
            else:
                # 无人接收
                next_player = (current_player + 1) % 4
                need_draw = True

            # 判断游戏结束
            # 1. 牌堆为空
            # 2. 有人接收达到4次
            if len(tiles) == 0:
                break
            
            # 处理下一轮：
            current_player = next_player
            
        # 轮流坐庄
        first_player = (first_player + 1) % 4

    return player_virus

# player_virus = [0, 0, 0, 0]

# for i in range(10000):
    
#     new_virus = shagua(4)
#     # print(new_virus)
#     for i in range(4):
#         player_virus[i] += new_virus[i]

# print(player_virus)

