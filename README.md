# Spotify Data pipeline (ETL)

![Spotify_Project](images/Spotify-ETL.jpeg)

**Tech Stack:** Python, AWS (Lambda, Cloud watch, S3, Trigger, Crawler, Glue, Athena)

•	Extracted Spotify API data using Python and automated extraction to AWS Lambda for efficient processing and storage.

•	Configured AWS Lambda with triggers set to execute every one-minute, channelling new data to an S3 bucket for uninterrupted data ingestion

•	Initiated data transformation with S3 triggers and Lambda to sort data into designated bucket folders.

•	Enabled an AWS Glue crawler to update the Glue Data Catalog automatically, allowing for sophisticated querying in Amazon Athena.



