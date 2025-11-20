import tkinter as tk  # 导入图形界面库
import random

# === 这里是幕后的逻辑处理 ===
def play_game():
    # 1. 模拟扔骰子
    num_a = random.randint(1, 6)
    num_b = random.randint(1, 6)
    
    # 2. 把结果更新到界面上的“大数字”上
    label_a_score.config(text=str(num_a))
    label_b_score.config(text=str(num_b))
    
    # 3. 判定胜负逻辑
    if num_a == 6 and num_b != 6:
        result_text.set("结果：玩家 A 获胜！")
        label_result.config(fg="red") # 赢了变成红色字
    elif num_b == 6 and num_a != 6:
        result_text.set("结果：玩家 B 获胜！")
        label_result.config(fg="blue") # 赢了变成蓝色字
    elif num_a == 6 and num_b == 6:
        result_text.set("结果：平局！两边都是 6！")
        label_result.config(fg="purple")
    else:
        result_text.set("结果：没人扔到 6，继续...")
        label_result.config(fg="black")

# === 下面是“搭建舞台”的代码 ===

# 1. 创建主窗口
window = tk.Tk()
window.title("骰子对决 v1.0")
window.geometry("400x300") # 设定窗口大小

# 2. 创建顶部的标题
header = tk.Label(window, text="谁先扔到 6 谁就赢", font=("Arial", 16, "bold"))
header.pack(pady=20) # pady 是垂直间距

# 3. 创建显示分数的区域 (用一个容器 Frame 把它们包起来)
frame_scores = tk.Frame(window)
frame_scores.pack(pady=10)

# 玩家 A 的显示区
label_a_name = tk.Label(frame_scores, text="玩家 A", font=("Arial", 12))
label_a_name.grid(row=0, column=0, padx=30)
label_a_score = tk.Label(frame_scores, text="?", font=("Arial", 36, "bold"), fg="red")
label_a_score.grid(row=1, column=0)

# 中间的 VS
label_vs = tk.Label(frame_scores, text="VS", font=("Arial", 12))
label_vs.grid(row=1, column=1)

# 玩家 B 的显示区
label_b_name = tk.Label(frame_scores, text="玩家 B", font=("Arial", 12))
label_b_name.grid(row=0, column=2, padx=30)
label_b_score = tk.Label(frame_scores, text="?", font=("Arial", 36, "bold"), fg="blue")
label_b_score.grid(row=1, column=2)

# 4. 创建结果显示栏
result_text = tk.StringVar() # 创建一个特殊的变量，方便后续修改文字
result_text.set("准备开始...")
label_result = tk.Label(window, textvariable=result_text, font=("Arial", 12))
label_result.pack(pady=20)

# 5. 创建控制按钮
# 注意：command=play_game 意思就是“点我，就去执行 play_game 这个函数”
btn_play = tk.Button(window, text="🎲 扔骰子！", font=("Arial", 14), bg="#DDDDDD", command=play_game)
btn_play.pack(ipadx=20, ipady=5)

# 6. 启动程序，进入“等待事件”的无限循环
window.mainloop()