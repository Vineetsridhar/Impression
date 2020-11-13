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
          <Image style={styles.avatarStyle} source={{ uri: avatar }} />
          <View style={{ width: 275, flexDirection: "column" }}>
            <Text>{contact.first_name}</Text>
            <Text>{contact.last_name}</Text>
            <Text>{contact.email}</Text>
          </View>
          <View style={{ alignItems: "flex-end" }}>
            <Icon name="arrow-right" size={20} color="black" type="entypo" />
          </View>
        </View>
      </TouchableOpacity>
    </ScrollView>
  );
}

export default Contact;
