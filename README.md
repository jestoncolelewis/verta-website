# VERTA Safety Website Rebuild

Converting the site builder version of the VERTA Safety website into hard code build. 

## Goals
- Deploy as a serverless static website
- Use only custom code in HTML, JavaScript, and CSS for frontend
- Use Python for Lambda function
- For forms, use Lambda as an intermediary to process the API request and send the form via email using SES
- Use custom IaC for deployment