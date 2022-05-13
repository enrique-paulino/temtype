# temtype
**temtype** is a locally hosted website that shows you what types are strong, or weak, against certain TemTem.<br>
Below is a gif demonstrating how to use the website which presents some cool features like showing the Luma variant on hover.

<img src="https://i.imgur.com/YJtkB5I.gif"/>

## How does it work?
This website runs locally on the user's PC and uses python (flask) to scrape data off of the internet, as well as local json files, to return type matchups of certain TemTem based on the user's input.

## How do I install?
1. Install Python (3.8).
2. Download the files as zip, and extract into a new folder.
3. Open the terminal in said folder and run the following command:
`pip install -r requirements.txt`
4. Open the file: `run_temtype.py` 
    - The cmd window will immediately close, this is normal.
5. Open `127.0.0.1:5000` in your browser and enjoy!

## Why did I make it?
I found myself always checking the wiki when playing TemTem to see the type matchups. I thought this would be a fun project as well as something that I could use whilst playing. I can't host it so the source code, and installation instructions, can be found in this repo so that it is publicly accessible. Although many programs like this already exist, and do it better, I simply wanted to try to make my own, allowing me the opportunity to learn how web scraping works and implement it into something potentially useful.
