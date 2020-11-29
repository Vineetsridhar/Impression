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


  return (
    <TouchableOpacity style={styles.rowContainer} onPress={() => {
      getUserFromGroups(group.group_name).then(res => res.json()).then(json => {
        navigation.navigate("GroupDetail", { data: json["response"], name: group.group_name });
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

