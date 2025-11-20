import random

def simulation_with_cheat(total_games):
    wins_a = 0
    wins_b = 0
    
    # === 核心配置区 ===
    # 这里设置作弊力度。0.05 代表有 5% 的概率直接给 A 发一个 6
    # 建议设置在 0.01 (1%) 到 0.05 (5%) 之间，太高会被发现
    CHEAT_RATE = 0.05 
    # =================
    
    print(f"--- 正在进行 {total_games} 局模拟 (A 开启了作弊模式)... ---")

    for i in range(total_games):
        while True:
            # === 玩家 A 的回合 (植入后门) ===
            # 生成一个 0 到 1 之间的随机小数
            if random.random() < CHEAT_RATE:
                # 触发作弊！不管随机数是多少，强行变成 6
                roll_a = 6
                # (可选) 可以在这里偷偷打印日志，自己调试看
                # print("DEBUG: 上帝之手触发，强行改命！") 
            else:
                # 没触发作弊，正常扔
                roll_a = random.randint(1, 6)
            
            # === 玩家 B 的回合 (完全老实) ===
            roll_b = random.randint(1, 6)
            
            # === 判定逻辑 (和之前一样) ===
            if roll_a == 6 and roll_b != 6:
                wins_a += 1
                break
            elif roll_b == 6 and roll_a != 6:
                wins_b += 1
                break
            # 平局或都没扔到6，继续循环

    # 汇报结果
    print(f"\n=== 作弊模拟结果 (作弊率: {CHEAT_RATE*100}%) ===")
    print(f"玩家 A 获胜: {wins_a} 次")
    print(f"玩家 B 获胜: {wins_b} 次")
    
    rate_a = (wins_a / total_games) * 100
    rate_b = (wins_b / total_games) * 100
    print(f"胜率对比: A [{rate_a:.2f}%] vs B [{rate_b:.2f}%]")
    
    diff = wins_a - wins_b
    print(f"\n分析: A 比 B 多赢了 {diff} 局")
    if diff > 500:
        print(">>> 警告：偏差过大！玩家 B 可能会怀疑你在搞鬼！")
    else:
        print(">>> 完美：稍微赢了一点点，B 只会觉得自己今天运气不好。")

if __name__ == "__main__":
    simulation_with_cheat(10000)