import pandas as pd
import requests

def check_url(url):
    try:
        response = requests.head(url)
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    try:
        #Read Excel the file
        file_path = r"C:/Users/file.xlsx" #Add your file path
        #Using index 1 for the second column (change this value with the columm you want)
        df = pd.read_excel(file_path, converters={1: str})  

        #Print DataFrame
        print(df.head())  #Print the first few rows of the DataFrame
        print(df.columns)  #Print the column names to verify the presence of 'E'

        #Iterate through each row and check URL status
        results = []
        for index, row in df.iterrows():
            url = row[1]  #Assuming the URLs are in the second column (index 1)
            print(f"URL: {url}")  # Print each URL to verify correctness
            status_code = check_url(url)
            results.append({'Link': url, 'Status Code': status_code})

        #Create a DataFrame from results
        result_df = pd.DataFrame(results)

        #Export the result DataFrame to a new Excel file
        result_df.to_excel("url_status_results.xlsx", index=False)
        print("Script executed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

