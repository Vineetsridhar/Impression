import React, { useState, useEffect, SetStateAction, Dispatch } from "react";
import {
  View,
  Text,
  TextInput,
  Image,
  ScrollView,
  TouchableOpacity,
  AsyncStorage,
  Alert,
  ToastAndroid,
} from "react-native";
import styles from "./ProfileStyle";
import avatar from "../../config/avatar";
import FormItem from "../components/FormItem";
import { getUserInfo, editUser, uploadDocument } from "../helpers/network";
import user from "../../config/user";
import { User } from "../helpers/interfaces";
import * as DocumentPicker from 'expo-document-picker';
import colors from '../../config/colors'
import { FontAwesome } from "@expo/vector-icons";


export default function ProfileScreen({ navigation }: any) {
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
        setGithub(json["gen_link_1"].split("/")[3] ?? "");
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

  let uploadDoc = async (file: DocumentPicker.DocumentResult) => {
    if (file != null) {
      uploadDocument(file)
    } else {
      alert('Please Select File first');
    }
  };

  const documentFetch = () => {
    DocumentPicker.getDocumentAsync({
      type: 'application/pdf',
      copyToCacheDirectory: true
    }).then(data => {
      uploadDoc(data)
    })
  }

  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={{ alignItems: "center" }}
    >
      <TouchableOpacity onPress={() => { }}>
        {
          image == "" &&
          <FontAwesome style={{ marginTop: 50 }} name="user" size={125} color={colors.text} />
        }
        {
          image != "" &&
          <Image style={styles.avatarStyle} source={{ uri: image }} />
        }
      </TouchableOpacity>

      <Text style={styles.title}>Name</Text>
      <View style={styles.rowContainer}>
        <TextInput
          style={[styles.nameStyle, { marginRight: 4 }]}
          placeholder="First Name"
          placeholderTextColor={colors.text}
          value={firstName}
          onChangeText={(text) => onChange(text, setFirstName)}
        />
        <TextInput
          style={[styles.nameStyle, { marginLeft: 4 }]}
          placeholder="Last Name"
          placeholderTextColor={colors.text}
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
        title="GitHub Handle"
        placeholder="SomeUsername"
        value={github}
        onChangeText={(text: string) => onChange(text, setGithub)}
      />
      <FormItem
        title="LinkedIn URL"
        placeholder="https://www.linkedin.com"
        value={linkedin}
        style={{ height: 100 }}
        onChangeText={(text: string) => onChange(text, setLinkedin)}
      />
      <TouchableOpacity onPress={documentFetch}>
        <Text style={styles.link}>Upload Resume</Text>
      </TouchableOpacity>

      <TouchableOpacity
        onPress={() => {
          editUser({
            email,
            first_name: firstName,
            last_name: lastName,
            organization: school,
            descr: description,
            gen_link_1: github ? `https://github.com/${github}` : null,
            gen_link_2: linkedin,
            user_type: "Student",
          }).then(() => {
            ToastAndroid.show("Your changes have been saved", ToastAndroid.LONG);
            navigation.navigate("Scan")
          }).catch(err => {
            Alert.alert("Error", "There was an error saving your changes. Please try again later.")
          })
        }}
      >
        <Text style={styles.link}>Submit</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}
