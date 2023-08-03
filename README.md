# SScraper

This is software created to learn what sensitive information can
be extracted from a website.


This software work simply: you insert the URL of the website then the software will automatically
extract the data and store it in a log file.
The log file is structured in the way explained below.

## Data

The data that this software will extract are:

- Metadata
- Technologies used
- Contacts
- Name of people (With the relative role if specified)
- Pages with forms

## Responsibility

This software is created with the only purpose of learning, I am not responsible for any malicious 
usage of the software.

## How to use

1. You have to install [Python](https://www.python.org/) on your device if you haven't already.
2. Download this repository and extract it into a folder
3. Use the command ` pip install -r requirements.txt` to install the dependencies needed
4. Run the `main.py` file running the command `py main.py` in the terminal
5. You are asked to insert a URL of the website, **insert the URL of the home page**

## Logs files

The logs are stored in the folder `/logs` inside the project directory.

Logs are stored in `md` files cause this format allows to create easy to read documents.

### Structure

#### Files

This section will include all the sensitive files that can be founded on a website such as sitemap.xml
and robots.txt.

#### Pages

Each page found on the website will be analyzed then the information will be reported in the log file
as follows:

##### Title | Url

###### Metadata

All the metadata of the current page

###### Links

List of all the links present on the page

###### Forms and Inputs

If the page includes forms/inputs and information about these forms/inputs

###### Cookies

The cookies that are saved when you are on the page

###### Contacts

By contacts, we mean emails, social links, etc.
All the information that regard the contacts that are found on the page

###### Technologies Used

All the technologies that can be detected, for example, GSAP, ReactJS

###### General Information

Names of people (With the relative role if specified)

# TODOs

- [x] Create the `logs` folder automatically
- [x] Update `requirements.txt` and remove unused dependencies
- [ ] Update `README.md` to make it more concise and clear
- [ ] Create proper error handling
- [ ] Add template to create pull requests and add documentation for contributors