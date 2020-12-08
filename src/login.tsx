import React, { Dispatch, SetStateAction } from "react";
import {
  View,
  Image,
  TouchableOpacity,
  AsyncStorage,
  ToastAndroid,
} from "react-native";
import styles from "./loginstyles";
import * as Google from "expo-google-app-auth";
import { newUser, linkedinLogin } from "./helpers/network";
import user from "../config/user";
import LinkedInModal from 'react-native-linkedin'

interface props {
  setLoggedIn: Dispatch<SetStateAction<boolean>>;
}
export default function Login({ setLoggedIn }: props):JSX.Element {
  const login = (userInfo: any) => {
    newUser(userInfo)
      .then((response) => response.json())
      .then((json) => {
        if (json["success"]) {
          user.email = json["email"];
          AsyncStorage.setItem("email", json["email"]);
          setLoggedIn(true);
        } else {
          console.log("failed?", json);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const initiateGoogleLogin = async () => {
    try {
      const result = await Google.logInAsync({
        androidClientId:
          "997021177023-e8fqpcgg4b7faas9iki043c0t76as4fj.apps.googleusercontent.com",
        androidStandaloneAppClientId:
          "997021177023-vv75tbs6vu4vvjt609jv7hkdpgmnlam6.apps.googleusercontent.com",
        scopes: ["profile", "email"],
      });
      if (result.type === "success") {
        const userInfoResponse = await fetch(
          "https://www.googleapis.com/userinfo/v2/me",
          {
            headers: { Authorization: `Bearer ${result.accessToken}` },
          }
        );
        const json = await userInfoResponse.json();
        login(json);
      } else {
        console.log("Cancelled");
      }
    } catch (err) {
      console.log(err);
    }
  };

  const linkedInButton = () => {
    return (
      <Image source={require('./assets/img/linkedinsignin.png')} style={styles.loginbutton} />
      // <Text>Login with linkedin</Text>
    )
  }

  return (
    <View style={styles.container}>
      <Image source={require('./assets/img/logo.png')} style={styles.avatarStyle} />
      <TouchableOpacity onPress={initiateGoogleLogin}>
        <Image
          source={require("./assets/img/signin.png")}
          style={styles.loginbutton}
        />
      </TouchableOpacity>

      <LinkedInModal
        shouldGetAccessToken={false}
        clientID="78awb6ngzwv3uc"
        redirectUri="https://njit-cs490-project3-impression.herokuapp.com/"
        onSuccess={authentication_code => {
          linkedinLogin(authentication_code)
            .then(data => data.json())
            .then(json => {
              if (json["success"]) {
                user.email = json["email"];
                AsyncStorage.setItem("email", json["email"]);
                setLoggedIn(true);
              } else {
                ToastAndroid.show("Error occured", ToastAndroid.LONG)
              }
            })
        }}
        renderButton={linkedInButton()}
      />
    </View>
  );
}
