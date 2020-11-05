import React, { useEffect, Dispatch, SetStateAction } from 'react';
import { Text, View, Image, TouchableOpacity } from 'react-native';
import styles from './loginstyles';
import avatar from '../config/avatar';
import * as Google from 'expo-google-app-auth';


interface props {
    setLoggedIn: Dispatch<SetStateAction<boolean>>;
}
export default function Login({ setLoggedIn }: props) {

    const login = (userInfo:any) => {
        //TODO add to db or something
        setLoggedIn(true)
    }

    const initiateGoogleLogin = async () => {
        try {
            
            const result = await Google.logInAsync({
                androidClientId: "997021177023-e8fqpcgg4b7faas9iki043c0t76as4fj.apps.googleusercontent.com",
                scopes: ["profile", "email"],
            });
            if (result.type === 'success') {
                let userInfoResponse = await fetch('https://www.googleapis.com/userinfo/v2/me', {
                    headers: { Authorization: `Bearer ${result.accessToken}` },
                });
                let json = await userInfoResponse.json();
                login(json);
            } else {
                console.log("Cancelled")
            }
        } catch (err) {
            console.log(err)
        }
    }

    return (
        <View style={styles.container}>
            <Image source={{ uri: avatar }} style={styles.avatarStyle} />
            <TouchableOpacity onPress={initiateGoogleLogin}>
                <Image source={require('./assets/img/signin.png')} style={styles.loginbutton}/>
            </TouchableOpacity>
        </View>
    )
}