import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import ScanScreen from './ScanScreen';
import React from 'react'
import ProfileScreen from './ProfileScreen';
import ContactScreen from './ContactScreen';

const Tab = createBottomTabNavigator();

export default function Tabs() {
  return (
    <Tab.Navigator>
        <Tab.Screen name="Settings" component={ProfileScreen} />
        <Tab.Screen name="Scan" component={ScanScreen} />
        <Tab.Screen name="Contacts" component={ContactScreen} />
    </Tab.Navigator>
  );
}