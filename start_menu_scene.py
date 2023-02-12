import pygame


class StartMenu:
    def __init__(self, display):
        self.display = display
        self.isExited = False
        self.maxScore = -1

    def show(self):
        # Set window size and title
        width = 600
        height = 300
        window = self.display.set_mode((width, height))
        self.display.set_caption("Start Menu")

        # Define colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        selected_color = (200, 200, 200)

        # Initialize font
        font32 = pygame.font.Font(None, 32)
        font27 = pygame.font.Font(None, 27)

        # Render text for the menu options
        start_text = font32.render("Start", True, white)
        exit_text = font32.render("Exit", True, white)

        # Set max_score_caption
        max_score_caption = font27.render("Max score (set invalid number if you want infinite game): ", True, white)

        # Initialize input field for max score
        max_score_input = pygame.Rect(100, 100, 200, 32)
        max_score = ""

        # Initialize menu options
        options = ["Start", "Exit"]
        selected_option = 0

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.isExited = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if options[selected_option] == "Start":
                            # Start game if the user has entered a max score
                            if max_score:
                                try:
                                    self.maxScore = int(max_score)
                                    return
                                except ValueError:
                                    print("Please enter a valid integer for max score")
                            else:
                                return
                        elif options[selected_option] == "Exit":
                            running = False
                            self.isExited = True
                    elif event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(options)
                    elif event.key == pygame.K_BACKSPACE:
                        max_score = max_score[:-1]
                    else:
                        max_score += event.unicode

            # Clear the screen
            window.fill(black)

            # Draw the input field for max score
            pygame.draw.rect(window, white, max_score_input, 2)
            pygame.draw.rect(window, black, max_score_input.inflate(-2, -2))

            # Render the text for the max score
            max_score_text = font32.render(max_score, True, white)
            window.blit(max_score_text, (100, 100))

            # Render the caption for the max score
            window.blit(max_score_caption, (100, 75))

            # Draw the menu options
            for i, option in enumerate(options):
                text = font32.render(option, True, white)
                if i == selected_option:
                    pygame.draw.rect(window, selected_color, (100, 150 + i * 35, 200, 35))
                    window.blit(text, (100, 150 + i * 50))
                else:
                    pygame.draw.rect(window, black, (100, 150 + i * 35, 200, 35))
                    window.blit(text, (100, 150 + i * 50))

            # Update the screen
            self.display.update()
