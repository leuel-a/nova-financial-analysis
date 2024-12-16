#!/usr/bin/env python
import gensim
from gensim.models import CoherenceModel


def compute_coherence_values(dictionary, corpus, texts, start, limit, step):
    """
    Compute coherence values for various numbers of topics.

    :param dictionary: Gensim dictionary object.
    :param corpus: Gensim corpus object.
    :param texts: List of input texts.
    :param start: Starting number of topics.
    :param limit: Maximum number of topics.
    :param step: Step size for the number of topics.
    :returns: A tuple containing the list of LDA models and their corresponding coherence values.
    """
    model_list = []
    coherence_values = []

    for num_topics in range(start, limit, step):
        # build the LDA model
        model = gensim.models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=100,
                                       update_every=1, chunksize=100, passes=100, alpha='auto', per_word_topics=True)
        model_list.append(model)

        # compute coherence scores
        coherence_model = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherence_model.get_coherence())

    return model_list, coherence_values
