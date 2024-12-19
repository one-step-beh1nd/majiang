import random

CHUAN_TILE_NUM = 108


def sichuan(round: int):
    player_virus = [0, 0, 0, 0]
    palyer_recev_count = [0, 0, 0, 0]

    tile_virus = [0] * CHUAN_TILE_NUM

    first_player = random.randint(0, 3)
    
    infect_player = 0

    def handle_tile(player_index, tile_index):
        if player_index == infect_player:
            tile_virus[tile_index] = min(10, tile_virus[tile_index] + 1)
        else:
            player_virus[player_index] += tile_virus[tile_index]

    
    for i in range(round):
        hu_player = [False, False, False, False]
        in_player = 4

        tiles = list(range(CHUAN_TILE_NUM))
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

            if random.random() < 0.4:
                # 有人接收
                # receiver = (current_player + random.randint(1, 3)) % 4

                temp = random.randint(1, in_player-1)
                
                false_count = 0

                for i in range(1, 4):
                    next = hu_player[(current_player+i) % 4]
                    if not next:
                        false_count += 1

                    if false_count == temp:
                        receiver = current_player + i

                receiver = receiver % 4

                # 接收次数+1， 感染病毒， 加入手牌，设置下一轮的玩家，不需要抽牌
                palyer_recev_count[receiver] += 1
                handle_tile(receiver, out_tile)
                hands[receiver].append(out_tile)
                next_player = receiver
                need_draw = False

                # 接收达到4次，则胡牌
                # if palyer_recev_count[receiver] >= 4:
                #     hu_player[receiver] = True
                #     in_player -= 1

                # if in_player <= 1:
                #     break

                if palyer_recev_count[receiver] >= 4:
                    break
            else:
                # 无人接收

                for i in range(1, 4):
                    next = hu_player[(current_player+i) % 4]
                    if not next:
                        next_player = (current_player + i) % 4
                        need_draw = True
                        break

            # 判断游戏结束
            # 1. 牌堆为空
            # 2. 三个人胡牌
            if len(tiles) == 0:
                break
            
            # 处理下一轮：
            current_player = next_player
            
        # 轮流坐庄
        first_player = (first_player + 1) % 4

    return player_virus



