# 我的 Python 学习项目 (My Learning Journey)

## 1. 📸 滤镜程序 (Filter Program)
- **文件名**: `camera_vision.py`
- **功能**: 调用摄像头，对实时画面进行矩阵运算，实现反色、边缘检测等滤镜效果。

## 2. 🎲 骰子游戏 (Dice Game)
- **文件名**: `gui_game.py`
- **功能**: 这是一个解决“先手优势”的公平掷骰子游戏。
- **两个版本逻辑**:
  1. **完全公平版**: 纯随机概率，完全公平。
  2. **作弊版**: 引入了 `CHEAT_RATE` (欺骗率) 常量。
     - 逻辑：`CHEAT_RATE` 这个常量来对roll_a进行随机地控制，CHEAT_RATE(欺骗率）的值就是`roll_a`为6的概率。

