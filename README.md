<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Property_management" />

  &#xa0;

  <!-- <a href="https://property_management.netlify.app">Demo</a> -->
</div>

<h1 align="center">Property_management</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{xinbow99}}/property_management?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{xinbow99}}/property_management?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{xinbow99}}/property_management?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/{{xinbow99}}/property_management?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{xinbow99}}/property_management?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{xinbow99}}/property_management?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{xinbow99}}/property_management?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Property_management 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{xinbow99}}" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

This is a property management system that follows the Model-View-Controller (MVC) architecture. It allows users to manage their properties and tenants through a web interface.

The project is built using FastAPI and SQLAlchemy. The database is SQLite.

The Model component defines the data structures and interacts with the database using SQLAlchemy. The View component consists of the API routes defined in FastAPI, which receive HTTP requests and communicate with the Controller. The Controller processes the data and communicates with the Model to retrieve or modify data.

Notably, the code was initially generated by ChatGPT and subsequently modified by a developer to implement the MVC architecture and fix any bugs.

The project can be run locally by installing the dependencies listed in requirements.txt and running the main.py file. The API documentation is available at http://localhost:8000/docs when the server is running.

## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##

The following tools were used in this project:
- [Python](https://www.python.org/)
- [ChatGPT](https://chat.openai.com/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/{{xinbow99}}/property_management

# Access
$ cd property_management

# Install dependencies
$ pip install -r requirements.txt

# Create the database
$ python gen_database.py

# Run the project
$ uvicorn app.main:app --reload

# The server will initialize in the <http://localhost:8000>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/{{xinbow99}}" target="_blank">{{Xinbow99}}</a>

&#xa0;

<a href="#top">Back to top</a>
