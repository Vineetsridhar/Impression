import React from "react";
import { View, Text, Image, ScrollView } from "react-native";
import { Avatar } from "react-native-elements";
import avatar from "../../config/avatar";
import styles from "../Contact/ContactsStyle";

function Contact({ name }: { name: string }) {
  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "flex-start" }}
    >
      <View style={styles.rowContainer}>
        <Image style={styles.avatarStyle} source={{ uri: avatar }} />
        <View style={{ flexDirection: "column" }}>
          <Text>{name}</Text>
          <Text>{name}</Text>
          <Text>{name}</Text>
        </View>
      </View>
    </ScrollView>
  );
}

export default Contact;
