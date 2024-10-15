from abc import ABC, abstractmethod
import os

# Abstract base class
class DataProcessor(ABC):

    # Template method
    def process(self, file: str) -> None:
        data = self.load_data(file)

        processed_data = self.process_data(data)

        print(f" > Processed data: {len(processed_data)} items.")

        self.save_data(processed_data)

    # Primitive operation
    @abstractmethod
    def load_data(self, file: str) -> str:
        raise NotImplementedError

    # Primitive operation
    @abstractmethod
    def process_data(self, data: str) -> str:
        raise NotImplementedError

    # Primitive operation
    @abstractmethod
    def save_data(self, data: str) -> None:
        raise NotImplementedError

# Concrete class
class CSVDataProcessor(DataProcessor):

    def load_data(self, file:str) -> str:
        print(" > Loading data from CSV file.")

        with open(file, "r", encoding="utf8") as file_handle:
            return file_handle.read()

    def process_data(self, data: str) -> str:
        print(" > Processing data.")

        # list of strings per line
        return [line.split(",") for line in data.split("\n")]
    
    def save_data(self, data: str) -> None:
        print(f" > Saving processed CSV data.\n{data}")

# Concrete class
class TXTDataProcessor(DataProcessor):

    def load_data(self, file: str) -> str:
        print(" > Loading data from TXT file.")

        with open(file, "r", encoding="utf8") as file_handle:
            return file_handle.read()

    def process_data(self, data: str) -> str:
        print(" > Processing data.")

        # list of strings per line
        return [[line] for line in data.split("\n")]

    def save_data(self, data: str) -> None:
        print(f" > Saving processed TXT data.\n{data}")

# Demo
if __name__ == "__main__":

    csv_processor = CSVDataProcessor()
    txt_processor = TXTDataProcessor()

    print("CVS Data Processing:")
    csv_processor.process(os.path.join(os.path.dirname(__file__), "input.csv"))

    print("--------------------")

    print("TXT Data Processing:")
    txt_processor.process(os.path.join(os.path.dirname(__file__), "input.txt"))
