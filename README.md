# Custom Mailing Client
This is a desktop application that reads a CSV (\*.csv) file and fetches email adresses & other information. Then it sends a personalized email to each email adrress according to the fetched information. You'll just have to choose an email template and login to your email account.
## User Guide
Suppose you are receiving responses of a event in a google form. You want to send each participant a personalized email which will contain their respective information. In such cases, you can download the responses as a CSV (\*.csv) file and use this app. You can also create your own CSV file and use that. But remember that the first row of your CSV file will be treated as the names of the fields/columns. These field/column names will be used as variables in email template. Now let's see how to send personalized emails using this app step by step:
1. Run `Custom Mailing Client.exe` then A command line window will pop up.
2. If the app can establish connection with SMTP server, a file dialog box will pop up. It will ask you to select a CSV `(\*.csv)` file from your pc.
3. After selecting the CSV file, number of fields & records in that file will be displayed. The field that contains email addresses will also be displayed.
4. If there are multiple fields containing email addresses, list of those fields will be displayed. You will be asked to insert a number to select one those fields.
5. Then another file dialog box will pop up. This will ask you to select a text document (\*.txt) file. The text file should contain subject of email & a template for the body.
6. The first line of the text file will be treated as subject of the email. From second line to end of the file will be treated as template for the body.
7. You can use variables in template to personalize email body for each recipient. Variables are expressed with `%{}%` in the template. For an example: 

    `Hi, Mr. %{Last Name}%, good afternooon!` Here **`%{Last Name}%`** is a variable in the template and **`Last Name`** is the name of field/column of your CSV file. The app will replace the variable with the data of that field for each recipient. Thus you can send email each person by mentioning his/her name.
8. If every variable of your template is valid, you will be asked to login to your gmail account.
9. Before logging in, make sure that you have allowed less secure app in your gmail account.
10. After logging in, press `Enter` to confirm you want to send emails. Then emails will be sent to everyone automatically. 
11. A `Logs` folder will be generated. There will an `emails_sent.log` file. It contains your email sending history. If any problem occurs during sending email, you can find here how many emails were sent successfully.
12. Errors may occur while running the app due to different issues. Learn more about these in the **Errors** section below.
