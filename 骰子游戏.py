import random

def simulate_games(total_games):
    # 1. 初始化记分牌
    wins_a = 0
    wins_b = 0
    
    print(f"--- 开始模拟 {total_games} 局游戏，请稍候... ---")

    # 2. 循环 10000 次
    for i in range(total_games):
        
        # 下面是一个单局游戏的逻辑 (和你刚才设计的一样)
        while True:
            roll_a = random.randint(1, 6)
            roll_b = random.randint(1, 6)
            
            # A 赢的条件 (A是6 且 B不是)
            if roll_a == 6 and roll_b != 6:
                wins_a += 1  # A得分
                break        # 这局结束，进入下一局
            
            # B 赢的条件 (B是6 且 A不是)
            elif roll_b == 6 and roll_a != 6:
                wins_b += 1  # B得分
                break        # 这局结束，进入下一局
                
            # 如果是平局 (都是6) 或者 没人扔到6
            # 代码会自动继续 while 循环，直到分出胜负

    # 3. 模拟结束，汇报结果
    print(f"\n=== 模拟结果 ({total_games} 局) ===")
    print(f"玩家 A 获胜: {wins_a} 次")
    print(f"玩家 B 获胜: {wins_b} 次")
    
    # 计算百分比
    rate_a = (wins_a / total_games) * 100
    rate_b = (wins_b / total_games) * 100
    print(f"胜率对比: A [{rate_a:.2f}%] vs B [{rate_b:.2f}%]")

    if abs(wins_a - wins_b) < (total_games * 0.02):
        print("\n结论: 结果非常接近！你的规则是公平的。")
    else:
        print("\n结论: 居然有显著偏差？可能代码逻辑有 Bug。")

# 运行模拟
if __name__ == "__main__":
    simulate_games(10000)