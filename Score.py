from Utils import SCORES_FILE_NAME


def add_score(DIFFICULTY):
    POINT_OF_WINNING = (DIFFICULTY * 3) + 5
    tmp = open(SCORES_FILE_NAME, "r").read()
    tmp = int(tmp)
    final_score = tmp + POINT_OF_WINNING
    final_score = str(final_score)
    curr_score = open(SCORES_FILE_NAME, "w+")
    curr_score.write(final_score)
    curr_score.close()


