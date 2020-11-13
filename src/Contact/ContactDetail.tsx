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
      <View style={styles.infoContainer}>
          <Text>
          Image here
          </Text>
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
          testorg/school{user["organization"]}
          </Text>
          </View>
      </View>
      <View style={styles.infoContainer}>
          <Text style={{textAlign: 'center'}}>
          This is just a holder for now.
          The actual description is here but is blank because it has no value yet.
          So this is here for now. This is the same for the school/org and links.
          {user["descr"]}
          </Text>
      </View>
      <View style={styles.infoContainer}>
      <Text style={{textAlign: 'center'}}>
      Link1 goes here: {user["gen_link_1"]}
      </Text>
      <Text style={{textAlign: 'center'}}>
      Link2 goes here: {user["gen_link_2"]}
      </Text>
      <Text style={{textAlign: 'center'}}>
      Link3 goes here: {user["gen_link_3"]}
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
