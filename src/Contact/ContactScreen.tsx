import React, { useEffect, useState } from "react";
import { View, Text } from "react-native";
import styles from "./ContactsStyle";
import Contact from "../components/Contact";
import ContactList from "../components/ContactList";
import { User } from "../helpers/interfaces";
import { getConnections } from "../helpers/network";
import user from "../../config/user";
import { TouchableOpacity } from "react-native-gesture-handler";
import { Icon } from "react-native-elements";

export default function ContactScreen({ navigation }: any) {
  //Add on tab focus listener to refresh data
  const [userConnections, setUserConnections] = useState<User[]>([]);
  const [companyConnections, setCompanyConnections] = useState<User[]>([]);

  let focusListener: () => {};

  const makeListeners = () => {
    focusListener = navigation.addListener("focus", () => {
      refreshData();
    });
  };

  const refreshData = () => {
    const parseConnections = (allConnections: User[]) => {
      setUserConnections(
        allConnections.filter(
          (connection) => connection.user_type === "Student"
        )
      );
      setCompanyConnections(
        allConnections.filter(
          (connection) => connection.user_type === "Recruiter"
        )
      );
    };

    getConnections(user.email)
      .then((response) => response.json())
      .then((data) => parseConnections(data["connections"]))
      .catch((err) => console.log(err));
  };
  useEffect(() => {
    refreshData();
    makeListeners();
  }, []);
  return (
    <View style={styles.container}>
      <View style={{ flex: 2 }}>
        <Icon name="building" type="font-awesome" size={60} color="white" />
        <ContactList contacts={companyConnections} />
      </View>
      <View style={{ flex: 2 }}>
        <Icon name="users" type="font-awesome" size={60} color="white" />
        <ContactList contacts={userConnections} />
      </View>
    </View>
  );
}
