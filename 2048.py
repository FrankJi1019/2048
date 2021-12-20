import pygame
import numpy as np
import random

windowWidth = 900
windowHeight = 600
maxGameLevel = 7
# Width of the edge of the button
buttonEdgeWidth = 5
# Width of the edge of the button when the mouse is hovering over it
buttonEdgeWidth2 = 5

# Color of the background for both game window and intro window
backgroundColor = (230, 255, 255)
# Color for the numbers (text) in th grid of the game window
numberColor = (123, 0, 180)
# Color of the grid in the game window
gridColor = (133, 133, 173)
# Color of the boxes according to the number in the box
boxColor_0 = (255, 255, 214)
boxColor_2 = (179, 240, 255)
boxColor_4 = (120, 255, 255)
boxColor_8 = (128, 204, 255)
boxColor_16 = (51, 255, 173)
boxColor_32 = (102, 255, 102)
boxColor_64 = (179, 255, 102)
boxColor_128 = (255, 255, 153)
boxColor_256 = (255, 255, 0)
boxColor_512 = (255, 204, 51)
boxColor_1024 = (255, 180, 51)
boxColor_2048 = (255, 153, 51)
boxColor_4096 = (255, 51, 51)
boxColor_error = (255, 0, 0)
boxColors = {0: boxColor_0, 2: boxColor_2, 4: boxColor_4, 8: boxColor_8, 16: boxColor_16, 32: boxColor_32,
             64: boxColor_64, 128: boxColor_128, 256: boxColor_256, 512: boxColor_512, 1024: boxColor_1024,
             2048: boxColor_2048, 4096: boxColor_4096}

# The color of the game title "2048" in the intro window
titleColor_2 = (255, 0, 0)
titleColor_0 = (230, 230, 0)
titleColor_4 = (0, 220, 0)
titleColor_8 = (0, 0, 230)

# Color of the button edge
buttonColor = backgroundColor
# Color of the button edge when mouse is hovering over it
buttonColor2 = (153, 51, 102)
# Color of the text in the button
buttonColorText = (153, 51, 102)
# Color of the text in the button when the mouse is hovering over it
buttonColorText2 = (153, 51, 102)

# Color of the buttons in the game window
gameButtonColor = (77, 136, 255)
# Second color of the button in the game window (when the mouse is hovering over it)
gameButtonColor2 = (64, 255, 0)
# color of the text on the button in the game window
gameButtonTextColor = backgroundColor
# Second color of the text on the button inn the game window (when the mouse is hovering over it)
gameButtonTextColor2 = backgroundColor

# The color of the text displayed when there is no more move
gameOverColor = (255, 0, 0)

pygame.init()
GameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()


def InitBoard(gameLevel):
    board = [[0 for i in range(gameLevel)] for j in range(gameLevel)]
    board = np.array(board)
    num2 = round(gameLevel / 2)
    for i in range(num2):
        row = random.randint(0, (gameLevel - 1))
        col = random.randint(0, (gameLevel - 1))
        while board[row][col] != 0:
            row = random.randint(0, (gameLevel - 1))
            col = random.randint(0, (gameLevel - 1))
        board[row][col] = [2, 2, 2, 4, 4][random.randint(0, 4)]
    return board


def ContinueGaming(array, gameLevel):
    for r in range(0, gameLevel - 1):
        for c in range(0, gameLevel - 1):
            if array[r][c] == array[r + 1][c]:
                return True
            if array[r][c] == array[r][c + 1]:
                return True
            if array[r][c] == 0 or array[r + 1][c] == 0 or array[r][c + 1] == 0 or array[r + 1][c + 1] == 0:
                return True
    for i in range(0, gameLevel - 1):
        if array[i][gameLevel - 1] == array[i + 1][gameLevel - 1]:
            return True
        if array[gameLevel - 1][i] == array[gameLevel - 1][i + 1]:
            return True
    return False


def SortZero(array, gameLevel):
    for i in range(0, gameLevel - 1):
        for j in range(0, gameLevel - 1):
            if array[j] == 0:
                array[j] = array[j + 1]
                array[j + 1] = 0
    return array


def MoveNumbers(board, move, gameLevel):
    board = np.array(board)
    for i in range(0, gameLevel):
        if move == 'a':
            board[i] = SortZero(board[i], gameLevel)
        if move == 'd':
            board = np.rot90(board)
            board = np.rot90(board)
            board[i] = SortZero(board[i], gameLevel)
            board = np.rot90(board)
            board = np.rot90(board)
        if move == 'w':
            board = np.rot90(board)
            board[i] = SortZero(board[i], gameLevel)
            board = np.rot90(board)
            board = np.rot90(board)
            board = np.rot90(board)
        if move == 's':
            board = np.rot90(board)
            board = np.rot90(board)
            board = np.rot90(board)
            board[i] = SortZero(board[i], gameLevel)
            board = np.rot90(board)
    return board


def NewNumber(board, gameLevel):
    if gameLevel <= 4:
        maxNew = 1
    else:
        maxNew = gameLevel - 3
    for i in range(maxNew):
        row = random.randint(0, gameLevel - 1)
        col = random.randint(0, gameLevel - 1)
        while board[row][col] != 0:
            row = random.randint(0, gameLevel - 1)
            col = random.randint(0, gameLevel - 1)
        board[row][col] = [2, 2, 2, 2, 4][random.randint(0, 4)]
    return board


def SumArray(array, gameLevel):
    for i in range(0, gameLevel - 1):
        if array[i] == array[i + 1]:
            array[i] = array[i] + array[i + 1]
            array[i + 1] = 0
    return array


def SumNumbers(board, move, gameLevel):
    board = np.array(board)
    for i in range(0, gameLevel):
        if move == 'a':
            board[i] = SumArray(board[i], gameLevel)
        if move == 'd':
            board = np.rot90(board)
            board = np.rot90(board)
            board[i] = SumArray(board[i], gameLevel)
            board = np.rot90(board)
            board = np.rot90(board)
        if move == 'w':
            board = np.rot90(board)
            board[i] = SumArray(board[i], gameLevel)
            board = np.rot90(board)
            board = np.rot90(board)
            board = np.rot90(board)
        if move == 's':
            board = np.rot90(board)
            board = np.rot90(board)
            board = np.rot90(board)
            board[i] = SumArray(board[i], gameLevel)
            board = np.rot90(board)
    return board


def ValidArray(array, gameLevel):
    if sum(array) == 0:
        return False
    for i in range(0, gameLevel - 1):
        if array[i] == 0 and array[i + 1] != 0:
            return True
    count = 0
    while array[count] != 0 and count < (gameLevel - 1):
        if array[count] == array[count + 1]:
            return True
        count += 1
    return False


def AllowMoving(array, m, gameLevel):
    m = m.lower()
    array = np.array(array)
    invalid = 0
    if m == 'w':
        array = np.rot90(array)
    if m == 'd':
        array = np.rot90(array)
        array = np.rot90(array)
    if m == 's':
        array = np.rot90(array)
        array = np.rot90(array)
        array = np.rot90(array)
    for i in range(0, gameLevel):
        if not ValidArray(array[i], gameLevel):
            invalid += 1
    if invalid == gameLevel:
        return False
    else:
        return True


def UpDateBoard(array, m, gameLevel):
    if AllowMoving(array, m, gameLevel):
        array = MoveNumbers(array, m, gameLevel)
        array = SumNumbers(array, m, gameLevel)
        array = MoveNumbers(array, m, gameLevel)
        array = NewNumber(array, gameLevel)
    return array


def display_message(text, center_x, center_y, color, fontSize):
    text = str(text)
    textFont = pygame.font.Font('freesansbold.ttf', fontSize)
    textSurf = textFont.render(text, True, color)
    textRec = textSurf.get_rect()
    textRec.center = (center_x, center_y)
    GameDisplay.blit(textSurf, textRec)


def DrawGrid(array, gameLevel):
    gridSize = 460
    sepWidth = gridSize / (11 * gameLevel + 1)
    boxSize = sepWidth * 10
    leftShift = 60
    downShift = 60
    pygame.draw.rect(GameDisplay, gridColor, (leftShift, downShift, gridSize, gridSize))
    for i in range(0, gameLevel):
        for j in range(0, gameLevel):
            boxX = leftShift + sepWidth + (sepWidth + boxSize) * i
            boxY = downShift + sepWidth + (sepWidth + boxSize) * j
            try:
                boxColor = boxColors[array[j][i]]
            except Exception:
                boxColor = boxColor_error
            pygame.draw.rect(GameDisplay, boxColor, (boxX, boxY, boxSize, boxSize))


def DrawButton(text, x, y, width, height, color, edgeColor, edgeWidth, buttonFontSize):
    pygame.draw.rect(GameDisplay, edgeColor, (x, y, width, height))
    pygame.draw.rect(GameDisplay, backgroundColor, (x + edgeWidth, y + edgeWidth, width - 2 * edgeWidth,
                                                    height - 2 * edgeWidth))
    display_message(text, x + 0.5 * width, y + 0.5 * height, color, buttonFontSize)


def DrawButton2(text, x, y, width, height, color1, color2, buttonFontSize):
    pygame.draw.rect(GameDisplay, color1, (x, y, width, height))
    display_message(text, x + 0.5 * width, y + 0.5 * height + 2, color2, buttonFontSize)


def MouseOnButton(buttonX, buttonY, buttonWidth, buttonHeight):
    mouse = pygame.mouse.get_pos()
    if buttonX < mouse[0] < (buttonX + buttonWidth) and buttonY < mouse[1] < (buttonY + buttonHeight):
        return True
    else:
        return False


def MouseClickButton(buttonX, buttonY, buttonWidth, buttonHeight):
    click = pygame.mouse.get_pressed()

    if MouseOnButton(buttonX, buttonY, buttonWidth, buttonHeight):
        if click[0] == 1:
            return True
        else:
            return False


def GenerateFirstButtonPosition(gameLevel):
    firstButtonY = round(windowHeight / (gameLevel + 1))
    firstButtonX = 450
    buttonVerticalSep = firstButtonY
    buttonHorizontalSep = 200
    return firstButtonY, firstButtonX, buttonHorizontalSep, buttonVerticalSep


def FinishGame():
    display_message('No More Possible Move', windowWidth / 2, 100, gameOverColor, 60)


def GameLoop(gameLevel):
    board = InitBoard(gameLevel)
    move = 'none'
    gridSize = 460
    sepWidth = gridSize / (11 * gameLevel + 1)
    boxSize = sepWidth * 10
    leftShift = 60
    downShift = 60
    numSize = round(0.4 * boxSize)
    restartButtonX = 630
    backButtonX = 630
    restartButtonY = 170
    backButtonY = 340
    buttonWidth = 150
    buttonHeight = 50
    buttonTextSize = 30

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move = 'w'
                if event.key == pygame.K_DOWN:
                    move = 's'
                if event.key == pygame.K_RIGHT:
                    move = 'd'
                if event.key == pygame.K_LEFT:
                    move = 'a'
            if event.type == pygame.KEYUP:
                move = 'none'

        GameDisplay.fill(backgroundColor)

        DrawButton2('RESTART', restartButtonX, restartButtonY, buttonWidth, buttonHeight, gameButtonColor,
                    gameButtonTextColor, buttonTextSize)
        if MouseOnButton(restartButtonX, restartButtonY, buttonWidth, buttonHeight):
            DrawButton2('RESTART', restartButtonX, restartButtonY, buttonWidth, buttonHeight, gameButtonColor2,
                        gameButtonTextColor2, buttonTextSize)
        if MouseClickButton(restartButtonX, restartButtonY, buttonWidth, buttonHeight):
            GameLoop(gameLevel)

        DrawButton2('BACK', backButtonX, backButtonY, buttonWidth, buttonHeight, gameButtonColor,
                    gameButtonTextColor, buttonTextSize)
        if MouseOnButton(backButtonX, backButtonY, buttonWidth, buttonHeight):
            DrawButton2('BACK', backButtonX, backButtonY, buttonWidth, buttonHeight, gameButtonColor2,
                        gameButtonTextColor2, buttonTextSize)
        if MouseClickButton(backButtonX, backButtonY, buttonWidth, buttonHeight):
            break

        DrawGrid(board, gameLevel)

        if ContinueGaming(board, gameLevel) and move != 'none':
            board = UpDateBoard(board, move, gameLevel)

        for i in range(0, gameLevel):
            for j in range(0, gameLevel):
                whatToShow = board[i][j]
                if whatToShow == 0:
                    whatToShow = ' '
                else:
                    whatToShow = str(whatToShow)
                numX = leftShift + sepWidth + 0.5 * boxSize + (sepWidth + boxSize) * j
                numY = downShift + sepWidth + 0.5 * boxSize + (sepWidth + boxSize) * i
                display_message(whatToShow, numX, numY, numberColor, numSize)

        move = 'none'

        if not ContinueGaming(board, gameLevel):
            FinishGame()

        pygame.display.update()
        clock.tick(100)


def IntroLoop():
    buttonFontSize = 40
    buttonWidth = 180 + 10 * (maxGameLevel >= 10)
    buttonHeight = 70
    firstButtonY, firstButtonX, buttonHorizontalSep, buttonVerticalSep = GenerateFirstButtonPosition(maxGameLevel // 2)
    firstButtonY -= buttonHeight / 2
    buttonText = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        GameDisplay.fill(backgroundColor)

        display_message('2', 160, 220, titleColor_2, 300)
        display_message('0', 290, 200, titleColor_0, 180)
        display_message('4', 190, 390, titleColor_4, 180)
        display_message('8', 330, 390, titleColor_8, 300)

        for i in range(2, maxGameLevel + 1):
            text = '- ' + str(i) + ' × ' + str(i) + ' -'
            buttonText.append(text)
            DrawButton(text, firstButtonX + buttonHorizontalSep * (i % 2 == 1),
                       firstButtonY + buttonVerticalSep * ((i - 2) // 2),
                       buttonWidth, buttonHeight, buttonColorText, buttonColor, buttonEdgeWidth, buttonFontSize)
            if MouseOnButton(firstButtonX + buttonHorizontalSep * (i % 2 == 1),
                             firstButtonY + buttonVerticalSep * ((i - 2) // 2),
                             buttonWidth, buttonHeight):
                DrawButton(text, firstButtonX + buttonHorizontalSep * (i % 2 == 1),
                           firstButtonY + buttonVerticalSep * ((i - 2) // 2),
                           buttonWidth, buttonHeight, buttonColorText2, buttonColor2, buttonEdgeWidth2, buttonFontSize)
            if MouseClickButton(firstButtonX + buttonHorizontalSep * (i % 2 == 1),
                                firstButtonY + buttonVerticalSep * ((i - 2) // 2),
                                buttonWidth, buttonHeight):
                return i

        pygame.display.update()
        clock.tick(100)


while True:
    level = IntroLoop()
    GameLoop(level)
