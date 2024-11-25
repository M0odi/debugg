import data_loader
import data_saver
from icecream import ic
from data_processor import DataProcessor

def main():
    data = data_loader.load_data('data.txt')

    ic()
    ic(data)
    
    processor = DataProcessor(data)
    ic()
    ic(processor)
    ic(processor.data)
    
    processed_data = processor.process()

    ic()
    ic(processed_data)
    ic(processor.data)

    filtered_data = processor.filter(10)

    # filtered_data not usage in funtional code (like processor), 
    # required create new DataProcessor object with filtered_data 

    ic()
    ic(filtered_data)
    ic(processor.data)

    data_saver.save_data('processed_data.txt', filtered_data)
    ic()
    ic(data_loader.load_data('processed_data.txt'))

if __name__ == "__main__":
    main()