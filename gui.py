import pygame


class sudoku:
    def __init__(self, list1):
        self.list1 = list1

    def play(self):

        l3 = []

        for items in self.list1:
            temp = []
            for item in items:
                temp.append(item)
            l3.append(temp)

        l3 = solve(0, -1, l3)

        l1 = []

        l2 = []

        for items in self.list1:
            temp = []
            for item in items:
                temp.append(item)
            l1.append(temp)

        for items in self.list1:
            temp = []
            for item in items:
                temp.append(item)
            l2.append(temp)

        pygame.init()

        height = 360
        width = 400

        screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption("sudoku by The Vaibhav")

        icon = pygame.image.load('panda.png')
        pygame.display.set_icon(icon)

        dark_slate_gray = (72, 61, 139)
        light_slate_gray = (106, 90, 205)

        back = (255, 248, 220)
        hilico = (188, 143, 143)

        x = 0
        y = 0

        # fetching fonts
        font_p = pygame.font.SysFont('arial black', 15)
        font_f = pygame.font.SysFont('comicsans', 40)

        running = True
        FAIL = 0

        while running:
            screen.fill(back)

            mo_pos = pygame.mouse.get_pos()

            num_col = dark_slate_gray

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 1

                    elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 2

                    elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 3

                    elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 4

                    elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 5

                    elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 6

                    elif event.key == pygame.K_KP7 or event.key == pygame.K_7:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 7

                    elif event.key == pygame.K_KP8 or event.key == pygame.K_8:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 8

                    elif event.key == pygame.K_KP9 or event.key == pygame.K_9:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 9

                    elif event.key == pygame.K_KP_0 or event.key == pygame.K_0 or event.key == pygame.K_BACKSPACE:
                        l1[mo_pos[0] // 40][mo_pos[1] // 40] = 0

                    elif event.key == pygame.K_SPACE:
                        solve(0, -1, l2)
                        pygame.time.delay(200)

                    elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if l1[mo_pos[0] // 40][mo_pos[1] // 40] == l3[mo_pos[0] // 40][mo_pos[1] // 40]:
                            l2[mo_pos[0] // 40][mo_pos[1] // 40] = l1[mo_pos[0] // 40][mo_pos[1] // 40]

                        else:
                            l1[mo_pos[0] // 40][mo_pos[1] // 40] = 0
                            l2[mo_pos[0] // 40][mo_pos[1] // 40] = 0
                            FAIL += 1

            for x in range(0, 9):
                for y in range(0, 9):

                    if x % 3 == 0 and y % 3 == 0:
                        thick = 3
                    else:
                        thick = 1

                    pygame.draw.line(screen, (0, 0, 255), (x * 40, 0), (x * 40, height), thick)
                    pygame.draw.line(screen, (0, 0, 255), (0, y * 40), (width, y * 40), thick)

                    no = self.list1[x][y]

                    if self.list1[x][y] != 0:
                        img1 = font_f.render(str(no), False, num_col, back)
                        screen.blit(img1, (x * 40 + 10, y * 40 + 10))

                    else:
                        if l2[x][y] != 0:
                            img1 = font_f.render(str(l2[x][y]), False, light_slate_gray, back)
                            screen.blit(img1, (x * 40 + 10, y * 40 + 10))

                        elif l1[x][y] != 0:
                            img1 = font_p.render(str(l1[x][y]), False, light_slate_gray, back)
                            screen.blit(img1, (x * 40 + 5, y * 40 + 2))

                        if all(a < b for a, b in zip(mo_pos, (x * 40 + 40, y * 40 + 40))) and all(
                                a > b for a, b in zip(mo_pos, (x * 40, y * 40))):
                            pygame.draw.rect(screen, hilico, (x * 40, y * 40, 40, 40), 4, 2)

            pygame.draw.rect(screen, (128, 0, 0), (0, 360, 360, 40), 3, -1)

            lives_img = font_f.render('FAILED  : ', False, (128, 0, 0), back)
            screen.blit(lives_img, (10, 365))

            time =pygame.time.get_ticks()
            timer = font_f.render(str("{:.1f}".format(time/1000)), False, (255, 0, 0), back)

            img2 = font_f.render(str(FAIL), False, dark_slate_gray, back)
            screen.blit(img2, (150, 365))

            screen.blit(timer, (225, 365))

            pygame.display.update()


def isingrid(x, i, j, sdk):
    while i % 3 != 0:
        i -= 1
    while j % 3 != 0:
        j -= 1

    for p in range(i, i + 3):
        for q in range(j, j + 3):
            if x == sdk[p][q]:
                return True
    else:
        return False

def issolved(sdk):
    for items in sdk:
        if 0 in items:
            return False
    else:
        return True

def is_aval(n, i, j, sdk):
    if n in sdk[i]:
        return False
    for p in range(0, 9):
        if sdk[p][j] == n:
            return False
    if isingrid(n, i, j, sdk):
        return False
    else:
        return True

def solve(i, j, sdk):
    if issolved(sdk):
        return

    if i == j == 8:
        print('Finished')
        return
    else:
        if j == 8 and i != 8:
            i += 1
            j = 0
        else:
            j += 1

        if sdk[i][j] == 0:
            for x in range(1, 10):
                if is_aval(x, i, j, sdk):
                    sdk[i][j] = x
                    solve(i, j, sdk)
            else:
                if not issolved(sdk):
                    sdk[i][j] = 0
                    return
        else:
            if issolved(sdk):
                return
            solve(i, j, sdk)
    return sdk

