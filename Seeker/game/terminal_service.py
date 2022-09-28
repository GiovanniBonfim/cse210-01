
class TerminalService:
    '''This class is a service that contains all the methods related to te terminal,
    like input and outputs.
    '''

    def read_number(self, prompt):
        '''This method will take a numerical input from the user
        '''
        return int(input(prompt))

    def read_text(self, prompt):
        '''This method will take a text input from the user
        '''
        return input(prompt)

    def write_text(self, text):
        '''This method is responsible to print in the terminal the given text
        '''
        print(text)