"""
Module to handle terminal interactions
"""
from dice_simulator import Simulator


class Main:
    """
    Main class to handle methods to support user interaction with the program
    """
    run = True

    def main(self):
        print("Enter 'roll' to continue rolling a dice")
        print("Enter 'exit' to  exit the program execution")

        while self.run:
            user_input = input("Please enter 'roll' or 'exit' : ")

            if user_input.lower() == 'exit':
                self.run = False
                print("***** GOOD-BYE *****")
            elif user_input.lower() == 'roll':
                value = Simulator().dice_roller()
                print("Result : "+str(value))
            else:
                print("You entered an invalid value")


if __name__ == "__main__":
    Main().main()
