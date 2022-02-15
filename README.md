# Custom CSV-exporter for NBGrader
# Usage:
1. Open a new terminal on your Jupyter Server
2. Run the command ```git clone https://github.com/lauri3k/csvExport.git``` to copy the exporter to your server.
3. Move to the new folder using ```cd csvExport```
4. Copy the file 'list_of_students.csv' to the folder*
5. Run the command ```nbgrader export --exporter=csv.CsvExport``` to export the grades. This will generate a new file 
called 'grades.csv'.

*The exporter expects there to be a 'list_of_students.csv' containing the columns Etternavn, Fornavn, Brukernavn and 
Student-ID.