import React, { useState } from "react";
import { View, Text, TouchableOpacity } from "react-native";
import styles from "../Contact/ContactsStyle";
import colors from '../../config/colors'
import { Group, User } from "../helpers/interfaces";
import { FontAwesome } from "@expo/vector-icons";
import { getUserFromGroups } from "../helpers/network";
import { useNavigation } from "@react-navigation/native";


export default function GroupItem({ group }: { group: Group }) {
  const navigation = useNavigation();

  const [users, setUsers] = useState<User[]>([]);

  return (
    <TouchableOpacity style={styles.rowContainer} onPress={() => {
      getUserFromGroups(group.group_name).then(res => res.json()).then(json => {
        setUsers(json["response"]);
        // navigation.navigate("ContactDetail", { user: contact });
      })
    }}>
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

