import React, { useEffect, useState } from "react";
import { View, Text, TextInput } from "react-native";
import styles from "./ContactsStyle";
import Contact from "../components/Contact";
import ContactList from "../components/ContactList";
import { User } from "../helpers/interfaces";
import { getConnections } from "../helpers/network";
import user from "../../config/user";
import { TouchableOpacity } from "react-native-gesture-handler";
import colors from '../../config/colors'
import { FontAwesome } from "@expo/vector-icons";
import { Appbar } from 'react-native-paper';

export default function ContactScreen({ navigation }: any) {
  //Add on tab focus listener to refresh data
  const [userConnections, setUserConnections] = useState<User[]>([]);
  const [companyConnections, setCompanyConnections] = useState<User[]>([]);
  const [keyword, setKeyword] = useState("");

  let focusListener: () => {};

  const totalConnected = "Total Contacts: " + (parseInt(userConnections.length) + parseInt(companyConnections.length));

  const _handleSearch = () => {
    console.log(
      "TODO add drop down menu or some other feature that allows user to choose from contacts displayed, " +
      "this will navigate them to the selected users Contact Details page"
    );
    console.log(keyword);

    if(keyword === "") return;
    var kw = keyword;
    kw = kw.toLowerCase();
    var names: string[] = [];

    for (var user of userConnections) {
      var fname = user["first_name"].toLowerCase();
      if (fname.includes(kw)) names.push(user["first_name"]);
    }
    setKeyword("");
    console.log(names);
  };

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
    <View style={{ width: '100%', marginTop: 15 }}>
    <Appbar.Header>
      <Appbar.Content title="Contacts" subtitle={totalConnected}/>
      <View>
        <TextInput
          clearButtonMode="always"
          placeholder="Search Connections"
          placeholderTextColor='white'
          style={{color: 'white'}}
          onChangeText={(value) => setKeyword(value)}
          value={keyword}
          />
      </View>
      <Appbar.Action icon="magnify" onPress={_handleSearch} />
    </Appbar.Header>
    </View>
      <View style={{ flex: 2 }}>
        <FontAwesome name="building" size={60} color={colors.text} />
        <ContactList contacts={companyConnections} />
      </View>
      <View style={{ flex: 2 }}>
        <FontAwesome name="users" size={60} color={colors.text} />
        <ContactList contacts={userConnections} />
      </View>
    </View>
  );
}
