from typing import List
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def remove_stop_words(text: str) -> str:
    """
    Remove stop words from the given text.

    :param text: the text to be removed stop words
    :type text: str

    :returns: The text without stop words in it
    :rtype: str
    """
    words = word_tokenize(text)
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word.lower() not in stop_words]

    return ' '.join(filtered_words)


def tokenize_word(text: str) -> List[str]:
    """
    Lemmatize and Tokenize a word

    :param text: the word that is going to be tokenized
    :type text: str

    :return: a list of words representing tokens
    :rtype: list[str]
    """
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token.isalpha()]
    return tokens


def extract_email_organization(email: str) -> str | None:
    """
    Extract the organization from an email address.

    :param email: the email address to extract the organization from
    :type email: str

    :return: the organization name or nothing is the email is not valid
    :rtype: str | None
    """
    try:
        domain = email.split('@')[1]
        organization = domain.split('.')[0]
        return organization.capitalize()
    except IndexError:
        return None
