import React, { useEffect, useState } from 'react'
import { Group } from '../helpers/interfaces';
import { Text, View, Alert } from 'react-native';
import GroupList from '../components/GroupList';
import styles from "./ContactsStyle";
import { getGroups } from '../helpers/network';
import user from '../../config/user';

export default function GroupsScreen() {
    const [groupConnections, setGroupConnections] = useState<Group[]>([]);
    useEffect(() => {
        getGroups(user.email).then(response => response.json()).then(json => {
            if (json["success"]) {
                setGroupConnections(json["response"]);
            } else {
                Alert.alert("Error", "There was an error fetching your groups")
            }
        }).catch(err => {
            console.log(err);
            Alert.alert("Error", "There was an error fetching your groups")
        })
    }, []);
    return (
        <View style={styles.container}>
            <GroupList group={groupConnections} />
        </View>
    );
}