import chess
import chess.engine
import random
from collections import Counter

''' CHANGE THESE CONFIGURATIONS '''

sim_games = 1 # How many games to simulate

opponent = "random" # Accepts 'random' or 'engine'

verbose = False # Should each game print results on termination

meta_analyze = True # When true analyzes the results list

''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''

results = []

def analyze_board(board, verbose=verbose):
  color_map = {None: "None", True: "White", False: "Black"}
  outcome = board.outcome()

  moves = board.fullmove_number
  winner = color_map[outcome.winner]
  termination = outcome.termination

  results.append((moves, winner, termination))
  if verbose: print(f"Game completed in {moves} moves with outcome {termination} and winner {winner}")

def meta_analyze():
  global results
  result_dicts = [dict(Counter(tup)) for tup in zip(*results)]
  moves = result_dicts[0]
  winners = result_dicts[1]
  terminations = result_dicts[2]
  print(moves, winners, terminations, sep="\n")

def play_game(opponent=opponent):

    engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")

    board = chess.Board()
    while (not board.is_game_over()):
        moves = list(board.legal_moves)
        random.shuffle(moves)
        random_move = moves[0]
        engine_move = engine.play(board, chess.engine.Limit(time=0.1)).move
        if board.turn or opponent == "random":
          board.push(random_move)
        else:
          board.push(engine_move)

    engine.quit()
    analyze_board(board)

for _ in range(sim_games): play_game()
if meta_analyze: meta_analyze()