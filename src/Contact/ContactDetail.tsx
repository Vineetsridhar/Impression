import React from "react";
import { User } from "../helpers/interfaces";
import { View, Text, StyleSheet, Image } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";
import avatar from "../../config/avatar";
import { Icon } from "react-native-elements";

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
      <View style={styles.infoContainer}>
        <Image
          style={{ width: 100, height: 100 }}
          source={{ uri: user["image"] || avatar }}
        />
      </View>
      <View style={styles.infoContainer}>
        <Text style={{ fontSize: 30, color: "white" }}>
          {user["first_name"]} {user["last_name"]}
        </Text>
      </View>

      <View style={styles.rowContainer}>
        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Icon name="envelope" type="font-awesome" size={30} color="white" />
        </View>

        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Text style={styles.textStyle}>{user["email"]}</Text>
        </View>
      </View>

      <View style={styles.rowContainer}>
        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Icon name="building" type="font-awesome" size={30} color="white" />
        </View>

        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Text style={styles.textStyle}>{user["organization"]}</Text>
        </View>
      </View>

      <View style={styles.infoContainer}>
        <Text style={styles.textStyle}>{user["descr"]}</Text>
      </View>

      <View style={styles.rowContainer}>
        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Icon name="github" type="font-awesome" size={30} color="white" />
        </View>

        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Text style={styles.textStyle}>{user["gen_link_1"]}</Text>
        </View>
      </View>

      <View style={styles.rowContainer}>
        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Icon name="linkedin" type="font-awesome" size={30} color="white" />
        </View>

        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Text style={styles.textStyle}>{user["gen_link_2"]}</Text>
        </View>
      </View>

      <View style={styles.rowContainer}>
        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Icon name="link" type="font-awesome" size={30} color="white" />
        </View>

        <View
          style={{
            flex: 1,
            justifyContent: "flex-start",
            alignItems: "center",
          }}
        >
          <Text style={styles.textStyle}>{user["gen_link_3"]}</Text>
        </View>
      </View>
      {/**Object.keys(user).map((key) => (
          <Text>
          {key}: {user[key]}
          </Text>
      ))**/}
    </View>
  );
}
const styles = StyleSheet.create({
  infoContainer: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  rowContainer: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
  },
  textStyle: {
    fontSize: 20,
    color: "white",
  },
  container: {
    margin: 0,
    flex: 1,
    padding: 16,
    backgroundColor: "#192879",
  },
  icon: {
    marginVertical: 16,
  },
});
