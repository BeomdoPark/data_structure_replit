from tkinter import *


def draw_triangle(x, y, size, depth):
    if depth == 0:
        return

    # 삼각형 그리기
    points = [
        x,
        y,
        x + size,
        y,
        x + size / 2,
        y - size * 0.866025,
    ]
    canvas.create_polygon(points, fill="white", outline="red")

    # 재귀 호출로 삼각형 그리기
    draw_triangle(x, y, size / 2, depth - 1)
    draw_triangle(x + size / 2, y, size / 2, depth - 1)
    draw_triangle(x + size / 4, y - size * 0.433013, size / 2, depth - 1)


# 윈도우 생성
window = Tk()
canvas = Canvas(window, width=800, height=700)
canvas.pack()

# 삼각형 그리기 호출
draw_triangle(100, 600, 600, 8)

# 윈도우 실행
window.mainloop()
