# shopui

This is a small school project on the subject "Experimentierlabor LAMP Stack". 
The goal was to learn how to and experiment with accessing a database from python scripts
launched by Apache via CGI. 

The final exercise was to create some visualizations for customer data (and to first import that into the database). For this, a small VueJS application dubbed "ShopUI" has been created. It uses VueUse, TailwindCSS and PrimeVue (which internally uses Graph.js) to create a UI with some visualizations.
For simplicity, the backend still uses Apatche for static file hosting and Python CGI scripts as API endpoints for database access via SQLModel.


## Project structure

- ```backend```: The CGI scripts for accessing the database. Should be copied (or symlinked) to be accessible under the ```/api/``` route.
- ```shopui```: The VueJS project for the frontent. The build artifacts should be copied/symlinked to the webroot.
- ```test_exerciese```: All the initial test exercises for accessing the database and using CGI
- ```import_database.py```: Script to import customer data from ```Kundendaten.csv``` into the database.
- ```requirements.txt```: Dependencies of the CGI scripts. Make sure these are accessible somehow (e.g. with the script interpreter hack mentioned in the docs)


## Project Setup

```sh
cd shopui
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```
