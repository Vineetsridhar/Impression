# Project3 - Impression

# About
TODO

# Setup
NOTE: This was needed for me on ubuntu linux, proceed with caution. May delete these steps if not needed.

1. Run the commands `node -v` and `npm -v` to verify you have the latest versions of node and npm installed. If not updated with the commands ``
2. Add your PATH to your `~/.profile` with `echo "export PATH=$PATH:~/.npm-global/bin" >> ~/.profile`.
3. To avoid having to source `~/.profile` upon terminal startup, run the command `echo "source ~/.profile" >> ~/.bashrc`

# Setup Expo
1. Install expo by running the command `npm install -g expo-cli`.

# View on web browser
1. Change directories with `cd ~/Impression`.
2. Run the application with `npm run start`.
3. A web browser should open up to view the application. If not press `?` in the terminal to display a list of commands.

# View on android application
1. Download and open the `Expo` android application on the `Google Play Store`. 
2. Change directories with `cd ./Impression`.
3. Run `npm install`
4. Run the application `npm run start`.
5. Use the `Expo` app to scan the QR code that appears in the terminal or web page.
