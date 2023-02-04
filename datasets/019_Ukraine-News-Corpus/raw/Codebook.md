# A Dataset for Analyzing and Detecting News Bias using Crowdsourcing

This dataset contains English news articles that report on the Ukraine Crisis. The articles were published in 33 countries all over the world. In total, the dataset comprises 90 news articles and 2,57 sentences. All sentences are labeled with regard to bias dimensions (subjectivity, hidden assumptions/premises, representation of governments) and bias tendencies (pro-West, pro-Russia). For data annotation, a total of 570 crowd workers were recruited to provide five judgements per sentence. For a detailed description of our dataset generation approach, please see our paper "A Dataset for Analyzing and Detecting News Bias using Crowdsourcing"

## Data Set Description

This data set comprises 90 labeled articles and 2,057 labeled sentences. Each json file contains all annotation data of one article including its sentences. Based on multiple judgements per sentence, we calculated the sentence label for each dimension/tendency in three ways:

- average ("avg"): average vote
- majority ("maj"): majority vote
- intensified ("intensified"): majority vote with exception: If at least two crowdworkers selected a non-neutral answer whereas the majority selected a neutral answer, then the non-majority answer is set as sentence label

## Data Structure

Each json file contains all information on the article defined per id. 

### Article JSON properties:
- "id": unique article identifier
- "subjectivity": JSON object with all calculated article subjectivity scores
  - "avg": Ratio of subjective sentences based on average vote
  - "maj": Ratio of subjective sentences based on majority vote
  - "intensified": Ratio of subjective sentences based on intensified vote
- "hidden_assumptions": JSON object with calculated article premises scores
  - "avg": Ratio of sentences with hidden assumptions based on average vote
  - "maj": Ratio of sentences with hidden assumptions based on majority vote
  - "intensified": Ratio of sentences with hidden assumptions based on intensified vote
- "framing": JSON object with ratio of framed sentences concerning each government
  - "russia": JSON object with ratios of positive, negative and neutral sentences concerning the Russian government
    - "pos_sent": JSON object with ratio of positive sentences
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
    - "neutral_sent": JSON object with ratio of neutral sentences 
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
    - "neg_sent": JSON object with ratio of negative sentences 
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
  - "ukraine": JSON object with ratios of positive, negative and neutral sentences concerning the Ukrainian government
    - "pos_sent": JSON object with ratio of positive sentences
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
    - "neutral_sent": JSON object with ratio of neutral sentences 
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
    - "neg_sent": JSON object with ratio of negative sentences 
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
  - "west": JSON object with ratios of positive, negative and neutral sentences concerning the Western governments
    - "pos_sent": JSON object with ratio of positive sentences
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
    - "neutral_sent": JSON object with ratio of neutral sentences 
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
    - "neg_sent": JSON object with ratio of negative sentences 
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote 
- "bias": JSON object with all calculated bias article scores
  - "pro-Russia": JSON object with all ratios of pro-Russian scores 
    - "avg": Based on average vote
    - "maj": Based on majority vote
    - "intensified": Based on intensified vote 
  - "pro-West": JSON object with all calculated pro-West  scores
    - "avg": Based on average vote
    - "maj": Based on majority vote
    - "intensified": Based on intensified vote 
- "sentences": an array of sentence JSON objects

### Sentence JSON Properties:

- "id": unique sentence identifier
- "article": identifier of the article the sentence belongs to
- "position_in_article": sentence position starting at position 0
- "content": sentence content (text)
- "subjectivity": JSON object with all corresponding annotation data
  - "score": JSON object with all subjectivity scores
    - "avg": Based on average vote
    - "maj": Based on majority vote
    - "intensified": Based on intensified vote
  - "judgements": Array with all crowd worker judgements
  - "cw_origins": Array with abbreviated countries of origin of judging crowd workers
- "hidden_assumptions": JSON object with all corresponding annotation data
  - "score": JSON object with all hidden assumption scores
    - "avg": Based on average vote
    - "maj": Based on majority vote
    - "intensified": Based on intensified vote
  - "judgements": Array with all crowd worker judgements
  - "cw_origins": Array with abbreviated countries of origin of judging crowd workers
- framing: JSON object with all corresponding annotation data
  - "score": JSON object with all framing scores
    - "russia"
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote
    - "ukraine"
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote
    - "west"
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote
  - "judgements": Array with all crowd worker judgements
  - "cw_origins": Array with abbreviated countries of origin of judging crowd workers
- "bias": JSON object with all corresponding annotation data
  - "score": JSON object with bias scores
    - "pro-russia"
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote
    - "pro-west"
      - "avg": Based on average vote
      - "maj": Based on majority vote
      - "intensified": Based on intensified vote
  - "judgements": Array with all crowd worker judgements
  - "cw_origins": Array with abbreviated countries of origin of judging crowd workers