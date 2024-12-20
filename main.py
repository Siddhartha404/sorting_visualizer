import pygame
import random
from algorithms import bubbleSort

# Pygame initialization
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ALGO_WIDTH, ALGO_HEIGHT = 400, 400
WHITE, BLUE, RED, YELLOW, GREEN = ((255, 255, 255), (0, 0, 255), (255, 0, 0), (255, 255, 0), (0, 255, 0))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Function to draw the vertical bars
def drawArray(array, highlights=[],swap=False):
    max_length = ALGO_WIDTH - 20  # Max length for rectangles  
    scale = max_length / 100  # Scale factor for rectangle height
    rect_width = ALGO_WIDTH // len(array)  # Width available for each rectangle
    rect_spacing = rect_width // 5  # Space between rectangles
    actual_width = rect_width - rect_spacing  # Actual rectangle width

    screen.fill(WHITE)
    for i, val in enumerate(array):
        x = i * rect_width + rect_spacing // 2 + (SCREEN_WIDTH - ALGO_WIDTH) // 2  # X-position (centered)
        y = SCREEN_HEIGHT - (val * scale) - 50  # Bottom-aligned with margin
        width = actual_width
        height = val * scale

        # Highlight the compared/swapped bars
        color = RED if i in highlights else BLUE
        if color == RED and swap:
            color = YELLOW

        pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.display.flip()

# Main function
def main():
    running = True
    sorting = True
    array = [random.randint(1, 100) for _ in range(20)]  # Generate a random array

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start sorting on SPACE key
                    sorting = True
                elif event.key == pygame.K_r:  # Reset array on R key
                    array = [random.randint(1, 100) for _ in range(20)]
                    sorting = False

        if sorting:
            bubbleSort(array, drawArray, delay=100)
            sorting = False  # Stop sorting once done

        drawArray(array)  # Draw the array in its current state

    pygame.quit()

if __name__ == "__main__":
    main()
