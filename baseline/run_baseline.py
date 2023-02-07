from mbwrapper import MBWrapper

wrapper = MBWrapper.MBWrapper(5, 4, "bart", gpu=0, batch_size=64, model_length=78)
result = wrapper.main()