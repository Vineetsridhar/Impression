import React, { useEffect } from "react";
import { View, Text, Image, ScrollView, TouchableOpacity } from "react-native";
import avatar from "../../config/avatar";
import styles from "../Contact/ContactsStyle";
import colors from '../../config/colors'
import { User } from "../helpers/interfaces";
import { useNavigation } from "@react-navigation/native";
import { FontAwesome } from "@expo/vector-icons";

interface props {
  contact: User,
  toggleSelection: () => void;
  isSelected: boolean;
  isSelection: boolean
}
function Contact({ contact, isSelected, isSelection, toggleSelection }: props) {
  const navigation = useNavigation();
  const navigateToContactDetail = () => {
    navigation.navigate("ContactDetail", { user: contact });
  };

  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "flex-start" }}
    >
      <TouchableOpacity style={styles.rowContainer} onPress={isSelection ? toggleSelection : navigateToContactDetail} onLongPress={toggleSelection}>
        <View style={styles.innerContainer}>
          <Image style={styles.avatarStyle} source={{ uri: contact["image"] || avatar }} />

          <View style={{ flexDirection: "column" }}>
            <Text style={[styles.mainTextStyle]}>{contact.first_name} {contact.last_name}</Text>
            <Text style={styles.textStyle}>{contact.email}</Text>
            {contact.organization ? <Text style={styles.textStyle}>{contact.organization}</Text> : null}
          </View>
        </View>

        <FontAwesome
          name={isSelected ? "check" : "angle-right"}
          type="font-awesome"
          color={colors.main}
          size={40}
          style={{ marginRight: 8 }}
        />

      </TouchableOpacity>
    </ScrollView>
  );
}

export default Contact;
