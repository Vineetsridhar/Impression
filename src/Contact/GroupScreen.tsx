import React, { useEffect, useState } from 'react'
import { Group } from '../helpers/interfaces';
import { Text, View, Alert } from 'react-native';
import GroupList from '../components/GroupList';
import styles from "./ContactsStyle";
import { getGroups } from '../helpers/network';
import user from '../../config/user';
import { createStackNavigator } from '@react-navigation/stack';
import GroupDetail from './GroupDetail';

function GroupScreen() {
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

const Stack = createStackNavigator();

export default function GroupsScreen() {
    return (
        <Stack.Navigator
            screenOptions={{
                headerShown: false
            }}
        >
            <Stack.Screen name="GroupScreen" component={GroupScreen} />
            <Stack.Screen name="GroupDetail" component={GroupDetail} />
        </Stack.Navigator>

    );
}