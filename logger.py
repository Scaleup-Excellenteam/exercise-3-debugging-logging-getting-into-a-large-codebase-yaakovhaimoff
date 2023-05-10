import logging


def get_logger():
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler and add it to the logger
    handler = logging.FileHandler("chess.log")
    handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Remove any existing handlers from the logger
    for existing_handler in logger.handlers:
        logger.removeHandler(existing_handler)

    # Add the new handler to the logger
    logger.addHandler(handler)

    return logger


white_knight_move = 0  # knight_move is a global variable
black_knight_move = 0  # knight_move is a global variable


def add_knight_moves(add, white):
    global white_knight_move
    global black_knight_move
    if white:
        white_knight_move += add
    else:
        black_knight_move += add

def get_knight_moves(white):
    if white:
        return white_knight_move
    else:
        return black_knight_move


all_white_pieces_are_alive = 0  # all_pieces_are_alive is a global variable
all_black_pieces_are_alive = 0  # all_pieces_are_alive is a global variable
white_dead_pieces = 0
black_dead_pieces = 0

def add_pieces_are_alive(white):
    global all_white_pieces_are_alive
    global all_black_pieces_are_alive
    if white and white_dead_pieces == 0:
        all_white_pieces_are_alive += 1
    elif not white and black_dead_pieces == 0:
        all_black_pieces_are_alive += 1


def get_pieces_are_alive(white):
    if white:
        return all_white_pieces_are_alive
    else:
        return all_black_pieces_are_alive


def add_dead_pieces(white):
    global white_dead_pieces
    global black_dead_pieces
    if white:
        white_dead_pieces += 1
    elif not white:
        black_dead_pieces += 1


white_checks = 0  # white checks is a global variable
black_checks = 0  # black checks is a global variable


def add_checks(add, white):
    global white_checks
    global black_checks
    if white:
        white_checks += add
    else:
        black_checks += add

def get_checks(white):
    if white:
        return white_checks
    else:
        return black_checks
