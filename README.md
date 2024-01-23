# Pandas-Data-Analysis

This Python script is designed to analyze survey data related to job satisfaction (JobSat), compensation (ConvertedComp), and work preferences of respondents in the technology industry. The survey data is read from the 'survey_results_public.csv' file, and the schema data, which defines the survey's structure, is read from the 'survey_results_schema.csv' file.
Data Extraction and Preparation

    Reading Data: The script imports the pandas library and reads the survey data and schema data into Pandas DataFrames using relative paths.

    Column Selection: Relevant columns such as 'Respondent', 'YearsCode', 'ConvertedComp', 'JobSat', 'WorkWeekHrs', 'WorkRemote', 'LanguageWorkedWith', and 'Country' are extracted from the main DataFrame (df).

    Indexing: The 'Respondent' column is set as the index of the DataFrame (new_df).

    Numerical Conversion: The categorical values in the 'JobSat' column are replaced with numerical values to facilitate analysis. The column is then renamed to 'JobSatConverted' and converted to a float type.

    Binary Columns: Two new binary columns, 'WorksWithPython' and 'WorksWithC#', are created to indicate whether respondents work with Python or C# based on the 'LanguageWorkedWith' column.

Data Analysis

The script performs the following analyses:

    Python Work Analysis: Displays the mean 'ConvertedComp' and 'JobSatConverted' for respondents working with Python.

    C# Work Analysis: Displays the mean 'ConvertedComp' and 'JobSatConverted' for respondents working with C#.


Note: This script provides valuable insights into the job satisfaction and compensation of survey respondents based on their technology preferences. The results can be useful for understanding the trends and preferences within the technology industry.

Author

Matthew Dodd
