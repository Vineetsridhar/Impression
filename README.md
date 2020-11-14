# Project3 - Impression

# About

COVID-19 has had a big impact on daily life. One aspect that was immediately affected by the virus was academics.
With the need of everything becoming virtual, students have been taking their education at home from their laptops and/or mobile devices.
All activities and events that students usually participated in were made virtual, as well, including career fairs and recruitment opportunities.
Due to this, recruiters and students struggle to find ways to make a virtual connection to be as successful as an in-person one;
it has become an arduous task for recruiters and applicants to exchange information. This is where our application, Impression, comes in.

By giving each user a unique QR code to scan, Impression will allow the user to make connections on the spot through their mobile devices.
These connections will add users to each other's contact list and store the users' personal information, like how to contact them, resume, links to personal websites, etc.
Companies will be able to attach any important documents about their mission statement, open positions, or any other information they want be made readily available.
Impression will allow for a seamless exhcange of information between users and will reduce the amount of paper often used during career fairs and/or interviews,
as all the information will be stored virtually for the users to revisit if need be.

# Disclaimer

- Because Heroku takes a while to start up on the first launch, when the application is first launched, it might take a while to actually respond


# Setup

### Clone the Repo
1. In your desired directory run the command `git clone https://github.com/Impression-App/Impression.git`

NOTE: The steps below were needed for on `Ubuntu Linux` and may not be needed for everyone, proceed with caution. May ignore these steps if you have the latest versions of `node` and `npm` working.

1. Run the commands `node -v` and `npm -v` to verify you have the latest versions of node and npm installed. If not updated, update with the commands `npm install -g npm`.
   NOTE: The app may not run without up to date `node` and `npm` versions. App is confirmed to run on `node v10.23.0` and `npm 6.14.8`
2. Add your PATH to your `~/.profile` with `echo "export PATH=$PATH:~/.npm-global/bin" >> ~/.profile`.
3. To avoid having to source `~/.profile` upon terminal startup, run the command `echo "source ~/.profile" >> ~/.bashrc`

# Installs Needed

1. Run `npm install` inside of the project directory. This will install all required packages in the project.
2. Run `[sudo] pip[3] install flask` inside of the project directory to install flask.
3. Run `[sudo] pip[3] install flask-socketio` inside of the project directory to install flask-socketio.
4. Run `[sudo] pip[3] install Flask-SQLAlchemy==2.1` inside of the project directory to install SQLAlchemy.
5. Run `python -m pip install requests` inside of the project directory to install Requests.
6. Run `[sudo] pip[3] install psycopg2` inside of the project directory to install Psycopg.
   NOTE: If errors occur try running `[sudo] pip[3] install psycopg2-binary` instead.
7. Run `[sudo] pip[3] install pyqrcode` inside of the project directory to install pyqrcode.
8. Run `[sudo] pip[3] install boto3` inside of the project directory to install boto3.
9. Run `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs` inside of the project directory to install PostGreSQL.

# Set Up Environment Variables (Windows 10)
1. Press the `windows` key followed by the `r` key.
2. When the window pops up click `OK`.
3. Switch to the `Advanced` tab and navigate to the `Environment Variables`.
4. All `Variable`'s and `Value`'s will be inserted in the `User variables for user` section.
5. Refer to `https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html` to obtain your appropiate `Value` for each of the       `Variable`'s listed below.

   `AWS_ACCESS_KEY_ID`
   `AWS_DEFAULT_REGION`
   `AWS_SECRET_ACCESS_KEY`
6. Insert your `postgres url` `Variable` and `Value`

   `DATBASE_URL`
   `postgres://{user}:{password}@{hostname}:{port}/{database-name}`
    
# Setup IP Address
1. Navigate to the `helpers` folder `cd ~/Impression/src/helpers`.
2. Open the file `network.tsx`.
3. On line `4` you will see `const url = "http://XXX.XXX.X.XX:8080";`, replace the `X`'s with your IPV4 address.
   Obtain your IP address through the Linux command `hostname -I` or Windows command `ipconfig`.
4. Open the file `socket.tsx`.
5. Repeat `step 3` except for the value `const socket` on line `3`.

# Setup Expo

1. Install expo by running the command `npm install -g expo-cli`.

# View on Expo

1. On an android mobile device download and open the `Expo` app on the `Google Play Store`.
2. Back on your pc, open a terminal and change directories with `cd ~/Impression/Backend`.
3. Run the command `python server.py` to start the server.
4. In another terminal, change directories with `cd ~/Impression`.
5. Run the application `npm run start`.
6. A web browser should open up with the Metro Bundler. If not press `?` in the terminal to display a list of commands for help.
7. Select the `connection` setting `LAN`.
8. When the connection is complete, use the `Expo` app to scan the QR code that appears in the terminal or web page. The app should should now appear on your android devices screen.

# Linting

For linting, we decided to ignore these errors/warnings:

1. E1101 (no-member) for all python files that have to do with the SQLAlchemy instances
2. R0902 (too-many-instance-attributes) because we need that many instances for our project
3. R0903 (too-few-public-methods) because we just need these classes to store data
4. R0913 (too-many-arguments) because our table needs those specific arguments for the users information
5. R1710: (inconsistent-return-statements) because we need to return that specific statement there for upload
6. C0114 (missing-module-docstring)/C0115 (missing-class-docstring)/C0116 (missing-function-docstring) because
   we do not have docstrings for our modules/classes/functions
7. C0413 (wrong-import-position) because we need the import statements after the 'db.session.commit()' in server.py
8. W0611 (unused-import) because we need the imports for SQL Alchemy in those separate python files

# What we did

## Vineet Sridhar

- I built the structure of the application. [Frontend]
  - I created the tabs, and all the pages on the screen
  - I created the Scan screen
  - I also implemented Google login
  - I connected the frontend to the backend, and wrote the calls for the communication between the two.
  
## Chris
- Done
   - Created expo application to initialize the project.
   - Created Profile page for a user.
   - Created Contacts page for People and Organizations.
   - Styled Profile page.
   - Styled Contacts page.
   - Styled Contact Detail page.
   - Updated User’s Profile page based on backend data.
- In Progress (extra features not needed for sprint 1)
   - Add app bar / navigation bar to Contact Detail.
   - Add search feature for a contact.

