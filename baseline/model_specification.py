from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          BartForSequenceClassification, BartTokenizer,
                          ConvBertForSequenceClassification, ConvBertTokenizer,
                          ElectraForSequenceClassification, ElectraTokenizer,
                          GPT2ForSequenceClassification, GPT2Tokenizer)


class ModelSpecifications:
    @staticmethod
    def modelspecifications(name, model_length):
        if name == "convbert":
            convbert_tokenizer = ConvBertTokenizer.from_pretrained(
                'YituTech/conv-bert-base', model_max_length=model_length)
            convbert_model = ConvBertForSequenceClassification.from_pretrained(
                'YituTech/conv-bert-base', num_labels=2)
            learning_rate = 5e-5
            return convbert_model, convbert_tokenizer, learning_rate

        elif name == "bart":
            bart_tokenizer = BartTokenizer.from_pretrained(
                "facebook/bart-base", model_max_length=model_length)
            bart_model = BartForSequenceClassification.from_pretrained(
                "facebook/bart-base", num_labels=2)
            learning_rate = 5e-5
            return bart_model, bart_tokenizer, learning_rate

        elif name == "robertatwitter":
            roberta_twitter_tokenizer = AutoTokenizer.from_pretrained(
                "cardiffnlp/twitter-roberta-base", model_max_length=model_length)
            roberta_twitter_model = AutoModelForSequenceClassification.from_pretrained(
                'cardiffnlp/twitter-roberta-base', num_labels=2)
            learning_rate = 5e-5
            return roberta_twitter_model, roberta_twitter_tokenizer, learning_rate

        elif name == "gpt2":
            gpt2_tokenizer = GPT2Tokenizer.from_pretrained(
                "gpt2", model_max_length=model_length)
            gpt2_tokenizer.pad_token = gpt2_tokenizer.eos_token
            gpt2_model = GPT2ForSequenceClassification.from_pretrained(
                'gpt2', num_labels=2)
            gpt2_model.config.pad_token_id = gpt2_tokenizer.pad_token_id
            learning_rate = 5e-5
            return gpt2_model, gpt2_tokenizer, learning_rate

        elif name == "electra":
            electra_tokenizer = ElectraTokenizer.from_pretrained(
                'google/electra-base-discriminator', model_max_length=model_length)
            electra_model = ElectraForSequenceClassification.from_pretrained(
                'google/electra-base-discriminator', num_labels=2)
            learning_rate = 5e-5
            return electra_model, electra_tokenizer, learning_rate

        else:
            print('Model not found')
            raise ValueError
