# Day 057 - Templating with Jinja in Flask Applications
 
## Goals
- Using Jinja to Produce Dynamic HTML Pages
- Challenge_ Combining Jinja Templating with APIs
- Multiline Statements with Jinja
- URL Building with Flask

## guess_age_gender(name)
- Set up a route 'to/guess/some_name'
- Extract the name at the end of the URL 
- Make two API calls to [Genderize](https://api.genderize.io) and [Agify](https://api.agify.io) to guess the age and gender
- Insert the result from the API call into the template
- Generate an HTML with the results

## get_blog(num)]
- Multiline statements with Jinja
- Pass a json from the server and get data from the json in html with Jinja
- Render the json data when html file is opened

## [Blog Templating](blog-templating)
- Use Flask Jinja, API to create a blog website
- Get data with API request call
- Display posts title and subtitle in the home page
- Open post and display all other data