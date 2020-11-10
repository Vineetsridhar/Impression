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


# Setup
NOTE: This was needed for me on ubuntu linux, proceed with caution. May delete these steps if not needed.

1. Run the commands `node -v` and `npm -v` to verify you have the latest versions of node and npm installed. If not updated, update with the commands `npm install -g npm`.
   NOTE: The app may not run without up to date `node` and `npm` versions. App is confirmed to run on `node   v10.23.0` and `npm 6.14.8` 
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
6. Run `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs` inside of the project directory to install PostGreSQL.

# Setup Expo
1. Install expo by running the command `npm install -g expo-cli`.

# View on web browser
1. Change directories with `cd ~/Impression`.
2. Run the application with `npm run start`.
3. A web browser should open up with the Metro Bundler. If not press `?` in the terminal to display a list of commands for help.
4. Select the `connection` setting `LAN`.
5. Click `Run in web browser`.
6. A debugging page may pop up and overlay the web page, simply close it out with `escape` key or click the `x` on the top right of the web page.

# View on android application
1. Download and open the `Expo` android application on the `Google Play Store`. 
2. Change directories with `cd ~/Impression`.
3. Run the application `npm run start`.
4. A web browser should open up with the Metro Bundler. If not press `?` in the terminal to display a list of commands for help.
5. Select the `connection` setting `Tunnel`.
   NOTE: `Tunnel` may take some time to load. Refer to the terminal output and/or `Metro Bundler` output to know when tunneling is complete.
6. When `Tunnel` connection is complete, use the `Expo` app to scan the QR code that appears in the terminal or web page. The app should should now appear on your android devices screen.
