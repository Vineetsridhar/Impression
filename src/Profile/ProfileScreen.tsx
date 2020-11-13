import React, { useState, useEffect, SetStateAction, Dispatch } from "react";
import {
  View,
  Text,
  TextInput,
  Image,
  ScrollView,
  TouchableOpacity,
  AsyncStorage,
} from "react-native";
import { Avatar } from "react-native-elements";
import styles from "./ProfileStyle";
import avatar from "../../config/avatar";
import FormItem from "../components/FormItem";
import { getUserInfo, editUser } from "../helpers/network";
import user from "../../config/user";
import { User } from "../helpers/interfaces";
import { Icon } from "react-native-elements";

export default function ProfileScreen() {
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [school, setSchool] = useState("");
  const [description, setDescription] = useState("");
  const [github, setGithub] = useState("");
  const [linkedin, setLinkedin] = useState("");
  const [image, setImage] = useState("");

  useEffect(() => {
    getUserInfo(user.email)
      .then((response) => response.json())
      .then((json: User) => {
        setFirstName(json["first_name"] ?? "");
        setLastName(json["last_name"] ?? "");
        setEmail(json["email"] ?? "");
        setSchool(json["organization"] ?? "");
        setDescription(json["descr"] ?? "");
        setGithub(json["gen_link_1"] ?? "");
        setLinkedin(json["gen_link_2"] ?? "");
        setImage(json["image"] ?? "");
      });
  }, []);

  const onChange = (
    text: string,
    callback: Dispatch<SetStateAction<string>>
  ) => {
    callback(text);
  };

  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "center" }}
    >
      <TouchableOpacity onPress={() => {}}>
        {
          image == "" &&
          <Icon style={{marginTop: 50}} name="user" type="font-awesome" size={125} color="white"/>
        }
        {
          image != "" &&
          <Image style={styles.avatarStyle} source={{ uri: image}} />
        }
      </TouchableOpacity>

      <Text style={styles.title}>Name</Text>
      <View style={styles.rowContainer}>
        <TextInput
          style={[styles.nameStyle, { marginRight: 4 }]}
          placeholder="First Name"
          placeholderTextColor="white"
          value={firstName}
          onChangeText={(text) => onChange(text, setFirstName)}
        />
        <TextInput
          style={[styles.nameStyle, { marginLeft: 4 }]}
          placeholder="Last Name"
          placeholderTextColor="white"
          value={lastName}
          onChangeText={(text) => onChange(text, setLastName)}
        />
      </View>

      <FormItem
        title="School/Organization"
        placeholder="NJIT"
        value={school}
        onChangeText={(text) => onChange(text, setSchool)}
      />
      <FormItem
        title="Email"
        value={email}
        placeholder="email@email.com"
        onChangeText={(text) => onChange(text, setEmail)}
      />

      <FormItem
        title="About you"
        placeholder="I am a..."
        style={{ height: 100 }}
        value={description}
        onChangeText={(text: string) => onChange(text, setDescription)}
      />
      <FormItem
        title="GitHub"
        placeholder="https://www.github.com"
        value={github}
        onChangeText={(text: string) => onChange(text, setGithub)}
      />
      <FormItem
        title="LinkedIn"
        placeholder="https://www.linkedin.com"
        value={linkedin}
        style={{ height: 100 }}
        onChangeText={(text: string) => onChange(text, setLinkedin)}
      />
      {/* <TouchableOpacity>
        <Text style={styles.link}>Upload Resume</Text>
      </TouchableOpacity> */}

      <TouchableOpacity
        onPress={() => {
          editUser({
            email,
            first_name: firstName,
            last_name: lastName,
            organization: school,
            descr: description,
            gen_link_1: github,
            gen_link_2: linkedin,
            user_type: "Student",
          });
        }}
      >
        <Text style={styles.link}>Submit</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}
