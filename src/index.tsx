import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import ScanScreen from './ScanScreen';
import React from 'react'
import ProfileScreen from './ProfileScreen';
import ContactScreen from './ContactScreen';
import { Ionicons } from '@expo/vector-icons';


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
    
    }>
        <Tab.Screen name="Profile" component={ProfileScreen} />
        <Tab.Screen name="Scan" component={ScanScreen} />
        <Tab.Screen name="Contacts" component={ContactScreen} />
    </Tab.Navigator>
  );
}