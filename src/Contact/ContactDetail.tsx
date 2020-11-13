import React from "react";
import { User } from "../helpers/interfaces";
import { ScrollView, View, Text, StyleSheet, Image } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";
import avatar from "../../config/avatar";
import { Icon } from "react-native-elements";
import styles from "./ContactDetailStyle.tsx";

export default function ContactDetail({ route }: { route: any }) {
  const { user } = route.params;
  const navigation = useNavigation();
  return (
    <View style={styles.container}>
      <Ionicons
        name="md-arrow-back"
        size={35}
        color="white"
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
        <ScrollView style={styles.scrollView}>
          <Text style={{fontSize: 15, color: 'white'}}>{user["descr"]}</Text>
        </ScrollView>
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
