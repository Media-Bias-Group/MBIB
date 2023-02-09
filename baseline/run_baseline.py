from baseline.trainer.TrainerWrapper import TrainerWrapper

wrapper = TrainerWrapper(5, 'cognitive-bias', "bart", gpu=0, batch_size=64, model_length=78)
result = wrapper.run()