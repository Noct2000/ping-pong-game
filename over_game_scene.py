import pygame


class OverGameScene:
    def __init__(self, display):
        self.display = display
        self.isExited = False
        self.maxScore = -1

    def show(self, winner, is_exited):
        # If player exit from start menu
        if is_exited:
            self.isExited = True
            return

        # Set window size and title
        width = 600
        height = 300
        window = self.display.set_mode((width, height))
        self.display.set_caption("Ping-Pong game")

        # Define colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        selected_color = (200, 200, 200)

        # Initialize font
        font32 = pygame.font.Font(None, 32)
        font27 = pygame.font.Font(None, 27)

        # Set max_score_caption
        if winner:
            max_score_caption = font27.render(f"Winner is {winner['name']} with score: {winner['score']}", True, white)
        else:
            max_score_caption = font27.render("No winner", True, white)

        # Get the rectangle representing the size of the text surface
        text_rect = max_score_caption.get_rect()

        # Set the central x-position of the text
        text_rect.centerx = window.get_rect().centerx
        text_rect.centery = 100

        # Initialize menu options
        options = ["Restart", "Exit"]
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
                        if options[selected_option] == "Restart":
                            running = False
                        elif options[selected_option] == "Exit":
                            running = False
                            self.isExited = True
                    elif event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(options)

            # Clear the screen
            window.fill(black)

            # Render the caption for the max score
            window.blit(max_score_caption, text_rect)

            # Draw the menu options
            for i, option in enumerate(options):
                text = font32.render(option, True, white)
                if i == selected_option:
                    text_width = 100
                    pygame.draw.rect(window, selected_color, (text_rect.centerx - text_width, 150 + i * 35, 200, 35))
                    window.blit(text, (text_rect.centerx - text_width, 150 + i * 50))
                else:
                    pygame.draw.rect(window, black, (100, 150 + i * 35, 200, 35))
                    window.blit(text, (text_rect.centerx - text_width, 150 + i * 50))

            # Update the screen
            self.display.update()
