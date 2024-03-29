# Custom Mailing Client
This is a console application that reads a CSV (\*.csv) file and fetches email addresses & other information. Then it sends a personalized email to each email address according to the fetched information. You'll just have to choose an email template and log in to your email account.
**[`Download`](https://github.com/sakibhossain323/Custom-Mailing-Client/releases)**
## User Guide
Suppose you are receiving responses of an event in a google form. You want to send each participant a personalized email which will contain their respective information. In such cases, you can download the responses as a CSV (\*.csv) file and use this app. You can also create your own CSV file and use that. But remember that the first row of your CSV file will be treated as the names of the fields/columns. These field/column names will be used as variables in the email template. Now let's see how to send personalized emails using this app step by step:
1. At first run `Custom Mailing Client.exe` then a command line window will pop up.
2. If the app can establish a connection with the SMTP server, a file dialog box will pop up. It will ask you to select a CSV (\*.csv) file from your pc.
3. After selecting the CSV file, the number of fields & records in that file will be displayed. The field that contains email addresses will also be displayed.
4. If there are multiple fields containing email addresses, a list of those fields will be displayed. You will be asked to insert a number to select one of those fields.
5. Then another file dialog box will pop up. This will ask you to select a text document (\*.txt) file. The text file should contain the subject of the email and a template for the body.
6. The first line of the text file will be treated as the subject of the email. From the second line upto the end of the file will be treated as a template for the body.
7. You can use variables in the template to personalize the email body for each recipient. Variables are expressed with `%{}%` in the template. For an example: 

    `Hi, Mr. %{Last Name}%, good afternooon!` Here **`%{Last Name}%`** is a variable in the template and **`Last Name`** is the name of the field/column of your CSV file. The app will replace the variable with the data of that field for each recipient. Thus you can send an email to each person by mentioning his/her name.
8. If every variable of your template is valid, you will be asked to log in to your gmail account.
9. Before logging in, make sure that you have allowed less secure apps in your gmail account.
10. After logging in, press `Enter` to confirm you want to send emails. Then emails will be sent to everyone automatically. 
11. A `Logs` folder will be generated in the current directory of the app. There will be an `emails_sent.log` file. It contains your email sending history. If any problem occurs during sending an email, you can find here how many emails were sent successfully.
## Errors
Instructions are provided for most of the common issues instantly. But you may face unexpected or unresolved error sometimes as this application is still under development. If you face such errors, checkout `errors.log` file under the `Logs` folder.
## Limitations
As this application is still under development, it has some limitations till now. These are:
1. It can send emails with only plain text. Styling or formatting text is not possible yet.
2. It cannot send any attachments yet.
3. You can only send emails from gmail account till now.  
