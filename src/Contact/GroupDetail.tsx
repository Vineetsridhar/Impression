import React from 'react'
import ContactList from '../components/ContactList'
import { Text, StyleSheet, ScrollView, ToastAndroid, Alert } from 'react-native'
import colors from '../../config/colors'
import font from '../../config/font'
import { Button } from 'react-native-paper'
import * as DocumentPicker from 'expo-document-picker';
import { uploadGroupDocument } from '../helpers/network';
import { leaveGroup } from "../helpers/network";

export default function GroupDetail({ navigation, route }: any) {

  const groupName = route.params.name
  const leaveMsg =
    "Are you sure you want to leave " +
    groupName +
    "'s group?";

  const goToDocs = () => {
    navigation.push("GroupDocuments", { name: route.params.name, groupId: route.params.groupId })
  }

  const emptyFunction = () => {}

  const uploadDoc = async (file: DocumentPicker.DocumentResult) => {
    if (file != null) {
      uploadGroupDocument(file, route.params.groupId).then(response => response.json()).then(json => {
        if (json["success"]) {
          ToastAndroid.show("Your document has been shared with the group", ToastAndroid.LONG);
        } else {
          throw "error"
        }
      }).catch(() => {
        ToastAndroid.show("There was an error uploading your document", ToastAndroid.LONG);
      })
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

  const handleLeaveGroupAlert = () => {
    Alert.alert("Canceling Leave Group", leaveMsg, [
      {
        text: "Cancel",
        onPress: () => console.log("Canceling Leave Group"),
        style: "cancel",
      },
      {
        text: "OK",
        onPress: handleLeaveGroup,
      },
    ]);
  };

  const handleLeaveGroup = () => {
    leaveGroup(route.params.groupId, route.params.name)
      .then((result) => result.json())
      .then((responseData) => {
        console.log(responseData);
        navigation.pop()
      });
  };
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>{route.params.name}</Text>
      <ContactList
        contacts={route.params.data}
        setButtonVisible={emptyFunction}
        selected={new Set<number>()}
        setSelected={emptyFunction}
        isSelection={false}
        setIsSelection={emptyFunction} />
      <Button onPress={documentFetch}>Upload shared document</Button>
      <Button onPress={goToDocs}>View shared documents</Button>
      <Button onPress={handleLeaveGroupAlert}>Leave Group</Button>
    </ScrollView>
  )
}

const styles = StyleSheet.create({
  title: {
    width: "100%",
    textAlign: "center",
    fontSize: 30,
    fontFamily: font.bold,
    color: colors.text,
    marginVertical: 16,
  },
  container: { backgroundColor: colors.background, flex: 1 },
});
