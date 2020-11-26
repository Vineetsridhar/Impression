import React from "react";
import { View, Text, Image, ScrollView, TouchableOpacity } from "react-native";
import avatar from "../../config/avatar";
import styles from "../Contact/ContactsStyle";
import colors from '../../config/colors'
import { User } from "../helpers/interfaces";
import { useNavigation } from "@react-navigation/native";
import { FontAwesome } from "@expo/vector-icons";


function Group({ group }: { group: Group }) {
  /**
  TODO: for GroupDetails
  const navigation = useNavigation();
  const navigateToContactDetail = () => {
    navigation.navigate("ContactDetail", { user: contact });
  };
  **/
  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "flex-start" }}
    >
      <TouchableOpacity style={styles.rowContainer} onPress={() => console.log("TODO, add Group Detail Page")}>
        <View style={styles.innerContainer}>
          <View style={{ flexDirection: "column" }}>
            <Text style={[styles.mainTextStyle]}>{group.group_name}</Text>
          </View>
        </View>

        <FontAwesome
          name="angle-right"
          type="font-awesome"
          color={colors.main}
          size={40}
          style={{ marginRight: 8 }}
        />

      </TouchableOpacity>
    </ScrollView>
  );
}

export default Group;
