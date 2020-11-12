import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  TextInput,
  Image,
  ScrollView,
  TouchableOpacity,
} from "react-native";
import { Avatar } from "react-native-elements";
import styles from "./ProfileStyle";
import avatar from "../../config/avatar";
import FormItem from "../components/FormItem";
import { getUserInfo } from "../helpers/network";
import user from "../../config/user";

export default function ProfileScreen() {
  const [email, setEmail] = useState('email@email');
  const [firstName, setFirstName] = useState('First Name');
  const [lastName, setLastName] = useState('Last Name');

  useEffect(() => {
    getUserInfo(user.email)
      .then((response) => response.json())
      .then((json) => {
        console.log(json);
        setFirstName(json['first_name'])
        setLastName(json['last_name'])
        setEmail(json['email'])
      });
  });
  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "center" }}
    >
      <TouchableOpacity onPress={() => {}}>
        <Image style={styles.avatarStyle} source={{ uri: avatar }} />
      </TouchableOpacity>

      <Text style={styles.title}>Name</Text>
      <View style={styles.rowContainer}>
        <TextInput
          style={[styles.nameStyle, { marginRight: 4 }]}
          placeholder="First Name"
          value={firstName}
        />
        <TextInput
          style={[styles.nameStyle, { marginLeft: 4 }]}
          placeholder="Last Name"
          value={lastName}
        />
      </View>

      <FormItem title="School/Organization" placeholder="NJIT" />
      <FormItem title="Email" value={email} placeholder="email@email.com" />

      <FormItem
        title="About you"
        placeholder="I am a..."
        style={{ height: 100 }}
      />
      <FormItem title="GitHub" placeholder="https://www.github.com" />
      <FormItem
        title="LinkedIn"
        placeholder="https://www.linkedin.com"
        style={{ height: 100 }}
      />
      <TouchableOpacity onPress={() => {}}>
        <Text style={styles.link}>Download Resume</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}
