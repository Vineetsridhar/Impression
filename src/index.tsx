import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import React from 'react'
import ProfileScreen from './Profile/ProfileScreen';
import ContactScreen from './Contact/ContactScreen';
import { Ionicons } from '@expo/vector-icons';
import Scan from './Scan'

const Tab = createBottomTabNavigator();

export default function Tabs() {
  return (
    <Tab.Navigator screenOptions={({route}) => ({
        tabBarIcon: ({ focused, color, size }) => {
            let iconName:string;
    
            if (route.name === 'Scan') {
                iconName = 'md-qr-scanner';
            } else if (route.name === 'Profile') {
                iconName = 'md-person';
            } else {
                iconName = "md-people"
            }
    
            return <Ionicons name={iconName} size={size} color={color} />;
          },
        })
    }
    initialRouteName={"Scan"}>
        <Tab.Screen name="Profile" component={ProfileScreen} />
        <Tab.Screen name="Scan" component={Scan} />
        <Tab.Screen name="Contacts" component={ContactScreen} />
    </Tab.Navigator>
  );
}