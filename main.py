import pygame, sys, random

# color constants
LIGHT_GRAY = (224, 223, 220)
DARK_GRAY = (34, 40, 49)
ORANGE = (214, 90, 49)

# kana dictionaries
# FIXME add combined kana, i.e. 'fa' or 'nyu'
hiragana_dict = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'か':'ka', 'き':'ki', 'く':'ku', 'け':'ke', 'こ':'ko', 'が':'ga', 'ぎ':'gi', 'ぐ':'gu', 'げ':'ge', 'ご':'go', 'さ':'sa', 'し':'shi', 'す':'su', 'せ':'se', 'そ':'so', 'ざ':'za', 'じ':'ji', 'ず':'zu', 'ぜ':'ze', 'ぞ':'zo', 'た':'ta', 'ち':'chi', 'つ':'tsu', 'て':'te', 'と':'to', 'だ':'da', 'じ':'ji', 'づ':'du', 'で':'de', 'ど':'do', 'な':'na', 'に':'ni', 'ぬ':'nu', 'ね':'ne', 'の':'no', 'ま':'ma', 'み':'mi', 'む':'mu', 'め':'me', 'も':'mo', 'は':'ha', 'ひ':'hi', 'ふ':'fu', 'へ':'he', 'ほ':'ho', 'ば':'ba', 'び':'bi', 'ぶ':'bu', 'べ':'be', 'ぼ':'bo', 'ぱ':'pa', 'ぴ':'pi', 'ぷ':'pu', 'ぺ':'pe', 'ぽ':'po', 'ら':'ra', 'り':'ri', 'る':'ru', 'れ':'re', 'ろ':'ro', 'を':'wo', 'ん':'n', 'や':'ya', 'ゆ':'yu', 'よ':'yo'}
katakana_dict = {'ア':'a', 'イ':'i', 'ウ':'u', 'エ':'e', 'オ':'o', 'カ':'ka', 'キ':'ki', 'ク':'ku', 'ケ':'ke', 'コ':'ko', 'ガ':'ga', 'ギ':'gi', 'グ':'gu', 'ゲ':'ge', 'ゴ':'go', 'サ':'sa', 'シ':'shi', 'ス':'su', 'セ':'se', 'ソ':'so', 'ザ':'za', 'ジ':'ji', 'ズ':'zu', 'ゼ':'ze', 'ゾ':'zo', 'タ':'ta', 'チ':'chi', 'ツ':'tsu', 'テ':'te', 'ト':'to', 'ダ':'da', 'ジ':'ji', 'ヅ':'du', 'デ':'de', 'ド':'do', 'ナ':'na', 'ニ':'ni', 'ヌ':'nu', 'ネ':'ne', 'ノ':'no', 'マ':'ma', 'ミ':'mi', 'ム':'mu', 'メ':'me', 'モ':'mo', 'ハ':'ha', 'ヒ':'hi', 'フ':'fu', 'ヘ':'he', 'ホ':'ho', 'バ':'ba', 'ビ':'bi', 'ブ':'bu', 'ベ':'be', 'ボ':'bo', 'パ':'pa', 'ピ':'pi', 'プ':'pu', 'ペ':'pe', 'ポ':'po', 'ラ':'ra', 'リ':'ri', 'ル':'ru', 'レ':'re', 'ロ':'ro', 'ヲ':'wo', 'ン':'n', 'ャ':'ya', 'ユ':'yu', 'ヨ':'yo'}
combined_kana_dict = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'か':'ka', 'き':'ki', 'く':'ku', 'け':'ke', 'こ':'ko', 'が':'ga', 'ぎ':'gi', 'ぐ':'gu', 'げ':'ge', 'ご':'go', 'さ':'sa', 'し':'shi', 'す':'su', 'せ':'se', 'そ':'so', 'ざ':'za', 'じ':'ji', 'ず':'zu', 'ぜ':'ze', 'ぞ':'zo', 'た':'ta', 'ち':'chi', 'つ':'tsu', 'て':'te', 'と':'to', 'だ':'da', 'じ':'ji', 'づ':'du', 'で':'de', 'ど':'do', 'な':'na', 'に':'ni', 'ぬ':'nu', 'ね':'ne', 'の':'no', 'ま':'ma', 'み':'mi', 'む':'mu', 'め':'me', 'も':'mo', 'は':'ha', 'ひ':'hi', 'ふ':'fu', 'へ':'he', 'ほ':'ho', 'ば':'ba', 'び':'bi', 'ぶ':'bu', 'べ':'be', 'ぼ':'bo', 'ぱ':'pa', 'ぴ':'pi', 'ぷ':'pu', 'ぺ':'pe', 'ぽ':'po', 'ら':'ra', 'り':'ri', 'る':'ru', 'れ':'re', 'ろ':'ro', 'を':'wo', 'ん':'n', 'や':'ya', 'ゆ':'yu', 'よ':'yo', 'ア':'a', 'イ':'i', 'ウ':'u', 'エ':'e', 'オ':'o', 'カ':'ka', 'キ':'ki', 'ク':'ku', 'ケ':'ke', 'コ':'ko', 'ガ':'ga', 'ギ':'gi', 'グ':'gu', 'ゲ':'ge', 'ゴ':'go', 'サ':'sa', 'シ':'shi', 'ス':'su', 'セ':'se', 'ソ':'so', 'ザ':'za', 'ジ':'ji', 'ズ':'zu', 'ゼ':'ze', 'ゾ':'zo', 'タ':'ta', 'チ':'chi', 'ツ':'tsu', 'テ':'te', 'ト':'to', 'ダ':'da', 'ジ':'ji', 'ヅ':'du', 'デ':'de', 'ド':'do', 'ナ':'na', 'ニ':'ni', 'ヌ':'nu', 'ネ':'ne', 'ノ':'no', 'マ':'ma', 'ミ':'mi', 'ム':'mu', 'メ':'me', 'モ':'mo', 'ハ':'ha', 'ヒ':'hi', 'フ':'fu', 'ヘ':'he', 'ホ':'ho', 'バ':'ba', 'ビ':'bi', 'ブ':'bu', 'ベ':'be', 'ボ':'bo', 'パ':'pa', 'ピ':'pi', 'プ':'pu', 'ペ':'pe', 'ポ':'po', 'ラ':'ra', 'リ':'ri', 'ル':'ru', 'レ':'re', 'ロ':'ro', 'ヲ':'wo', 'ン':'n', 'ャ':'ya', 'ユ':'yu', 'ヨ':'yo'}


def draw_start_menu(version=1):
    screen.fill(DARK_GRAY)
    # title text
    title_font = pygame.font.SysFont('cascadia code', 60)
    title_text = 'Kana Speed Guesser!'
    title_surf = title_font.render(title_text, 0, ORANGE)
    title_rect = title_surf.get_rect(center=(250, 50))
    screen.blit(title_surf, title_rect)

    # welcome message
    welcome_font = pygame.font.SysFont('MSUI Gothic', 23)
    welcome_text = 'たくさん日本語をべんきょうしてください！'
    welcome_surf = welcome_font.render(welcome_text, 0, ORANGE)
    welcome_rect = welcome_surf.get_rect(center=(250, 100))
    screen.blit(welcome_surf, welcome_rect)

    # kana and time selection text
    selection_font = pygame.font.SysFont('cascadia code', 40)
    if version == 1:
        selection_text = 'Select Kana Set:'
    elif version == 2:
        selection_text = 'Select Time Limit'
    selection_surf = selection_font.render(selection_text, 0, ORANGE)
    selection_rect = selection_surf.get_rect(center=(250, 195))
    screen.blit(selection_surf, selection_rect)

    # choice 1
    pygame.draw.rect(screen, LIGHT_GRAY, pygame.Rect(112, 226, 276, 65), 0, 30)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(112, 226, 276, 65), 3, 30)

    choice_font = pygame.font.SysFont('cascadia code', 40)
    if version == 1:
        choice_one_text = 'Hiragana'
    elif version == 2:
        choice_one_text = '0:30'
    choice_one_surf = choice_font.render(choice_one_text, 0, DARK_GRAY)
    choice_one_rect = choice_one_surf.get_rect(center=(250, 258))
    screen.blit(choice_one_surf, choice_one_rect)

    # choice 2
    pygame.draw.rect(screen, LIGHT_GRAY, pygame.Rect(112, 316, 276, 65), 0, 30)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(112, 316, 276, 65), 3, 30)

    if version == 1:
        choice_two_text = 'Katakana'
    elif version == 2:
        choice_two_text = '1:00'
    choice_two_surf = choice_font.render(choice_two_text, 0, DARK_GRAY)
    choice_two_rect = choice_two_surf.get_rect(center=(250, 348))
    screen.blit(choice_two_surf, choice_two_rect)

    # choice 3
    pygame.draw.rect(screen, LIGHT_GRAY, pygame.Rect(112, 406, 276, 65), 0, 30)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(112, 406, 276, 65), 3, 30)

    if version == 1:
        choice_three_text = 'All Kana'
    elif version == 2:
        choice_three_text = '5:00'
    choice_three_surf = choice_font.render(choice_three_text, 0, DARK_GRAY)
    choice_three_rect = choice_three_surf.get_rect(center=(250, 438))
    screen.blit(choice_three_surf, choice_three_rect)


def draw_end_menu(score, high_score):
    # results
    result_font = pygame.font.SysFont('cascadia code', 90)
    result_text = 'Results!'
    result_surf = result_font.render(result_text, 0, ORANGE)
    result_rect = result_surf.get_rect(center=(250, 50))
    screen.blit(result_surf, result_rect)

    # score
    score_font = pygame.font.SysFont('cascadia code', 50)
    score_text = f'Score: {str(score)}'
    score_surf = score_font.render(score_text, 0, ORANGE)
    score_rect = score_surf.get_rect(center=(250, 120))
    screen.blit(score_surf, score_rect)

    # high score
    high_score_font = pygame.font.SysFont('cascadia code', 50)
    high_score_text = f'High Score: {str(high_score)}'
    high_score_surf = high_score_font.render(high_score_text, 0, ORANGE)
    high_score_rect = high_score_surf.get_rect(center=(250, 170))
    screen.blit(high_score_surf, high_score_rect)

    # missed kana
    pygame.draw.rect(screen, LIGHT_GRAY, pygame.Rect(112, 240, 276, 65), 0, 30)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(112, 240, 276, 65), 3, 30)

    missed_kana_font = pygame.font.SysFont('cascadia code', 40)
    missed_kana_text = 'Skipped Kana'
    missed_kana_surf = missed_kana_font.render(missed_kana_text, 0, DARK_GRAY)
    missed_kana_rect = missed_kana_surf.get_rect(center=(250, 272))
    screen.blit(missed_kana_surf, missed_kana_rect)

    # return to menu
    pygame.draw.rect(screen, LIGHT_GRAY, pygame.Rect(112, 340, 276, 65), 0, 30)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(112, 340, 276, 65), 3, 30)

    return_font = pygame.font.SysFont('cascadia code', 40)
    return_text = 'Main Menu'
    return_surf = return_font.render(return_text, 0, DARK_GRAY)
    return_rect = return_surf.get_rect(center=(250, 372))
    screen.blit(return_surf, return_rect)


def draw_rectangle(left, top, width, height, border_radius=30, border_top_left=-1, border_top_right=-1, border_bottom_left=-1, border_bottom_right=-1, color=LIGHT_GRAY):
    pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height), 0, border_radius, border_top_left, border_top_right, border_bottom_left, border_bottom_right)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(left, top, width, height), 3, border_radius, border_top_left, border_top_right, border_bottom_left, border_bottom_right)


def draw_kana(data):
    draw_rectangle(130, 125, 240, 240)
    key, value = random.choice(list(data.items()))
    kana_text = key
    if len(kana_text) > 1:
        kana_font = pygame.font.SysFont('MSUI Gothic', 120)
    else:
        kana_font = pygame.font.SysFont('MSUI Gothic', 200)
    kana_surf = kana_font.render(kana_text, 0, DARK_GRAY)
    kana_rect = kana_surf.get_rect(center=(250, 250))
    screen.blit(kana_surf, kana_rect)
    return key, value


def draw_text_box(text):
    draw_rectangle(130, 415, 240, 65)
    box_font = pygame.font.SysFont('cascadia code', 40)
    box_surf = box_font.render(text, 0, DARK_GRAY)
    box_rect = box_surf.get_rect(center=(250, 447))
    screen.blit(box_surf, box_rect)


def draw_score(score, color=LIGHT_GRAY):
    draw_rectangle(279, 20, 60, 60, 20, 0, 20, 0, 20, color)
    score_font = pygame.font.SysFont('cascadia code', 40)
    score_surf = score_font.render(str(score), 0, DARK_GRAY)
    score_rect = score_surf.get_rect(center=(309, 50))
    screen.blit(score_surf, score_rect)


def draw_timer(time):
    minutes = time // 60
    seconds = time % 60

    if len(str(seconds)) > 1:
         clock_num = f'{minutes}:{seconds}'
    else:
         clock_num = f'{minutes}:0{seconds}'

    draw_rectangle(161, 20, 120, 60, 20, 20, 0, 20, 0)
    clock_text = clock_font.render(clock_num, True, DARK_GRAY)
    clock_rect = clock_text.get_rect(center=(221, 50))
    screen.blit(clock_text, clock_rect)


def draw_countdown():
    count = 3

    for i in range(4):
        if i < 3:
            timer_text = str(count)
            size = 200
        else:
            timer_text = 'TYPE!'
            size = 90
        pygame.draw.rect(screen, ORANGE, pygame.Rect(130, 125, 240, 240), 0, 30)
        timer_font = pygame.font.SysFont('MSUI Gothic', size)
        timer_surf = timer_font.render(timer_text, 0, LIGHT_GRAY)
        timer_rect = timer_surf.get_rect(center=(250, 250))
        screen.blit(timer_surf, timer_rect)
        pygame.display.update()
        count -= 1
        pygame.time.delay(1000)


def missed_kana_screen(skips):
    screen.fill(DARK_GRAY)
    draw_rectangle(10, 10, 80, 60, 20)
    back_button = pygame.Rect(10, 10, 80, 60)
    back_font = pygame.font.SysFont('cascadia code', 40)
    back_text = 'Back'
    back_surf = back_font.render(back_text, 0, DARK_GRAY)
    back_rect = back_surf.get_rect(center=(50, 40))
    screen.blit(back_surf, back_rect)

    draw_rectangle(10, 80, 480, 410)

    kana_font = pygame.font.SysFont('MSUI Gothic', 25)
    kana_text_list = []
    skip_set = set(skips)
    skip_list = list(skip_set)
    for i in skip_list:
        if i != skip_list[-1]:
            kana_text_list.append(f'{i[0]} = {i[1]}, ')
        else:
            kana_text_list.append(f'{i[0]} = {i[1]}')

    text_x, text_y = 250, 110
    length = 0
    kana_text = ''
    for i in kana_text_list:
        kana_text += i
        length += 1
        if length == 4 or i == kana_text_list[-1]:
            kana_surf = kana_font.render(kana_text, 0, DARK_GRAY)
            kana_rect = kana_surf.get_rect(center=(text_x, text_y))
            screen.blit(kana_surf, kana_rect)
            text_y += 30
            kana_text = ''
            length = 0
        if text_y > 470:
            break

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                if back_button.collidepoint(pos):
                    screen.fill(DARK_GRAY)
                    return
        pygame.display.update()


if __name__ == '__main__':
    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Kana Speed Guesser')
    draw_start_menu()

    # choice rects for interactive buttons
    opt_one = pygame.Rect(112, 226, 276, 65)
    opt_two = pygame.Rect(112, 316, 276, 65)
    opt_three = pygame.Rect(112, 406, 276, 65)

    # initial game state variables
    system_running = True
    start_running = True
    game_running = False
    game_over = False
    high_score = 0
    version = 1

    while system_running:
        # start menu loop
        while start_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # detects button presses
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = event.pos
                    if opt_one.collidepoint(pos) or opt_two.collidepoint(pos) or opt_three.collidepoint(pos):
                        if version == 1:
                            if opt_one.collidepoint(pos):
                                data_set = hiragana_dict
                                opt = opt_one
                                choice_text = 'Hiragana'
                                text_coord = (250, 258)

                            elif opt_two.collidepoint(pos):
                                data_set = katakana_dict
                                opt = opt_two
                                choice_text = 'Katakana'
                                text_coord = (250, 348)

                            elif opt_three.collidepoint(pos):
                                data_set = combined_kana_dict
                                opt = opt_three
                                choice_text = 'All Kana'
                                text_coord = (250, 438)

                            pygame.draw.rect(screen, ORANGE, opt, 0, 30)
                            choice_font = pygame.font.SysFont('cascadia code', 40)
                            choice_surf = choice_font.render(choice_text, 0, DARK_GRAY)
                            choice_rect = choice_surf.get_rect(center=text_coord)
                            screen.blit(choice_surf, choice_rect)

                            pygame.display.update()
                            pygame.time.delay(150)
                            draw_start_menu(2)
                            version = 2

                        elif version == 2:
                            if opt_one.collidepoint(pos):
                                counter = 30
                                opt = opt_one
                                choice_text = '0:30'
                                text_coord = (250, 258)

                            elif opt_two.collidepoint(pos):
                                counter = 60
                                opt = opt_two
                                choice_text = '1:00'
                                text_coord = (250, 348)

                            elif opt_three.collidepoint(pos):
                                counter = 300
                                opt = opt_three
                                choice_text = '5:00'
                                text_coord = (250, 438)

                            pygame.draw.rect(screen, ORANGE, opt, 0, 30)
                            choice_font = pygame.font.SysFont('cascadia code', 40)
                            choice_surf = choice_font.render(choice_text, 0, DARK_GRAY)
                            choice_rect = choice_surf.get_rect(center=text_coord)
                            screen.blit(choice_surf, choice_rect)

                            pygame.display.update()
                            pygame.time.delay(150)

                            start_running = False
                            game_running = True
                            break


            pygame.display.update()

        # game background
        screen.fill(DARK_GRAY)
        draw_rectangle(161, 20, 120, 60, 20, 20, 0, 20, 0)
        draw_rectangle(279, 20, 60, 60, 20, 0, 20, 0, 20)
        draw_rectangle(130, 125, 240, 240)
        draw_rectangle(130, 415, 240, 65)

        # skip button
        skip_font = pygame.font.SysFont('cascadia code', 30)
        skip_surf = skip_font.render('Press TAB to skip', 0, (LIGHT_GRAY))
        skip_rect = skip_surf.get_rect(center=(250, 390))
        screen.blit(skip_surf, skip_rect)

        # game state
        user_text = ''
        game_score = 0
        skip_list = []
        green_count = -1

        # countdown and initial draw_kana()
        clock_font = pygame.font.SysFont('cascadia code', 40)
        draw_timer(counter)
        draw_score(game_score)
        draw_countdown()

        # initiate timer
        clock = pygame.time.Clock()
        clock_text = clock_font.render(str(counter), True, DARK_GRAY)
        time_delay = 1000
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, time_delay)

        solution = draw_kana(data_set)

        # game loop
        while game_running and not game_over:
            clock.tick(60)

            if green_count > 0:
                draw_score(game_score, (130,251,130))
                green_count -= 1
            elif green_count == 0:
                draw_score(game_score)
                green_count -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and len(user_text) != 0:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_TAB:
                        skip_list.append(solution)
                        solution = draw_kana(data_set)
                    elif event.key not in range(97, 123):
                        continue
                    else:
                        user_text += chr(event.key)
                    draw_text_box(user_text)


                if user_text == solution[1]:
                    game_score += 1
                    user_text = ''
                    draw_rectangle(130, 415, 240, 65)
                    solution = draw_kana(data_set)
                    draw_score(game_score)
                    green_count = 8

                if event.type == timer_event:
                    if counter < 1:
                        game_over = True
                        game_running = False
                        if game_score > high_score:
                            high_score = game_score
                        break
                    else:
                        counter -= 1

            draw_timer(counter)
            pygame.display.update()

        screen.fill(DARK_GRAY)
        draw_end_menu(game_score, high_score)
        missed_kana_rect = pygame.Rect(112, 240, 276, 65)
        return_rect = pygame.Rect(112, 340, 276, 65)

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # detects button presses
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = event.pos
                    if missed_kana_rect.collidepoint(pos):
                        missed_kana_screen(skip_list)
                        draw_end_menu(game_score, high_score)
                        missed_kana_rect = pygame.Rect(112, 240, 276, 65)
                        return_rect = pygame.Rect(112, 340, 276, 65)
                    elif return_rect.collidepoint(pos):
                        screen.fill(DARK_GRAY)
                        draw_start_menu()

                        # choice rects for interactive buttons
                        opt_one = pygame.Rect(112, 226, 276, 65)
                        opt_two = pygame.Rect(112, 316, 276, 65)
                        opt_three = pygame.Rect(112, 406, 276, 65)

                        alph = 0
                        version = 1
                        green_count = -1

                        start_running = True
                        game_over = False
                        button = False

            pygame.display.update()



