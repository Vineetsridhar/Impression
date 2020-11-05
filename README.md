# Project3 - Impression

# About
TODO

# Setup
NOTE: This was needed for me on ubuntu linux, proceed with caution. May delete these steps if not needed.

1. Run the commands `node -v` and `npm -v` to verify you have the latest versions of node and npm installed. If not updated, update with the commands `npm install -g npm`.
   NOTE: The app may not run without up to date `node` and `npm` versions. App is confirmed to run on `node   v10.23.0` and `npm 6.14.8` 
2. Add your PATH to your `~/.profile` with `echo "export PATH=$PATH:~/.npm-global/bin" >> ~/.profile`.
3. To avoid having to source `~/.profile` upon terminal startup, run the command `echo "source ~/.profile" >> ~/.bashrc`

# Installs Needed
1. Install React Native Elements `npm install react-native-elements`. This is required for using `Avatar` for User Profile Image.
2. Install prop-types `npm i -S prop-types`. This is used for validating props of Contact component.
3. Install Typescript `npm install -g typescript`.

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
