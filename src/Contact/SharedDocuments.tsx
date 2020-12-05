import React, { useEffect, useState } from 'react';
import { Text, View } from 'react-native';
import { Button } from 'react-native-paper';
import {Document} from '../helpers/interfaces'
import { FlatList } from 'react-native-gesture-handler';

interface props {
    navigation: any
}
export default function SharedDocument({ navigation }: props) {

    const [documents,setDocuments] = useState<Document[]>([]);

    useEffect(() => {
        //Make call to fetch all group docs
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