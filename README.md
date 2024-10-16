# Local TV Server Web Scraper

Web scraper including GitHub Action workflow to retrieve new tv stream from a website every other hour.


## Manual usage

Either you use a virtual environment *(preferred)*:

        # Setup & activate virtual environment
        python3 -m venv ./env
        source ./env/bin/activate
        
        # Install required modules from requirements.txt
        pip install -r requirements.txt
        
        # Execute web scraper
        python main.py
        
Alternatively, you can use it without a virtual environment:

        # Install required modules
        pip install requests
        pip install beautifulsoup4
        
        # Execute web scraper
        python3 main.py

## Settings for GitHub Action

For the GitHub Action you need the following configurations:

1. Set the *Workflow Permissions* to *Read and write permissions* under *Settings > Actions > General*.
2. Under *Settings > Secrets and variables > Actions* define the repository secrets `MAIL_PASSWORD` and `MAIL_USERNAME`

## Note
`pipreqs` is used for creating the `requirements.txt`. 

    pip install pipreqs
    pipreqs /path/to/project
