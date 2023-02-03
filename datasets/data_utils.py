import re

def prepare_text(text):
        text = re.sub(r"@[A-Za-z0-9_]+", ' ', text) # remove @user
        text = re.sub(r"https?://[A-Za-z0-9./]+", ' ', text) # remove links
        text = re.sub(r"[^a-zA-z.!?'0-9]", ' ', text) # remove smileys
        text = re.sub('[^A-Za-z0-9]+', ' ', text) # remove any other special characters
        text = re.sub('#', '', text) # remove hash sign
        text = re.sub('\t', ' ',  text) # remove tab
        text = re.sub(r" +", ' ', text) # remove multiple whitespaces
        text = re.sub(r"linebreak", '', text)  # remove linebreaks
        return text