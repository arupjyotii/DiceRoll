**Dice Roller** 


This Flask application simulates rolling a dice and displays the outcome along with a dice logo. It also includes a "Refresh" button to reset the dice rolling functionality.

Running the Flask Application:

1. Clone the Repository:
   - Clone this repository to your local machine.

2. Install Flask:
   - Make sure you have Python installed on your system.
   - Install Flask using pip:
     ```
     pip install Flask
     ```

3. Run the Application:
   - Navigate to the directory where the repository is cloned.
   - Run the Flask application:
     ```
     python app.py
     ```

4. Access the Application:
   - Open a web browser and go to http://127.0.0.1:5000/ to access the application.
   - You should see the Flask Dice Roller application running.

Explanation of Files:

1. app.py:
   - This is the main Python script that defines the Flask application.
   - It contains the Flask routes for handling requests and rolling the dice.

2. templates/index.html:
   - This HTML template file defines the structure of the web page.
   - It includes placeholders for displaying the dice roll outcome and buttons for rolling the dice and refreshing the page.

3. static/style.css:
   - This CSS file contains styles for styling the HTML elements.
   - It defines the appearance of the web page, including the background color, font styles, and button styles.

4. dice-logo.png:
   - This is the image file for the dice logo displayed on the web page.

How the Application Works:

- When you run the Flask application, it starts a web server locally on port 5000.
- The HTML template defines the layout of the web page, including placeholders for displaying the dice roll outcome.
- When you click the "Roll Dice" button, a JavaScript function sends a request to the Flask server.
- The Flask server generates a random dice roll outcome and sends it back to the client.
- The JavaScript function updates the web page with the dice roll outcome.
- You can click the "Refresh" button to reset the dice rolling functionality and start over.

This README provides an overview of how to run the Dice Roller application and explains how it works. If you have any questions or issues, feel free to contact the developer.
