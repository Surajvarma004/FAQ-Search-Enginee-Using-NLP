from config import *
from sentence_transformers import SentenceTransformer, util
import logging
from logging.handlers import TimedRotatingFileHandler

# load transformer models
model = SentenceTransformer(MODEL)


# function for log files
def log_setup(logname, file):
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(file, "midnight", interval=1, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    handler.suffix = "%Y%m%d"
    logger.addHandler(handler)
    return logger


def question_search(ques, emmbding_df, conf):
    """
    obj: This function is used to search similar question
    :param ques: input question from user
    :param emmbding_df: a data frame which contain embedding of the same question
    :param conf: thershold for question similartiy
    :return: list of similar questions
    """

    ques = [ques]
    # extract embeddings for all all questoin
    sentence_embd = emmbding_df["embd"].to_list()
    # create embeddings for questions
    question_embd = model.encode(ques, convert_to_tensor=True)

    # Compute cosine-similarities for each sentence with each other sentence
    cosine_scores = util.cos_sim(sentence_embd, question_embd)

    emmbding_df["score"] = [round(float(score), 2) for score in cosine_scores]  # remove
    result = emmbding_df[emmbding_df["score"] >= conf].reset_index(drop=True)
    # convert all question into list
    sq = result["question1"].to_list()
    return sq
