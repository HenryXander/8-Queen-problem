import copy
import random
import pygame
import sys

from Local_search_problem import local_search_problem
from CSP import CSP
from Local_search_agent import agent

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

FONT_SIZE = 36

# Define the size of the board and squares
BOARD_SIZE = 8
SQUARE_SIZE = 60
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE

# Title setup
title_index = 0
titles = ["hill_climbing", "simulated_annealing", "min_conflict"]


class transition_model():

    def __init__(self):
        self.queens = [1, 2, 3, 4, 5, 6, 7, 8]
        self.spots = [1, 2, 3, 4, 5, 6, 7, 8]

    def get_actions(self, node):
        queen = random.choice(self.queens)
        current_spot = node.state[queen]
        available_spots = copy.copy(self.spots)
        available_spots.remove(current_spot)
        new_spot = random.choice(available_spots)
        action = (queen, new_spot)
        return [action]

    def result(self, state, action):
        queen = action[0]
        new_spot = action[1]

        new_state = copy.copy(state)
        new_state[queen] = new_spot
        return new_state

    def step_cost(self, state, action):
        return 1


def heuristic(node):
    state = node.state
    attacks = 0
    for i in range(1, 9):
        for j in range(i + 1, 9):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks


def schedule(time):
    start_temp = 100
    factor = 0.99 ** (time - 1)
    if factor <= 0.001:
        return 0
    else:
        temp = start_temp * factor
        return temp


def initialize_initial_state():
    state = {}
    for i in range(1, 9):
        state[i] = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    return state


def initialize_csp():
    X = [1, 2, 3, 4, 5, 6, 7, 8]
    D = {}
    for var in X:
        D[var] = [1, 2, 3, 4, 5, 6, 7, 8]

    def no_conflict(var1, var2, val1, val2):
        if val1 == val2:  # zelfde rij
            return False
        elif abs(var1 - var2) == abs(val1 - val2):  # zelfde diagonaal
            return False
        return True

    C = {}
    for Xi in X:
        for Xj in X:
            if Xi < Xj:
                C[(Xi, Xj)] = no_conflict
    csp = CSP(X, D, C)
    return csp


def visualize_board(screen, board):

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Draw the squares
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Draw the queens
    for col, row in board.items():
        screen.blit(queen_image, ((col - 1) * SQUARE_SIZE, (row - 1) * SQUARE_SIZE))


def draw_title(screen):
    title_text = font.render(titles[title_index], True, RED)
    arrow_left = font.render("<", True, RED)
    arrow_right = font.render(">", True, RED)

    screen.blit(arrow_left, (SCREEN_WIDTH // 2 - title_text.get_width() // 2 - 50, SCREEN_HEIGHT - 50))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT - 50))
    screen.blit(arrow_right, (SCREEN_WIDTH // 2 + title_text.get_width() // 2 + 50, SCREEN_HEIGHT - 50))



if __name__ == '__main__':
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("8-Queens Visualization")
    font = pygame.font.Font(None, FONT_SIZE)
    clock = pygame.time.Clock()
    # Load the queen image and scale it to fit the squares
    queen_image = pygame.image.load("queen.jpg")
    queen_image = pygame.transform.scale(queen_image, (SQUARE_SIZE, SQUARE_SIZE))

    initial_state = initialize_initial_state()
    transition_model = transition_model()

    queen_problem = local_search_problem(initial_state, transition_model)

    csp = initialize_csp()
    agent = agent(queen_problem, heuristic, csp)

    current_board = initial_state

    print(queen_problem.initial_state, heuristic(queen_problem.initial_node))
    algo = titles[title_index]
    running = True
    GREY = (200, 200, 200)
    screen.fill(GREY)

    h_value = heuristic(queen_problem.initial_node)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    title_index = (title_index - 1) % len(titles)
                    algo = titles[title_index]
                elif event.key == pygame.K_RIGHT:
                    title_index = (title_index + 1) % len(titles)
                    algo = titles[title_index]
                elif event.key == pygame.K_SPACE:
                    if algo == "hill_climbing":
                        solution = agent.hill_climbing()
                        if solution != "Failure":
                            print(solution.state, solution.h_value)
                            h_value = solution.h_value
                            current_board = solution.state
                        else:
                            print("Failure")
                    elif algo == "simulated_annealing":
                        solution = agent.simulated_annealing(schedule)
                        if solution != "Failure":
                            print(solution.state, solution.h_value)
                            h_value = solution.h_value
                            current_board = solution.state
                        else:
                            print("Failure")
                    elif algo == "min_conflict":
                        solution = agent.min_conflicts()
                        if solution != "Failure":
                            print(solution.state, solution.h_value)
                            h_value = solution.h_value
                            current_board = solution.state
                        else:
                            print("Failure")

                elif event.key == pygame.K_r: #RESET
                    current_board = initial_state
                    h_value = heuristic(queen_problem.initial_node)



        screen.fill(GREY)
        visualize_board(screen, current_board)
        draw_title(screen)
        h_value_text = font.render(f"h value = {h_value}", True, RED)
        screen.blit(h_value_text, (SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        # clock.tick(60)
