import React, { useEffect, useState } from 'react';
import { Text, View, ToastAndroid, StyleSheet, Linking, Alert } from 'react-native';
import { Document } from '../helpers/interfaces'
import { FlatList, TouchableOpacity } from 'react-native-gesture-handler';
import { getGroupDocuments } from '../helpers/network';
import colors from '../../config/colors';
import { Ionicons } from '@expo/vector-icons'; 
import font from '../../config/font';

interface props {
    route: any
}
export default function SharedDocument({ route }: props):JSX.Element {

    const [documents, setDocuments] = useState<Document[]>([]);

    useEffect(() => {
        getGroupDocuments(route.params.groupId).then(response => response.json()).then(json => {
            if (json["success"]) {
                setDocuments(json["response"])
            } else {
                ToastAndroid.show("Error getting group docs data", ToastAndroid.LONG);
            }
        })
    }, [])

    const openLink = (link:string) => {
        Linking.canOpenURL(link).then((canOpenURL) => {
            if (canOpenURL) {
              Linking.openURL(link);
            } else {
              Alert.alert("Error", "Cannot open URL");
            }
          });
    }

    const documentItem = ({ item }: { item: Document }) => {
        return (
            <TouchableOpacity style={styles.item} onPress={() => openLink(item.url)}>
                <Ionicons name="md-cloud-download" size={40} color={colors.main} />
                <Text style={styles.text}>{item.name}</Text>
            </TouchableOpacity>
        )
    }
    return (
        <View style={styles.container}>
            <FlatList
                data={documents}
                renderItem={documentItem} />
        </View>
    )
}

const styles = StyleSheet.create({
    container:{
        backgroundColor:colors.background,
        padding:16,
        flex:1
    },
    item:{
        display:'flex',
        flexDirection:'row',
        alignItems:'center'
    },
    text:{
        fontFamily: font.regular,
        fontSize: 20,
        paddingHorizontal: 16
    }
})