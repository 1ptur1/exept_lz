from ex import DataLock

if __name__ == "__main__":
    input_file = 'var10.csv'
    processor = DataLock(input_file)    
    processor.read_dataframe()

    