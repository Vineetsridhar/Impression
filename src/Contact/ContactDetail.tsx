import React from "react";
import { User } from "../helpers/interfaces";
import { View, Text } from "react-native";

export default function ContactDetail({ user }: { user: User }) {
  return (
    <View>
      {Object.keys(user).map((key) => (
        <Text>{user[key]}</Text>
      ))}
    </View>
  );
}
