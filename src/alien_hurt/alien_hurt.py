import pgzrun

WIDTH = 800
HEIGHT = 600

color = (52, 157, 186)

zoom = Actor('alien')
zoom.pos = 200, 150

# 初始化


def draw():
    screen.fill(color)
    zoom.draw()


speed = 2
# 刷新


def update():
    zoom.left = zoom.left + speed
    if zoom.right > WIDTH:
        zoom.left = 0

# 鼠标事件


def set_alien_hurt():
    zoom.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.3)


def set_alien_normal():
    zoom.image = 'alien'


def on_mouse_down(pos):
    if zoom.collidepoint(pos):
        set_alien_hurt()


pgzrun.go()
