import React from "react";
import { View, Text, Image, ScrollView, TouchableOpacity } from "react-native";
import { Avatar, Icon, Button } from "react-native-elements";
import avatar from "../../config/avatar";
import styles from "../Contact/ContactsStyle";
import { User } from "../helpers/interfaces";
import { useNavigation } from "@react-navigation/native";

function Contact({ contact }: { contact: User }) {
  const navigation = useNavigation();
  const navigateToContactDetail = () => {
    navigation.navigate("ContactDetail", { user: contact });
  };

  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "flex-start" }}
    >
      <TouchableOpacity onPress={navigateToContactDetail}>
        <View style={styles.rowContainer}>
          {
            contact["image"] == "" &&
            <Icon name="user" type="font-awesome" size={30} color="white"/>
          }
          {
            contact["image"] != "" &&
            <Image style={styles.avatarStyle} source={{ uri: contact["image"] || avatar}} />
          }
          <View style={{ width: 275, flexDirection: "column" }}>
            <Text style={styles.textStyle}>{contact.first_name}</Text>
            <Text style={styles.textStyle}>{contact.last_name}</Text>
            <Text style={styles.textStyle}>{contact.email}</Text>
          </View>
          <View style={{ alignItems: "flex-end" }}>
            <Icon
              name="angle-right"
              type="font-awesome"
              size={50}
              color="white"
            />
          </View>
        </View>
      </TouchableOpacity>
    </ScrollView>
  );
}

export default Contact;
