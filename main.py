from window import Window, Line, Point

def main():
    win = Window(800, 600)
    line_test = Line(Point(100, 100), Point(200, 300))
    win.draw_line(line_test, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()