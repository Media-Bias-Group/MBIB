from evaluation.baseline.trainer.BaselineWrapper import BaselineWrapper

wrapper = BaselineWrapper(5, 'cognitive-bias', "roberta", gpu=0, batch_size=64, model_length=128)
result = wrapper.run()