class Rect:
    def draw_rect(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            if a > 0 and b > 0:
                r = ""
                r += "*" * b + "\n"
                for i in range(0, a - 2):
                    r += ("*" + " " * (b - 2) + "*") + "\n"
                if a > 1:
                    r += "*" * b + "\n"
                return r


            else:
                raise Exception("Długość boku musi być dłuższa od 0")
        else:
            raise Exception("Długość boku musi być liczbą całkowitą")