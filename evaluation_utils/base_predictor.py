######################################################################################
### This is a read-only file to allow participants to run their code locally.      ###
### It will be over-writter during the evaluation, Please do not make any changes  ###
### to this file.                                                                  ###
######################################################################################


class BaseMNISTPredictor:
    def prediction_setup(self):
        """
        You can do any preprocessing required for your codebase here :
            like loading your models into memory, etc.
        """
        raise NotImplementedError

    def prediction(self, image_file_path: str):
        """
        This function will be called for all the flight during the evaluation.
        NOTE: In case you want to load your model, please do so in `inference_setup` function.
        """
        raise NotImplementedError
