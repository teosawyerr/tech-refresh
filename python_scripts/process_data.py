import pandas as pd

def process_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    df['name_length'] = df['name'].apply(len)
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")
