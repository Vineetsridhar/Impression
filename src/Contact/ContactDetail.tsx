import React from "react";
import { User } from "../helpers/interfaces";
import { View, Text } from "react-native";

export default function ContactDetail({ route }: { route: any }) {
  const { user } = route.params;
  return (
    <View>
      {Object.keys(user).map((key) => (
        <Text>
          {key}: {user[key]}
        </Text>
      ))}
    </View>
  );
}
