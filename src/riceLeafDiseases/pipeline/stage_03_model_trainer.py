from riceLeafDiseases.config.configuration import ConfigurationManager
from riceLeafDiseases.components.model_trainer import Training
from riceLeafDiseases.logger import logging




STAGE_NAME = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()