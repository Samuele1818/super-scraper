# SScraper

This is a software created with the purpose of learning what are the sensitive information that can
be extracted from a website.

This software will work in a very simple way, you insert the URL of the website, and thw software
will automatically extract all the date of the website and store this data in a log file that is
structured in a way explained below.

## Data

The date that this software will extract are:

- Metadata
- Technologies used
- Contacts
- Name of people (With the relative role if specified)
- Pages with forms

## Responsibility

This software is created with the only purpose of learn, I am not responsible for any malicious usage
of the software.

## How to use

1. You have to install [Python](https://www.python.org/) on your device, if you haven't already it.
2. Download this repository and extract into a folder
3. Run the `main.py` file running the command `py main.py` in the terminal
4. You are asked to insert a URL of the website, **insert the URL of the home page**

## Logs files

The logs are stored in the folder `/logs`, inside the project directory.

Logs are stored in `md` files cause this format allows to create easy to read documents.

**Note that if the logs folder not exists, the logs files cannot be created!**

**The feature to create the folder automatically has to be added**

### Structure

#### Files

This section will include all the sensitive files that can be founded on a website such as sitemap.xml
and robots.txt.

#### Pages

Each page founded in the website will be analyzed and the information will be reported in the log file
as follows:

##### Title | Url

###### Metadata

All the metadata of the current page

###### Links

List of all the links present on the page

###### Forms and Inputs

If page includes forms / inputs and information about these forms / inputs

###### Cookies

The cookies saved when you are on the page

###### Contacts

By contacts, we mean emails, social link, ecc.
All the information that regard the contacts found in the page

###### Technologies Used

All the technologies that can be detected, e.g. GSAP, ReactJS

###### General Information

Names of people (With the relative role if specified)

# TODOs

- [x] Create `logs` folder automatically
- [x] Update `requirements.txt` and remove unused dependencies
- [ ] Update `README.md` to make it more concise and clear
- [ ] Create proper error handling
- [ ] Add template to create pull requests and add a documentation for contributors