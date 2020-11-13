import React from "react";
import { User } from "../helpers/interfaces";
import { View, Text, StyleSheet, Image } from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";
import avatar from "../../config/avatar";

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
        style={{width: 150, height: 150}}
        source={{ uri: user["image"] || avatar }}
      />
      </View>
      <View style={styles.infoContainer}>
          <Text style={{ fontSize: 30 }}>
          {user["first_name"]} {user["last_name"]}
          </Text>
      </View>
      <View style={styles.rowContainer}>
          <View style={{flex: 1, justifyContent: 'flex-start', alignItems: 'center'}}>
          <Text style={{textAlign: 'center'}}>
          {user["email"]}
          </Text>

          </View>
          <View style={{flex: 1, justifyContent: 'flex-end', alignItems: 'center'}}>
          <Text style={{textAlign: 'center'}}>
          {user["organization"] || (user["first_name"] + " is currently not enrolled in a University or involved in any Organizations.")}
          </Text>
          </View>
      </View>
      <View style={styles.infoContainer}>
          <Text style={{textAlign: 'center'}}>
          {user["descr"]}
          </Text>
      </View>
      <View style={styles.infoContainer}>
      <Text style={{textAlign: 'center'}}>
      {user["gen_link_1"]}
      </Text>
      <Text style={{textAlign: 'center'}}>
      {user["gen_link_2"]}
      </Text>
      <Text style={{textAlign: 'center'}}>
      {user["gen_link_3"]}
      </Text>
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
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center'
  },
  rowContainer: {
    flex:1,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center'
  },
  nameContainer: {
    flex: 1,
    flexDirection: 'column'
  },
  container: {
    margin: 0,
    flex: 1,
    padding: 16,
  },
  icon: {
    marginVertical: 16,
  },
});
