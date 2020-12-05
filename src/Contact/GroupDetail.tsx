import React from 'react'
import ContactList from '../components/ContactList'
import { Text, StyleSheet, ScrollView, ToastAndroid } from 'react-native'
import colors from '../../config/colors'
import font from '../../config/font'
import { Button } from 'react-native-paper'
import * as DocumentPicker from 'expo-document-picker';
import { uploadGroupDocument } from '../helpers/network'

export default function GroupDetail({ navigation, route }: any) {
    const goToDocs = () => {
        navigation.push("GroupDocuments", { name: route.params.name })
    }

    const uploadDoc = async (file: DocumentPicker.DocumentResult) => {
        if (file != null) {
            uploadGroupDocument(file).then(response => response.json()).then(json => {
                if(json["success"]){
                    ToastAndroid.show("Your document has been shared with the group", ToastAndroid.LONG);
                } else {
                    throw "error"
                }
            }).catch(err => {
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
    return (
        <ScrollView style={styles.container}>
            <Text style={styles.title}>{route.params.name}</Text>
            <ContactList
                contacts={route.params.data}
                setButtonVisible={() => { }}
                selected={new Set<number>()}
                setSelected={() => { }}
                isSelection={false}
                setIsSelection={() => { }} />
            <Button onPress={documentFetch}>Upload shared document</Button>
            <Button onPress={goToDocs}>View shared documents</Button>
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
