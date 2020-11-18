import React from "react";
import { User } from "../helpers/interfaces";
import { ScrollView, View, Text, Image } from "react-native";
import { Ionicons, FontAwesome } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";
import avatar from "../../config/avatar";
import styles from "./ContactDetailStyle";
import colors from '../../config/colors';


export default function ContactDetail({ route }: { route: any }) {
  const { user }: { user: User } = route.params;
  const navigation = useNavigation();
  return (
    <View style={styles.container}>
      <Ionicons
        name="md-arrow-back"
        size={35}
        color={colors.text}
        style={styles.icon}
        onPress={() => {
          navigation.navigate("Contacts");
        }}
      />
      <View style={styles.infoContainer}>
        {user["image"] == "" && (
          <FontAwesome name="user" type="font-awesome" size={100} color={colors.text} />
        )}
        {user["image"] != "" && (
          <Image
            style={{ width: 100, height: 100, borderRadius: 50 }}
            source={{ uri: user["image"] || avatar }}
          />
        )}
      </View>
      <View style={styles.infoContainer}>
        <Text style={{ fontSize: 25, color: colors.text }}>
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
          <FontAwesome name="envelope" type="font-awesome" size={30} color={colors.text} />
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
          <FontAwesome name="building" type="font-awesome" size={30} color={colors.text} />
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
          <Text style={{ fontSize: 15, color: colors.text }}>{user["descr"]}</Text>
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
          <FontAwesome name="github" type="font-awesome" size={30} color={colors.text} />
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
          <FontAwesome name="linkedin" type="font-awesome" size={30} color={colors.text} />
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
          <FontAwesome name="link" type="font-awesome" size={30} color={colors.text} />
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
