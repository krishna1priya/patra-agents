query_dataset = [
    {'inputs': {'question': 'How many models are there in the system?'}, 'outputs': {'must_mention': ['The number of models in the system is 100.']}},
    {'inputs': {'question': 'How many edge devices are there in the system?'}, 'outputs': {'must_mention': ['NumberOfEdgeDevices: 10']}},
    {'inputs': {'question': 'What is the framework was used for model with model ID 888a1c63-2d03-478d-92b9-b371c752306e-model'}, 'outputs': {'must_mention': ['The framework used for the model with model ID `888a1c63-2d03-478d-92b9-b371c752306e-model` is `tensorflow`.']}},
    {'inputs': {'question': 'What is the accuracy of the model with model ID 888a1c63-2d03-478d-92b9-b371c752306e-model?'}, 'outputs': {'must_mention': ['The accuracy of the model with model ID `888a1c63-2d03-478d-92b9-b371c752306e-model` is 0.5686.']}},
    {'inputs': {'question': 'What are the 5 models most closely resembling the one with ID e835e0f3-3c13-4ab8-9b17-a8c5ea8dc788?'}, 'outputs': {'must_mention': ['It appears that there are no models closely resembling the one with ID `e835e0f3-3c13-4ab8-9b17-a8c5ea8dc788` based on the given query. The result set is empty.']}},
    {'inputs': {'question': 'What is the architecture of edge device?'}, 'outputs': {'must_mention': ['The architecture of the edge device is as follows:', '- CPU Architecture: ARM Cortex-A57', '- GPU Architecture: Nvidia Maxwell']}},
    {'inputs': {'question': 'Does the edge device with Device ID: jetson-nano-1 support AI operations ?'}, 'outputs': {'must_mention': ['The edge device with Device ID: jetson-nano-1 supports the following AI operations:', '- Machine Learning: True', '- Computer Vision: True', '- Deep Learning: True']}},
    {'inputs': {'question': 'What type of model is it?'}, 'outputs': {'must_mention': ['The type of model is: dnn']}},
    {'inputs': {'question': 'What is the name of the model with model ID 888a1c63-2d03-478d-92b9-b371c752306e-model?'}, 'outputs': {'must_mention': ['The name of the model with model ID 888a1c63-2d03-478d-92b9-b371c752306e-model is "UCI Adult tensorflow model".']}},
    {'inputs': {'question': 'Who is the owner of the model with model ID 888a1c63-2d03-478d-92b9-b371c752306e-model?'}, 'outputs': {'must_mention': ['Owner: Sachith Withana', 'Model Count: 100']}},
    {'inputs': {'question': 'Who owns most of the models?'}, 'outputs': {'must_mention': ['Number of Model Cards written by Sachith: 0']}},
    {'inputs': {'question': 'Who is the author of the model card named, UCI Adult Data Analysis?'}, 'outputs': {'must_mention': ['The author of the model card named "UCI Adult Data Analysis" is Sachith Withana.']}},
    {'inputs': {'question': 'How many unique device types are present in the database?'}, 'outputs': {'must_mention': ['The number of unique device types present in the database is 7']}},
    {'inputs': {'question': 'Which model trained on the UCI Adult Dataset has the lowest demographic parity?'}, 'outputs': {'must_mention': ['There are no models trained on the UCI Adult Dataset with demographic parity information available in the database.']}},
    {'inputs': {'question': 'What are the explainability metrics for model ID 3075715e-bac0-4783-bff9-4d8ea6a5f638?'}, 'outputs': {'must_mention': ['No explainability metrics were found for the model with ID 3075715e-bac0-4783-bff9-4d8ea6a5f638.']}},
    {'inputs': {'question': 'Which model deployed in SF-zone-02 has the highest fairness score?'}, 'outputs': {'must_mention': ['There are no models deployed in SF-zone-02 with a recorded fairness score.']}},
    {'inputs': {'question': 'Which database is used for this datastorage?'}, 'outputs': {'must_mention': ['The database used for data storage is the UCI Machine Learning Repository.']}},
    {'inputs': {'question': 'What do you know about UCI Machine Learning Repository?'}, 'outputs': {'must_mention': ['There is no information available in the database regarding the UCI Machine Learning Repository.']}},
    {'inputs': {'question': 'How many model cards are present in the system?'}, 'outputs': {'must_mention': ['The number of model cards present in the system is 100.']}},
    {'inputs': {'question': 'Name the model cards are present in the system?'}, 'outputs': {'must_mention': ['All the model cards listed have the same name ""UCI Adult Data Analysis"" but different external IDs']}},
    {'inputs': {'question': 'How many bias analysis are present in UCI Adult Data Analysis?'}, 'outputs': {'must_mention': ['The UCI Adult Data Analysis contains 100 bias analyses.']}},
    {'inputs': {'question': 'Name the edge device in the system?'}, 'outputs': {'must_mention': ['Nvidia Jetson Nano']}},
    {'inputs': {'question': 'Which bias analysis has the lowest demographic parity difference?'}, 'outputs': {'must_mention': ['The bias analysis with the lowest demographic parity difference is as follows: - Name: 7e110269-8e1d-4a2c-b4db-c713b292d511bias_analysis External ID: 7e110269-8e1d-4a2c-b4db-c713b292d511-bias']}},
    {'inputs': {'question': 'How many deployements are made for model ID 888a1c63-2d03-478d-92b9-b371c752306e-model?'}, 'outputs': {'must_mention': ['The number of deployments made for the model with ID 888a1c63-2d03-478d-92b9-b371c752306e-model is 0']}},
    {'inputs': {'question': 'Name the datasheet?'}, 'outputs': {'must_mention': ['The datasheet name is ""UCI Adult Dataset']}},
]