import React, { useEffect, useState } from 'react';
import { Text, View, ToastAndroid } from 'react-native';
import { Button } from 'react-native-paper';
import {Document} from '../helpers/interfaces'
import { FlatList } from 'react-native-gesture-handler';
import { getGroupDocuments } from '../helpers/network';

interface props {
    navigation: any,
    route:any
}
export default function SharedDocument({ navigation, route }: props) {

    const [documents,setDocuments] = useState<Document[]>([]);

    useEffect(() => {
        getGroupDocuments(route.params.groupId).then(response => response.json()).then(json => {
            if(json["success"]){
                setDocuments(json["response"])
            } else {
                ToastAndroid.show("Error getting group docs data", ToastAndroid.LONG);
            }
        })
    }, [])

    const documentItem = ({item}:{item:Document}) => {
        return <Text>{item.name}</Text>
    }
    return (
        <View>
            <FlatList
                data={documents}
                renderItem={documentItem}/>
        </View>
    )
}