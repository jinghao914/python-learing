import cv2

# === 1. 打开摄像头 ===
# 参数 0 表示默认摄像头。如果你有多个摄像头，可以是 1, 2...
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("错误：无法打开摄像头。请检查摄像头是否连接或被其他程序占用。")
    exit()

print("--- 摄像头已启动，按 'q' 键退出 ---")

# === 2. 循环读取视频帧 ===
while True:
    # `ret` 是一个布尔值，表示是否成功读取帧
    # `frame` 就是当前捕获到的图片 (一个数字矩阵！)
    ret, frame = cap.read()

    if not ret:
        print("错误：无法从摄像头接收帧（可能流结束）。")
        break

    # === 3. 对每一帧图片进行实时处理 (这里是核心) ===
    # 我们可以尝试各种滤镜。
    
    # --- 滤镜选项 1: 黑白效果 (最简单) ---
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR) # 如果转成灰度，要再转回来才能显示彩色方块

    # --- 滤镜选项 2: 边缘检测 (像素描，或黑客帝国) ---
    # Canny 算法可以找到图片中亮度变化剧烈的地方（也就是物体的边缘）
    frame = cv2.Canny(frame, 100, 200) # 100, 200 是阈值，可以调整玩玩看
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR) # Canny 输出是灰度图，为了显示要转回三通道

    # --- 滤镜选项 3: 实时反色 (像底片) ---
    # frame = 255 - frame 

    # --- 滤镜选项 4: 模糊效果 ---
    # frame = cv2.GaussianBlur(frame, (21, 21), 0) # (21, 21) 是模糊的程度，越大越糊

    # === 4. 在窗口中显示处理后的帧 ===
    cv2.imshow('Live Camera Feed with Filter', frame)

    # === 5. 检测用户是否按下 'q' 键 ===
    # waitKey(1) 表示等待 1 毫秒。如果在这 1 毫秒内按下了键，它就会返回按下的键的 ASCII 值。
    # 0xFF 是一个掩码，用于确保只比较 ASCII 值的低 8 位。
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === 6. 释放摄像头资源并关闭所有窗口 ===
cap.release()
cv2.destroyAllWindows()