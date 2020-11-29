import React from "react";
import { View, Text, TouchableOpacity } from "react-native";
import styles from "../Contact/ContactsStyle";
import colors from '../../config/colors'
import { Group } from "../helpers/interfaces";
import { FontAwesome } from "@expo/vector-icons";


export default function GroupItem({ group }: { group: Group }) {
  /**
  TODO: for GroupDetails
  const navigation = useNavigation();
  const navigateToContactDetail = () => {
    navigation.navigate("ContactDetail", { user: contact });
  };
  **/
  return (
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
      />

    </TouchableOpacity>
  );
}

