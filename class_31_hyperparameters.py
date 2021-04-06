class HyperParameters(object):
    """:arg
    This class will be used to transmit hyperparameters between class.parameters
    Most of class can inherit this class and its hyperparameters
    
    
    
    
    
    
    
    
    """
    def __init__(self):
        """:arg



        """
        # we use this to test whether other class read HyperParameters() successfully
        self.TEST = 1

        # you can change this root path in this class and import_data() function will search from this root dictionary
        self.ROOTPATH = 'D:\\OneDrive\\03_Academic\\23_Github\\44_Quora_Data_Challenge\\03_data'

        # confidence inveral value
        self.ALPHA = 0.95