# vim: foldmethod=indent; foldnestmax=2
import os, sys, random, time


class uint8_shaker:
    UINT8_MAX = 255

    def __init__(self, value, delta):
        self.ascending = True
        self.value = value
        self.delta = delta

    def shake(self):
        if self.ascending and self.value + self.delta >= uint8_shaker.UINT8_MAX:
            self.value = uint8_shaker.UINT8_MAX
            self.ascending = False
        elif self.ascending:
            self.value += self.delta
        elif not self.ascending and self.value - self.delta <= 0:
            self.value = 0
            self.ascending = True
        elif not self.ascending:
            self.value -= self.delta

        return self.value

    def value(self):
        return self.value

    def __str__(self):
        return str(self.value)


class Progressbar:
    def __init__(self, window_width, character=" "):
        assert len(character) == 1
        self.window_width = window_width
        self.width = 0
        self.progress = 0
        self.character = character
        self.r = uint8_shaker(random.randint(0, 255), random.randint(5, 10))
        self.g = uint8_shaker(random.randint(0, 255), random.randint(5, 10))
        self.b = uint8_shaker(random.randint(0, 255), random.randint(5, 10))

        if self.character.isspace():
            self.base_color = 48
        else:
            self.base_color = 38

    def random_inc(self):
        if random.choice((True, False)):
            self.progress += 1

    def draw(self):
        width = int(self.window_width * self.progress / 100)
        if width != self.width:
            for _ in range(width - self.width):
                print(
                    f"\033[{self.base_color};2;{self.r};{self.g};{self.b}m"
                    f"{self.character}\033[m",
                    end=''
                )
                sys.stdout.flush()
                self.r.shake()
                self.g.shake()
                self.b.shake()
            self.width = width

    def finished(self):
        return self.progress >= 100


def main():
    os.system("")
    a = uint8_shaker(0, 1)
    window_width = os.get_terminal_size().columns
    if len(sys.argv) > 1:
        progressbar = Progressbar(window_width, sys.argv[1])
    else:
        progressbar = Progressbar(window_width)

    while not progressbar.finished():
        progressbar.random_inc()
        progressbar.draw()
        time.sleep(random.randint(1, 100) * 0.001)


if __name__ == '__main__':
    main()
