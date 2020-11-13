import React from "react";
import { User } from "../helpers/interfaces";
import { View, Text, StyleSheet } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";

export default function ContactDetail({ route }: { route: any }) {
  const { user } = route.params;
  const navigation = useNavigation();
  return (
    <View style={styles.container}>
      <Ionicons
        name="md-arrow-back"
        size={35}
        color="black"
        style={styles.icon}
        onPress={() => {
          navigation.navigate("Contacts");
        }}
      />
      {Object.keys(user).map((key) => (
        <Text>
          {key}: {user[key]}
        </Text>
      ))}
    </View>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  icon: {
    marginVertical: 16,
  },
});
