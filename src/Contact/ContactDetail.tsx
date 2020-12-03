import React from "react";
import { User } from "../helpers/interfaces";
import { ScrollView, View, Text, Image, TouchableOpacity, Linking, Alert } from "react-native";
import { Appbar } from 'react-native-paper';
import { Ionicons, FontAwesome } from "@expo/vector-icons";
import { useNavigation } from "@react-navigation/native";
import avatar from "../../config/avatar";
import styles from "./ContactDetailStyle";
import colors from '../../config/colors';
import ContactDetailRow from "../components/ContactDetailRow";
import LinkImage from "./LinkImage";
import { deleteConnection, getConnections } from "../helpers/network";

const iconMap = {
  "email": "envelope",
  "organization": "building",
  "descr": "pencil",
  "gen_link_1": "github",
  "gen_link_2": "linkedin",
  "gen_link_3": "link"
}
const itemKeys = {
  "email": "Email",
  "organization": "School/Organization",
  "descr": "About",
}
const wantedRows = ["email", "descr", "organization"]
const links = ["gen_link_1", "gen_link_2", "gen_link_3"]

export default function ContactDetail({ route }: { route: any }) {
  const { user }: { user: User } = route.params;
  const navigation = useNavigation();

  const deleteContact = () => {
    deleteConnection(user.email)
    .then(result => result.text())
    .then(responseData => {
      console.log(responseData);
    })
  }
  const isUrl = (url: string) => {
    //Got from https://stackoverflow.com/questions/5717093/check-if-a-javascript-string-is-a-url
    var res = url.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
    return (res !== null)
  }

  const openResume = () => {
    const link = `https://impression-app.s3.amazonaws.com/${user.email.replace(
      "@",
      "%40"
    )}/resume.pdf`;

    Linking.canOpenURL(link).then(canOpenURL => {
      if (canOpenURL) {
        Linking.openURL(link)
      } else {
        Alert.alert("Error", "Cannot open URL")
      }
    })
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
      <View style={{ width: '100%', marginTop: 15 }}>
        <Appbar.Header style={{ backgroundColor: 'white' }} >
          <Appbar.BackAction onPress={() => { navigation.navigate("Contacts"); }} />
          <Appbar.Content title="Contact Details" />
          <Appbar.Action icon="archive" type="entypo" onPress={deleteContact} />
        </Appbar.Header>
      </View>

      <Image
        style={{ width: 200, height: 200, borderRadius: 100, marginTop: 10 }}
        source={{ uri: user["image"] || avatar }}
      />

      <Text style={styles.title}>
        {user["first_name"]} {user["last_name"]}
      </Text>

      {wantedRows.map((key, i) => user[key] ? <ContactDetailRow itemKey={itemKeys[key] || "Some"} key={i} text={user[key]} /> : null)}

      <TouchableOpacity style={{ width: '100%', height: 100 }} onPress={openResume}>
        <Text style={styles.link}>Download Resume</Text>
      </TouchableOpacity>

      <View style={styles.linksContainer}>
        {links.map((link, i) => <LinkImage position={i} link={user[link]} />)}
      </View>
    </ScrollView>
  );
}
