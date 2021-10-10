# Impression
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

# Setup

### Clone the Repo
1. In your desired directory run the command `git clone https://github.com/Impression-App/Impression-Sprint2.git`

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
8. When the connection is complete, use the `Expo` app to scan the QR code that appears in the terminal or web page. The app should now appear on your android devices screen.
