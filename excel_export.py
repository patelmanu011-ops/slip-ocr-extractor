import pandas as pd

def save_to_excel(data, filename="output.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    return filename
