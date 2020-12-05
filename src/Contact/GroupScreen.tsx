import React, { useEffect, useState } from 'react'
import { Group } from '../helpers/interfaces';
import { Text, TextInput, View, Alert } from 'react-native';
import GroupList from '../components/GroupList';
import styles from "./ContactsStyle";
import { getGroups } from '../helpers/network';
import user from '../../config/user';
import { createStackNavigator } from '@react-navigation/stack';
import GroupDetail from './GroupDetail';
import { Entypo, Feather } from "@expo/vector-icons";
import colors from "../../config/colors";
import font from "../../config/font";

function GroupScreen({ navigation }: any) {
    let focusListener: () => {};

    const [groupConnections, setGroupConnections] = useState<Group[]>([]);
    const [keyword, setKeyword] = useState("");

    const refreshData = () => {
        getGroups(user.email).then(response => response.json()).then(json => {
            if (json["success"]) {
                setGroupConnections(json["response"]);
            }
        }).catch(err => {
            console.log(err);
        })
    }
    const makeListeners = () => {
        focusListener = navigation.addListener("focus", () => {
            refreshData();
        });
    };
    useEffect(() => {
        refreshData();
        makeListeners()
    }, []);

    const updateKeyword = (value:string) => {
      setKeyword(value);
    };
    useEffect(() => {
      handleSearch();
    }, [keyword]);

    const handleSearch = () => {
      let groupList = groupConnections;

      var kw = keyword.toLowerCase();
      let filteredGroupList = groupList.filter((item) => {
        if(item["group_name"].toLowerCase().includes(kw))
          return item;
      })

      if(!keyword || keyword == '') {
        setGroupConnections(
          groupList
        )
      } else if(Array.isArray(filteredGroupList)) {
        setGroupConnections(
          filteredGroupList
        )
      }
      console.log(groupConnections);
      if (keyword === "" || !keyword.trim().length) refreshData();
    };

    return (
        <View style={styles.container}>
        <View style={{ width: '100%', marginTop: 0, justifyContent:'center', flexDirection:'row', alignItems:'center', paddingHorizontal: 16 }}>

          <Feather name="search" style={{  fontSize: 20 }} />
          <TextInput
            value={keyword}
            onChangeText={updateKeyword}
            style={{
              backgroundColor:colors.background,
              width:'95%',
              paddingHorizontal:16,
              height: 50,
              color:colors.text,
              fontFamily:font.regular
            }}
            placeholder="Search Contacts"/>
        </View>
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
