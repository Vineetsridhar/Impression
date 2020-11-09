import React from "react";
import { View, Text, Image, ScrollView, TouchableOpacity } from "react-native";
import { Avatar, Icon, Button } from "react-native-elements";
import avatar from "../../config/avatar";
import styles from "../Contact/ContactsStyle";
import { createStackNavigator } from '@react-navigation/stack';
import ProfileScreen from '../Profile/ProfileScreen';

function Contact({ name }: { name: string }) {
  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "flex-start" }}
    >
      <TouchableOpacity onPress={console.log("TODO")}>
      <View style={styles.rowContainer}>
        <Image style={styles.avatarStyle} source={{ uri: avatar }} />
	<View style={{ width: 275, flexDirection: "column" }}>
          <Text>{name}</Text>
          <Text>{name}</Text>
          <Text>{name}</Text>
        </View>
	<View style={{alignItems: 'flex-end'}}> 
	  <Icon name="arrow-right" size={20} color="black" type="entypo" />
	</View>
      </View>
      </TouchableOpacity>
    </ScrollView>
  );
}

export default Contact;
